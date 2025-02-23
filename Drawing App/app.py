import tkinter as tk
from tkinter import messagebox

# Sample database of entertainment options mapped to emotions
entertainment_data = {
    "happy": {
        "music": ["Happy - Pharrell Williams", "Good Vibrations - The Beach Boys"],
        "movies": ["The Pursuit of Happyness", "Sing"],
        "games": ["Just Dance", "Mario Kart"],
    },
    "sad": {
        "music": ["Someone Like You - Adele", "Fix You - Coldplay"],
        "movies": ["The Notebook", "A Beautiful Mind"],
        "games": ["Stardew Valley", "Journey"],
    },
    "angry": {
        "music": ["Smells Like Teen Spirit - Nirvana", "Killing in the Name - Rage Against the Machine"],
        "movies": ["Fight Club", "Gladiator"],
        "games": ["DOOM", "Call of Duty"],
    },
    "relaxed": {
        "music": ["Weightless - Marconi Union", "Clair de Lune - Debussy"],
        "movies": ["Amélie", "Forrest Gump"],
        "games": ["Flower", "Animal Crossing"],
    }
}

class EmotionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion-Driven Entertainment App")
        self.root.geometry("600x500")
        
        # Initialize favorites
        self.favorites = []

        # Main Menu Frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)
        
        # Emotion Selection
        self.emotions = ["happy", "sad", "angry", "relaxed"]
        self.create_main_menu()

    def create_main_menu(self):
        # Clear any existing frames
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Label
        label = tk.Label(self.main_frame, text="Select your current emotion:", font=("Helvetica", 16))
        label.pack(pady=20)
        
        # Buttons for each emotion
        for emotion in self.emotions:
            button = tk.Button(
                self.main_frame, 
                text=emotion.capitalize(), 
                font=("Helvetica", 14), 
                width=15, 
                command=lambda em=emotion: self.show_categories(em)
            )
            button.pack(pady=10)

    def show_categories(self, emotion):
        # Clear main frame for new content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Title for categories
        label = tk.Label(self.main_frame, text=f"Choose a category for '{emotion.capitalize()}' Mood", font=("Helvetica", 16))
        label.pack(pady=10)
        
        # Buttons for categories
        categories = entertainment_data[emotion].keys()
        for category in categories:
            button = tk.Button(
                self.main_frame, 
                text=category.capitalize(), 
                font=("Helvetica", 14), 
                width=15, 
                command=lambda em=emotion, cat=category: self.show_recommendations(em, cat)
            )
            button.pack(pady=10)

        # Back button
        back_button = tk.Button(self.main_frame, text="Back", font=("Helvetica", 12), command=self.create_main_menu)
        back_button.pack(pady=10)

    def show_recommendations(self, emotion, category):
        # Clear main frame for new content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Title for recommendations
        label = tk.Label(self.main_frame, text=f"{category.capitalize()} for '{emotion.capitalize()}' Mood", font=("Helvetica", 16))
        label.pack(pady=10)
        
        # Listbox to display recommendations
        self.recommendation_list = tk.Listbox(self.main_frame, font=("Helvetica", 12), width=50, height=15)
        self.recommendation_list.pack(pady=10)
        
        # Populate recommendations
        recommendations = entertainment_data[emotion].get(category, [])
        for item in recommendations:
            self.recommendation_list.insert(tk.END, item)
        
        # Add interaction to recommendations
        self.recommendation_list.bind("<<ListboxSelect>>", lambda event: self.add_to_favorites(emotion, category))
        
        # Back button
        back_button = tk.Button(self.main_frame, text="Back", font=("Helvetica", 12), command=lambda: self.show_categories(emotion))
        back_button.pack(pady=10)

        # View Favorites button
        favorites_button = tk.Button(self.main_frame, text="View Favorites", font=("Helvetica", 12), command=self.view_favorites)
        favorites_button.pack(pady=10)

    def add_to_favorites(self, emotion, category):
        # Get selected item
        selected_item = self.recommendation_list.get(self.recommendation_list.curselection())
        if selected_item not in self.favorites:
            self.favorites.append((selected_item, emotion, category))
            messagebox.showinfo("Added to Favorites", f"'{selected_item}' has been added to your favorites!")
        else:
            messagebox.showwarning("Already Favorited", f"'{selected_item}' is already in your favorites.")

    def view_favorites(self):
        # Clear main frame for new content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Title for favorites
        label = tk.Label(self.main_frame, text="Your Favorites", font=("Helvetica", 16))
        label.pack(pady=10)
        
        # Listbox to display favorites
        favorites_list = tk.Listbox(self.main_frame, font=("Helvetica", 12), width=50, height=15)
        favorites_list.pack(pady=10)
        
        # Populate favorites
        if self.favorites:
            for item, emotion, category in self.favorites:
                favorites_list.insert(tk.END, f"{item} ({category.capitalize()} - {emotion.capitalize()})")
        else:
            favorites_list.insert(tk.END, "No favorites yet!")

        # Back button
        back_button = tk.Button(self.main_frame, text="Back", font=("Helvetica", 12), command=self.create_main_menu)
        back_button.pack(pady=10)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = EmotionApp(root)
    root.mainloop()
