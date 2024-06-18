import tkinter as tk
from tkinter import ttk, messagebox
from .recipe_book import RecipeBook
from .ingredient import Ingredient
from .recipe import Recipe
import os

# Klasa reprezentująca aplikację książki kucharskiej.
class RecipeBookApp:
    def __init__(self, root):
        self.root = root  # Główne okno aplikacji.
        self.root.title("Książka Kucharska")  # Tytuł okna aplikacji.
        self.recipe_book = RecipeBook("recipes", "charts")  # Inicjalizacja książki kucharskiej.

        self.setup_ui()  # Ustawienie interfejsu użytkownika.

    def setup_ui(self):
        # Konfiguracja interfejsu użytkownika.
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Nazwa Przepisu:").grid(row=0, column=0, sticky=tk.W)
        self.recipe_name = ttk.Entry(frame, width=30)
        self.recipe_name.grid(row=0, column=1, sticky=(tk.W, tk.E))

        self.ingredients = []  # Lista składników.
        ttk.Button(frame, text="Dodaj Składnik", command=self.add_ingredient).grid(row=0, column=2, sticky=tk.W)
        self.ingredient_list = tk.Listbox(frame, height=10, width=50)
        self.ingredient_list.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))
        ttk.Button(frame, text="Usuń Składnik", command=self.remove_ingredient).grid(row=1, column=2, sticky=tk.W)

        ttk.Button(frame, text="Dodaj Przepis", command=self.add_recipe).grid(row=2, column=0, sticky=tk.W)
        ttk.Button(frame, text="Usuń Przepis", command=self.remove_recipe).grid(row=2, column=1, sticky=tk.W)
        ttk.Button(frame, text="Znajdź Przepis", command=self.find_recipe).grid(row=2, column=2, sticky=tk.W)

        self.recipe_list = tk.Listbox(frame, height=10, width=50)
        self.recipe_list.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E))

        self.load_recipes()  # Załadowanie listy przepisów.

    def load_recipes(self):
        # Załadowanie przepisów z katalogu.
        self.recipe_list.delete(0, tk.END)
        for filename in os.listdir("recipes"):
            if filename.endswith(".json"):
                self.recipe_list.insert(tk.END, filename[:-5])

    def add_ingredient(self):
        # Dodanie składnika do przepisu.
        top = tk.Toplevel(self.root)
        top.title("Dodaj Składnik")

        ttk.Label(top, text="Nazwa:").grid(row=0, column=0, sticky=tk.W)
        name_entry = ttk.Entry(top, width=30)
        name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(top, text="Białko:").grid(row=1, column=0, sticky=tk.W)
        protein_entry = ttk.Entry(top, width=30)
        protein_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Label(top, text="Tłuszcz:").grid(row=2, column=0, sticky=tk.W)
        fat_entry = ttk.Entry(top, width=30)
        fat_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

        ttk.Label(top, text="Węglowodany:").grid(row=3, column=0, sticky=tk.W)
        carbs_entry = ttk.Entry(top, width=30)
        carbs_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

        def on_add():
            # Akcja dodania składnika.
            name = name_entry.get().strip()
            protein = float(protein_entry.get().strip())
            fat = float(fat_entry.get().strip())
            carbohydrates = float(carbs_entry.get().strip())

            ingredient = Ingredient(name, protein, fat, carbohydrates)
            self.ingredients.append(ingredient)
            self.ingredient_list.insert(tk.END, str(ingredient))
            top.destroy()

        ttk.Button(top, text="Dodaj", command=on_add).grid(row=4, column=1, sticky=tk.W)

    def remove_ingredient(self):
        # Usunięcie składnika z przepisu.
        selected = self.ingredient_list.curselection()
        if selected:
            self.ingredients.pop(selected[0])
            self.ingredient_list.delete(selected[0])

    def add_recipe(self):
        # Dodanie przepisu do książki kucharskiej.
        name = self.recipe_name.get().strip()
        if name and self.ingredients:
            recipe = Recipe(name, self.ingredients)
            self.recipe_book.add_recipe(recipe)
            self.load_recipes()
            messagebox.showinfo("Sukces", f"Przepis {name} został dodany!")
        else:
            messagebox.showwarning("Błąd", "Nazwa przepisu i składniki nie mogą być puste!")

    def remove_recipe(self):
        # Usunięcie przepisu z książki kucharskiej.
        selected = self.recipe_list.curselection()
        if selected:
            name = self.recipe_list.get(selected[0])
            self.recipe_book.remove_recipe(name)
            self.load_recipes()
            messagebox.showinfo("Sukces", f"Przepis {name} został usunięty!")
        else:
            messagebox.showwarning("Błąd", "Wybierz przepis do usunięcia!")

    def find_recipe(self):
        # Wyszukanie przepisu w książce kucharskiej.
        name = self.recipe_name.get().strip()
        if name:
            recipe = self.recipe_book.find_recipe(name)
            if recipe:
                self.show_recipe_details(recipe)
                chart_path = recipe.generate_nutrition_chart(self.recipe_book.charts_directory)
                messagebox.showinfo("Sukces", f"Wykres wartości odżywczych dla {name} został zapisany!\n{chart_path}")
            else:
                messagebox.showwarning("Błąd", f"Przepis {name} nie został znaleziony!")
        else:
            messagebox.showwarning("Błąd", "Nazwa przepisu nie może być pusta!")

    def show_recipe_details(self, recipe):
        # Wyświetlenie szczegółów przepisu.
        top = tk.Toplevel(self.root)
        top.title(f"Przepis: {recipe.name}")

        ingredients_text = "\n".join([str(ingredient) for ingredient in recipe.ingredients])
        ttk.Label(top, text=ingredients_text).grid(row=0, column=0, sticky=(tk.W, tk.E))
