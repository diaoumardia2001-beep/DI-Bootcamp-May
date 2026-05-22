# Exercice 1 : Animaux de compagnie
# Principaux sujets : Héritage, instanciation de classe, Listes, Polymorphisme

# Classes fournies
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Étape 1 : Créer la classe Siamese
# Créez une classe appelée Siamese qui hérite de la classe Cat.
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Étape 2 : Créer une liste d'instances de chat
# Créez une liste appelée all_cats contenant des instances de Bengal, Chartreux et Siamese.
bengal_cat = Bengal("Luna", 3)
chartreux_cat = Chartreux("Milo", 5)
siamese_cat = Siamese("Nala", 2)
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Étape 3 : Créer une instance Pets à partir de la liste des instances de chats
sara_pets = Pets(all_cats)

# Étape 4 : Emmener les chats en promenade
sara_pets.walk()


# Exercice 2 : Chiens
# Principaux sujets : Classes et objets, Méthodes, Attributs

# Étape 1 : Créer la classe Dog
# Créez une classe Dog avec name, age, et weight comme attributs.
# bark() retourne "<dog_name> barks"
# run_speed() retourne weight / age * 10
# fight(other_dog) retourne le chien gagnant basé sur run_speed * weight

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} barks"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f"{self.name} won the fight!"
        elif other_power > my_power:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a tie!"

# Étape 2 : Créer des instances de chien
dog1 = Dog("Rex", 5, 30)
dog2 = Dog("Buddy", 3, 20)
dog3 = Dog("Max", 4, 25)

# Étape 3 : Tester les méthodes sur les chiens
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))


# Exercice 3 : Chiens domestiqués
# Principaux sujets : Héritage, super(), *args, Module aléatoire

# Étape 1 : Importer le module random et réutiliser la classe Dog
import random

# Étape 2 : Créer la classe PetDog qui hérite de Dog
# - trained est initialisé à False
# - train() affiche bark() et met trained à True
# - play(*args) affiche "<dog_names> all play together"
# - do_a_trick() affiche un tour aléatoire si trained est True

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join(args)
        print(f"{self.name}, {dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet!")

# Étape 3 : Tester les méthodes PetDog
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()


# Exercice 4 : Cours en famille et par personne
# Principaux sujets : Classes, Méthodes d'instance, Listes, Conditions, f-strings

# Étape 1 : Créer la classe Person
# - Attributs : first_name, age, last_name (initialisé à "")
# - is_18() retourne True si age >= 18, sinon False

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18

# Étape 2 : Créer la classe Family
# - Attributs : last_name, members (liste vide)
# - born(first_name, age) : crée un Person, lui attribue le last_name, l'ajoute à members
# - check_majority(first_name) : vérifie si la personne a 18 ans ou plus
# - family_presentation() : affiche le nom de famille et chaque membre

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age)
        person.last_name = self.last_name
        self.members.append(person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"{first_name} not found in the family.")

    def family_presentation(self):
        print(f"Family name: {self.last_name}")
        for member in self.members:
            print(f"- {member.first_name}, age {member.age}")


# Test
my_family = Family("Dupont")
my_family.born("Alice", 20)
my_family.born("Tom", 15)
my_family.born("Emma", 18)

my_family.check_majority("Alice")
my_family.check_majority("Tom")
my_family.check_majority("Emma")

my_family.family_presentation()