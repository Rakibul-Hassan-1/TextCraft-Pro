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
        try:
            subprocess.run(["python", "converter.py"], check=True)
            messagebox.showinfo("Success", "Script 1 executed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to execute Script 1:\n{e}")

    def run_script2(self):
        try:
            subprocess.run(["python", "translator.py"], check=True)
            messagebox.showinfo("Success", "Script 2 executed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to execute Script 2:\n{e}")


# Create the application window
root = ctk.CTk()
app = DynamicButtonApp(root)
root.mainloop()
