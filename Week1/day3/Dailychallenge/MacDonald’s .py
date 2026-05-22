# Ce que vous apprendrez
# Classes et objets, Dictionnaires, Formatage de chaînes, Méthodes, Manipulation et tri des listes

# Instructions : La ferme du vieux MacDonald
# On vous fournit un exemple de code et son résultat.
# Votre tâche consiste à créer une classe Farm qui produit le même résultat.


# Étape 1 : Créer la classe Ferme
# Créez une classe appelée Farm.
# Cette classe représentera une ferme et ses animaux.

class Farm:
    pass


# Étape 2 : Implémenter la méthode __init__
# La classe Farm devrait avoir une méthode __init__.
# Elle prend un paramètre : farm_name.
# À l'intérieur de __init__, créez deux attributs :
# - name : pour stocker le nom de la ferme
# - animals : initialisé comme un dictionnaire vide

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

macdonald = Farm("McDonald")
print(macdonald.name)    # McDonald
print(macdonald.animals) # {}


# Étape 3 : Mettre en œuvre la méthode add_animal
# Créez une méthode appelée add_animal.
# Elle prend deux paramètres : animal_type et count (valeur par défaut de 1).
# Si animal_type existe déjà dans le dictionnaire, incrémentez son compteur de count.
# Sinon, ajoutez-le comme nouvelle clé avec count comme valeur.
# Exemple de dictionnaire : {'cow': 1, 'pig': 3, 'horse': 2}

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

macdonald = Farm("McDonald")
macdonald.add_animal("cow")
macdonald.add_animal("pig", 3)
macdonald.add_animal("horse", 2)
print(macdonald.animals) # {'cow': 1, 'pig': 3, 'horse': 2}


# Étape 4 : Mettre en œuvre la méthode get_info
# Créez une méthode appelée get_info.
# Elle retourne une chaîne affichant le nom de la ferme, les animaux et leur nombre,
# ainsi que la phrase "E-I-E-I-O!".
# Utilisez le formatage de chaînes pour aligner les noms et le nombre d'animaux.

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in sorted(self.animals.items()):
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-O!"
        return info

macdonald = Farm("McDonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)
print(macdonald.get_info())


# Étape 5 : Testez votre code
# Créez un objet Farm et appelez les méthodes add_animal et get_info.
# Vérifiez que le résultat correspond à l'exemple fourni.

macdonald = Farm("McDonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)
print(macdonald.get_info())
# Output:
# McDonald's farm
#
# cow : 5
# goat : 12
# sheep : 2
#
#     E-I-E-I-O!


# Bonus : Agrandissez la ferme

# Étape 6 : Mettre en œuvre la méthode get_animal_types
# Ajoutez une méthode get_animal_types à la classe Farm.
# Elle retourne une liste triée de tous les types d'animaux (clés du dictionnaire animals).
# Utilisez la fonction sorted() pour trier la liste.

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in sorted(self.animals.items()):
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-O!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

macdonald = Farm("McDonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)
print(macdonald.get_info())
print(macdonald.get_animal_types()) # ['cow', 'goat', 'sheep']


# Étape 7 : Mettre en œuvre la méthode get_short_info
# Ajoutez une méthode get_short_info à la classe Farm.
# Elle retourne une chaîne comme "McDonald's farm has cows, goats and sheeps."
# Appelez get_animal_types pour obtenir la liste des animaux.
# Ajoutez un "s" au nom de l'animal si son nombre est supérieur à 1.
# Utilisez le formatage de chaînes pour créer le résultat.

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in sorted(self.animals.items()):
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-O!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_list = [
            animal + "s" if self.animals[animal] > 1 else animal
            for animal in self.get_animal_types()
        ]
        if len(animal_list) > 1:
            animals_str = ", ".join(animal_list[:-1]) + " and " + animal_list[-1]
        else:
            animals_str = animal_list[0]
        return f"{self.name}'s farm has {animals_str}."

macdonald = Farm("McDonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info()) # McDonald's farm has cows, goats and sheeps.


# Étape 8 : Mettre à jour la méthode add_animal avec **kwargs
# Utilisez **kwargs pour passer plusieurs animaux en une seule fois.
# Les clés seront le nom de l'animal et les valeurs, la quantité.
# Exemple d'appel : macdonald.add_animal(cow=5, sheep=2, goat=12)

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, **kwargs):
        for animal_type, count in kwargs.items():
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in sorted(self.animals.items()):
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-O!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_list = [
            animal + "s" if self.animals[animal] > 1 else animal
            for animal in self.get_animal_types()
        ]
        if len(animal_list) > 1:
            animals_str = ", ".join(animal_list[:-1]) + " and " + animal_list[-1]
        else:
            animals_str = animal_list[0]
        return f"{self.name}'s farm has {animals_str}."

macdonald = Farm("McDonald")
macdonald.add_animal(cow=5, sheep=2, goat=12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())