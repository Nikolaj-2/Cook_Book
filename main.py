# main.py
import tkinter as tk
from recipe_book.recipe_book_app import RecipeBookApp

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeBookApp(root)
    root.mainloop()
