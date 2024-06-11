import unittest
from recipe_book.ingredient import Ingredient

class TestIngredient(unittest.TestCase):
    def test_to_dict(self):
        ingredient = Ingredient("Chicken", 25.0, 5.0, 0.0)
        self.assertEqual(ingredient.to_dict(), {
            "name": "Chicken",
            "protein": 25.0,
            "fat": 5.0,
            "carbohydrates": 0.0
        })

if __name__ == "__main__":
    unittest.main()
