# recipe_book/ingredient.py
class Ingredient:
    def __init__(self, name, protein, fat, carbohydrates):
        self.name = name
        self.protein = protein
        self.fat = fat
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"{self.name} (Białko: {self.protein}, Tłuszcz: {self.fat}, Węglowodany: {self.carbohydrates})"
