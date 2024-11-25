import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from googletrans import Translator
import threading
import pysrt


class SubtitleTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TextCraft Pro")
        self.root.geometry("800x500")
        self.root.configure(bg="#f7f7f7")
        self.root.resizable(False, False)

        self.input_file = ""
        self.translated_content = ""  # To store translated SRT content
        self.translation_in_progress = False  # Track translation progress
        self.zoom_factor = 12  # Default font size for SRT content
        self.ctrl_pressed = False  # Track whether Ctrl key is pressed

        self.setup_styles()
        self.create_widgets()

        # Bind key events for zooming
        self.root.bind("<Control_L>", self.ctrl_press)
        self.root.bind("<Control_R>", self.ctrl_press)
        self.root.bind("<KeyRelease-Control_L>", self.ctrl_release)
        self.root.bind("<KeyRelease-Control_R>", self.ctrl_release)
        self.root.bind("<MouseWheel>", self.handle_zoom)  # For Windows and macOS
        self.root.bind("<Button-4>", self.handle_zoom)   # For Linux (scroll up)
        self.root.bind("<Button-5>", self.handle_zoom)   # For Linux (scroll down)

    def setup_styles(self):
        ctk.set_appearance_mode("System")  # Set system theme (light/dark)
        ctk.set_default_color_theme("blue")  # Use the blue color theme

    def create_widgets(self):
        frame = ctk.CTkFrame(self.root)
        frame.pack(expand=True, fill=ctk.BOTH, padx=20, pady=20)

        title_label = ctk.CTkLabel(frame, text="Chinese to English Subtitle Translator", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        input_frame = ctk.CTkFrame(frame)
        input_frame.pack(fill=ctk.X, pady=5)
        ctk.CTkLabel(input_frame, text="Select Chinese SRT File:").pack(anchor=ctk.W)
        self.input_file_entry = ctk.CTkEntry(input_frame, width=500)
        self.input_file_entry.pack(side=ctk.LEFT, padx=5)
        ctk.CTkButton(input_frame, text="Browse", command=self.open_file).pack(side=ctk.RIGHT)

        self.translate_button = ctk.CTkButton(frame, text="Start Translation", command=self.start_translation)
        self.translate_button.pack(pady=20)

        self.cancel_button = ctk.CTkButton(
            frame,
            text="Cancel Translation",
            command=self.cancel_translation,
            state=ctk.DISABLED,
            fg_color="green",  # Set the button's background color to red
            hover_color="#cc0000",  # A slightly darker red for hover effect
            text_color="white"  # Ensure the text is readable
        )
        self.cancel_button.pack(pady=10)

        self.progress = ctk.CTkProgressBar(frame, width=500, mode="determinate")
        self.progress.pack(pady=10)

        self.status_label = ctk.CTkTextbox(frame, height=5, wrap="word", state="disabled")
        self.status_label.pack(pady=5, expand=True, fill=ctk.BOTH)
        self.update_status("Status: Waiting for input...")  # Initial status message

    def update_status(self, message):
        self.status_label.configure(state="normal")
        self.status_label.insert(ctk.END, f"{message}\n")
        self.status_label.configure(state="disabled")
        self.status_label.see(ctk.END)

    def open_file(self):
        self.input_file = filedialog.askopenfilename(filetypes=[("SRT Files", "*.srt")])
        self.input_file_entry.delete(0, ctk.END)
        self.input_file_entry.insert(0, self.input_file)

    def start_translation(self):
        if not self.input_file:
            messagebox.showwarning("Missing Information", "Please select an input file.")
            return

        self.translate_button.configure(state=ctk.DISABLED)
        self.cancel_button.configure(state=ctk.NORMAL)
        self.progress.set(0)
        self.update_status("Status: Translating...")

        self.translation_thread = threading.Thread(target=self.translate_srt)
        self.translation_thread.daemon = True
        self.translation_thread.start()

    def cancel_translation(self):
        self.translation_in_progress = False
        self.update_status("Status: Translation cancelled.")
        self.translate_button.configure(state=ctk.NORMAL)
        self.cancel_button.configure(state=ctk.DISABLED)
        self.progress.set(0)

    def translate_srt(self):
        try:
            self.translation_in_progress = True
            subs = pysrt.open(self.input_file, encoding="utf-8")
            translator = Translator()

            total_subs = len(subs)
            for idx, sub in enumerate(subs):
                if not self.translation_in_progress:
                    self.update_status("Status: Translation stopped by user.")
                    return

                translated_text = translator.translate(sub.text, src="zh-CN", dest="en").text
                sub.text = translated_text

                progress = ((idx + 1) / total_subs) * 100
                self.root.after(0, lambda v=progress: self.progress.set(v))
                self.update_status(f"Progress: Translated line {idx + 1}/{total_subs}")

            if self.translation_in_progress:
                self.translated_content = "\n".join([str(sub) for sub in subs])
                self.root.after(0, self.show_result_window)

        except Exception as e:
            self.root.after(0, lambda: self.handle_error(e))

    def show_result_window(self):
        self.update_status("Status: Translation complete!")
        self.translate_button.configure(state=ctk.NORMAL)
        self.cancel_button.configure(state=ctk.DISABLED)

        result_window = ctk.CTkToplevel(self.root)
        result_window.title("Translation Result")
        result_window.geometry("900x500")
        result_window.resizable(True, True)

        left_frame = ctk.CTkFrame(result_window)
        left_frame.pack(side=ctk.LEFT, expand=True, fill=ctk.BOTH)

        right_frame = ctk.CTkFrame(result_window)
        right_frame.pack(side=ctk.RIGHT, expand=True, fill=ctk.BOTH)

        ctk.CTkLabel(left_frame, text="Original File (Chinese):", font=("Arial", 12, "bold")).pack(pady=5)
        self.original_text = ctk.CTkTextbox(left_frame, wrap="word", height=20, width=50, font=("Arial", self.zoom_factor))
        self.original_text.pack(expand=True, fill=ctk.BOTH)
        with open(self.input_file, "r", encoding="utf-8") as f:
            self.original_text.insert(ctk.END, f.read())
        self.original_text.configure(state=ctk.DISABLED)

        ctk.CTkLabel(right_frame, text="Translated File (English):", font=("Arial", 12, "bold")).pack(pady=5)
        self.translated_text = ctk.CTkTextbox(right_frame, wrap="word", height=20, width=50, font=("Arial", self.zoom_factor))
        self.translated_text.pack(expand=True, fill=ctk.BOTH)
        self.translated_text.insert(ctk.END, self.translated_content)
        self.translated_text.configure(state=ctk.DISABLED)

        # Add a download button
        download_button = ctk.CTkButton(result_window, text="Download Translated SRT", command=self.download_translated_file)
        download_button.pack(pady=10)

    def download_translated_file(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".srt", filetypes=[("SRT Files", "*.srt")])
        if save_path:
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(self.translated_content)
            messagebox.showinfo("Success", f"Translated file saved as:\n{save_path}")

    def handle_zoom(self, event):
        """Handle zooming with Ctrl + Mouse Wheel."""
        if self.ctrl_pressed:
            if event.delta > 0 or event.num == 4:  # Scroll up
                self.zoom_factor += 2
            elif event.delta < 0 or event.num == 5:  # Scroll down
                self.zoom_factor = max(8, self.zoom_factor - 2)
            self.update_zoom()

    def update_zoom(self):
        """Apply zoom to both text areas."""
        new_font = ("Arial", self.zoom_factor)
        if hasattr(self, "original_text"):
            self.original_text.configure(font=new_font)
        if hasattr(self, "translated_text"):
            self.translated_text.configure(font=new_font)

    def ctrl_press(self, event):
        """Track when Ctrl is pressed."""
        self.ctrl_pressed = True

    def ctrl_release(self, event):
        """Track when Ctrl is released."""
        self.ctrl_pressed = False

    def handle_error(self, error_message):
        self.update_status(f"Status: Error occurred - {error_message}")
        messagebox.showerror("Error", f"An error occurred: {error_message}")
        self.translate_button.configure(state=ctk.NORMAL)
        self.cancel_button.configure(state=ctk.DISABLED)


if __name__ == "__main__":
    root = ctk.CTk()
    app = SubtitleTranslatorApp(root)
    root.mainloop()
