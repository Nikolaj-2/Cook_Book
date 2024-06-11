import unittest
import os
import shutil
from recipe_book.recipe_book import RecipeBook
from recipe_book.ingredient import Ingredient
from recipe_book.recipe import Recipe

class TestRecipeBook(unittest.TestCase):
    def setUp(self):
        self.recipe_book = RecipeBook("test_recipes")
        self.ingredient1 = Ingredient("Chicken Breast", 31, 3.6, 0)
        self.ingredient2 = Ingredient("Olive Oil", 0, 13.5, 0)
        self.recipe = Recipe("Grilled Chicken", [self.ingredient1, self.ingredient2])
        self.recipe_book.add_recipe(self.recipe)

    def tearDown(self):
        shutil.rmtree("test_recipes")

    def test_add_and_find_recipe(self):
        recipe = self.recipe_book.find_recipe("Grilled Chicken")
        self.assertIsNotNone(recipe)
        self.assertEqual(recipe.title, "Grilled Chicken")

    def test_remove_recipe(self):
        self.recipe_book.remove_recipe("Grilled Chicken")
        recipe = self.recipe_book.find_recipe("Grilled Chicken")
        self.assertIsNone(recipe)

if __name__ == "__main__":
    unittest.main()
