import os
import subprocess
import customtkinter as ctk
from tkinter import messagebox


class DynamicButtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TextCraft Pro")
        self.root.geometry("400x400")
        self.root.configure(bg="#f7f7f7")
        self.root.resizable(True, True)

        # Set up styles
        ctk.set_appearance_mode("System")  # System appearance (light/dark)
        ctk.set_default_color_theme("blue")

        # Create the frame for dynamic layout
        frame = ctk.CTkFrame(self.root)
        frame.pack(expand=True, fill=ctk.BOTH, padx=20, pady=20)

        # Title Label
        title_label = ctk.CTkLabel(frame, text="TextCraft Pro", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        # Buttons
        self.button1 = ctk.CTkButton(
            frame,
            text="SRT To Paragraph (Converter)",
            command=self.run_script1,
            fg_color="#4CAF50",
            hover_color="#388E3C",
        )
        self.button1.pack(pady=10, expand=True, fill=ctk.X)

        self.button2 = ctk.CTkButton(
            frame,
            text="Chinese To English (Translator)",
            command=self.run_script2,
            fg_color="#2196F3",
            hover_color="#1976D2",
        )
        self.button2.pack(pady=10, expand=True, fill=ctk.X)

        # Footer Label
        footer_label = ctk.CTkLabel(
            self.root,
            text="Developed by Rakibul Hassan\nCSE, PCIU",
            font=("Arial", 12),
        )
        footer_label.pack(side="bottom", pady=10)

    def run_script1(self):
        self.execute_script("app/backend/converter.py", "Converter app")

    def run_script2(self):
        self.execute_script("app/backend/translator.py", "Translator app")

    def execute_script(self, script_relative_path, app_name):
        """Helper method to execute a script and handle errors."""
        script_path = os.path.join(os.getcwd(), script_relative_path)  # Convert to absolute path
        print(f"Attempting to run: {script_path}")  # Debugging line
        try:
            if os.path.exists(script_path):
                # Use sys.executable to find the current Python interpreter
                subprocess.run([os.sys.executable, script_path], check=True)
                messagebox.showinfo("Success", f"{app_name} executed successfully!")
            else:
                messagebox.showerror("Error", f"Script not found: {script_path}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to execute {app_name}:\n{e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")


# Create the application window
if __name__ == "__main__":
    root = ctk.CTk()
    app = DynamicButtonApp(root)
    root.mainloop()
