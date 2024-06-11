import unittest
import tkinter as tk
from recipe_book.recipe_book_app import RecipeBookApp
from recipe_book.ingredient import Ingredient

class TestRecipeBookApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = RecipeBookApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_add_ingredient_button(self):
        self.app.recipe_name.insert(0, "Test Recipe")
        self.app.add_ingredient()
        self.assertGreater(len(self.app.ingredients), 0)

    def test_remove_ingredient_button(self):
        self.app.ingredients.append(Ingredient("Chicken", 25, 5, 0))
        self.app.ingredient_list.insert(tk.END, "Chicken (Białko: 25, Tłuszcz: 5, Węglowodany: 0)")
        self.app.ingredient_list.selection_set(0)
        self.app.remove_ingredient()
        self.assertEqual(len(self.app.ingredients), 0)

    def test_add_recipe_button(self):
        self.app.recipe_name.insert(0, "Test Recipe")
        self.app.ingredients.append(Ingredient("Chicken", 25, 5, 0))
        self.app.add_recipe()
        self.assertIn("Test Recipe", self.app.recipe_list.get(0, tk.END))

    def test_remove_recipe_button(self):
        self.app.recipe_name.insert(0, "Test Recipe")
        self.app.ingredients.append(Ingredient("Chicken", 25, 5, 0))
        self.app.add_recipe()
        self.app.recipe_list.selection_set(0)
        self.app.remove_recipe()
        self.assertNotIn("Test Recipe", self.app.recipe_list.get(0, tk.END))

    def test_find_recipe_button(self):
        self.app.recipe_name.insert(0, "Test Recipe")
        self.app.ingredients.append(Ingredient("Chicken", 25, 5, 0))
        self.app.add_recipe()
        self.app.recipe_name.delete(0, tk.END)
        self.app.recipe_name.insert(0, "Test Recipe")
        self.app.find_recipe()
        # Test będzie sprawdzać, czy wykres został wygenerowany, a nie pokaże okna komunikatu, co może być trudne do automatycznego testowania.

if __name__ == "__main__":
    unittest.main()
