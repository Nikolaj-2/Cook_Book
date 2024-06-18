# Klasa reprezentująca składnik przepisu.
class Ingredient:
    def __init__(self, name, protein, fat, carbohydrates):
        self.name = name  # Nazwa składnika.
        self.protein = protein  # Zawartość białka.
        self.fat = fat  # Zawartość tłuszczu.
        self.carbohydrates = carbohydrates  # Zawartość węglowodanów.

    def __repr__(self):
        # Reprezentacja tekstowa składnika.
        return f"{self.name} (Białko: {self.protein}, Tłuszcz: {self.fat}, Węglowodany: {self.carbohydrates})"
