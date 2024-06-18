import matplotlib.pyplot as plt
import os

# Klasa reprezentująca przepis.
class Recipe:
    def __init__(self, name, ingredients):
        self.name = name  # Nazwa przepisu.
        self.ingredients = ingredients  # Lista składników przepisu.

    def get_nutritional_values(self):
        # Obliczanie sumarycznej zawartości białka, tłuszczu i węglowodanów w przepisie.
        protein = sum(ingredient.protein for ingredient in self.ingredients)
        fat = sum(ingredient.fat for ingredient in self.ingredients)
        carbohydrates = sum(ingredient.carbohydrates for ingredient in self.ingredients)
        return protein, fat, carbohydrates

    def generate_nutrition_chart(self, directory):
        # Generowanie wykresu wartości odżywczych przepisu.
        protein, fat, carbohydrates = self.get_nutritional_values()
        labels = ['Białko', 'Tłuszcz', 'Węglowodany']
        values = [protein, fat, carbohydrates]

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = os.path.join(directory, f"{self.name}_chart.svg")
        plt.savefig(filename, format='svg')
        plt.close()
        return filename
