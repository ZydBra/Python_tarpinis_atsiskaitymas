# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu.
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas:
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.


class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def was_expansive(self):
        if self.budget >= 100000000:
            return True
        else:
            return False

    def __str__(self):
        return f"title: {self.title}, director: {self.director}, budget: {self.budget}, expensive: {self.was_expansive()}"


print(Movie("Karibų piratai", "Gore Verbinski", 140000000))
print(Movie("Trys milijonai eurų", "Tadas Vidmantas", 3000000))
