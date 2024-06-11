import unittest
import os
from recipe_book.ingredient import Ingredient
from recipe_book.recipe import Recipe

class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.ingredient1 = Ingredient("Chicken Breast", 31, 3.6, 0)
        self.ingredient2 = Ingredient("Olive Oil", 0, 13.5, 0)
        self.recipe = Recipe("Grilled Chicken", [self.ingredient1, self.ingredient2])

    def test_to_dict(self):
        self.assertEqual(self.recipe.to_dict(), {
            "title": "Grilled Chicken",
            "ingredients": [
                {"name": "Chicken Breast", "protein": 31, "fat": 3.6, "carbohydrates": 0},
                {"name": "Olive Oil", "protein": 0, "fat": 13.5, "carbohydrates": 0}
            ]
        })

    def test_save_and_load(self):
        self.recipe.save("test_recipes")
        loaded_recipe = Recipe.load("test_recipes/Grilled Chicken.json")
        self.assertEqual(loaded_recipe.title, self.recipe.title)
        self.assertEqual(len(loaded_recipe.ingredients), len(self.recipe.ingredients))
        os.remove("test_recipes/Grilled Chicken.json")

    def test_generate_nutrition_chart(self):
        self.recipe.generate_nutrition_chart("test_chart.svg")
        self.assertTrue(os.path.exists("test_chart.svg"))
        os.remove("test_chart.svg")

if __name__ == "__main__":
    unittest.main()
