import math

# Étape 1 : Créer la classe Pagination
# Définissez une classe appelée Pagination pour représenter du contenu paginé.

# Étape 2 : Implémenter la méthode __init__
# - items (défaut None) : liste d'éléments
# - page_size (défaut 10) : nombre d'éléments par page
# - Si items est None, initialiser comme liste vide
# - Sauvegarder page_size et définir current_idx à 0
# - Calculer le nombre total de pages avec math.ceil

class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    # Étape 3 : Implémenter get_visible_items()
    # Retourne les éléments visibles sur la page courante.
    # Utilise le slicing basé sur current_idx et page_size.
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # Étape 4 : Implémenter les méthodes de navigation
    # go_to_page(page_num) : va à la page spécifiée (indexation basée sur 1)
    # Lève une ValueError si page_num est hors limites
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page {page_num} is out of range. Valid pages: 1 to {self.total_pages}")
        self.current_idx = page_num - 1
        return self

    # first_page() : navigue vers la première page
    def first_page(self):
        self.current_idx = 0
        return self

    # last_page() : navigue vers la dernière page
    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    # next_page() : avance d'une page (si pas déjà sur la dernière)
    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    # previous_page() : recule d'une page (si pas déjà sur la première)
    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # Bonus - Étape 5 : Ajouter une méthode __str__()
    # Retourne une chaîne affichant les éléments de la page courante, chacun sur une nouvelle ligne.
    def __str__(self):
        return "\n".join(str(item) for item in self.get_visible_items())


# Étape 6 : Tester le code
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

try:
    p.go_to_page(10)
except ValueError as e:
    print(f"ValueError: {e}")
# ValueError: Page 10 is out of range.

try:
    p.go_to_page(0)
except ValueError as e:
    print(f"ValueError: {e}")
# ValueError: Page 0 is out of range.

# Bonus : method chaining
p.first_page()
print(p.next_page().next_page().next_page().get_visible_items())
# ['m', 'n', 'o', 'p']

# Bonus : __str__
p.first_page()
print(str(p))
# a
# b
# c
# d