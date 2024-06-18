import os
import json
from .recipe import Recipe
from .ingredient import Ingredient

# Klasa reprezentująca książkę kucharską.
class RecipeBook:
    def __init__(self, directory, charts_directory):
        self.directory = directory  # Katalog na przepisy.
        self.charts_directory = charts_directory  # Katalog na wykresy.
        if not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists(charts_directory):
            os.makedirs(charts_directory)

    def add_recipe(self, recipe):
        # Dodanie przepisu do książki kucharskiej.
        recipe_path = os.path.join(self.directory, f"{recipe.name}.json")
        with open(recipe_path, 'w') as file:
            json.dump({
                'name': recipe.name,
                'ingredients': [
                    {
                        'name': ingredient.name,
                        'protein': ingredient.protein,
                        'fat': ingredient.fat,
                        'carbohydrates': ingredient.carbohydrates
                    } for ingredient in recipe.ingredients
                ]
            }, file, indent=4)

    def remove_recipe(self, name):
        # Usunięcie przepisu z książki kucharskiej.
        recipe_path = os.path.join(self.directory, f"{name}.json")
        chart_path = os.path.join(self.charts_directory, f"{name}_chart.svg")
        if os.path.exists(recipe_path):
            os.remove(recipe_path)
        if os.path.exists(chart_path):
            os.remove(chart_path)

    def find_recipe(self, name):
        # Znalezienie przepisu w książce kucharskiej.
        recipe_path = os.path.join(self.directory, f"{name}.json")
        if os.path.exists(recipe_path):
            with open(recipe_path, 'r') as file:
                data = json.load(file)
                ingredients = [
                    Ingredient(ingredient['name'], ingredient['protein'], ingredient['fat'], ingredient['carbohydrates'])
                    for ingredient in data['ingredients']
                ]
                return Recipe(data['name'], ingredients)
        return None
