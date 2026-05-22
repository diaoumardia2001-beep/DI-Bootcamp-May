# # Exercise 1: Cats
# # Key Python Topics:

# # Classes and objects
# # Object instantiation
# # Attributes
# # Functions

# # Step 1: Create Cat Objects
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("mimi", 4)
cat2 = Cat("george", 9)
cat3 = Cat("marie", 2)
print(f"{cat1.name} is {cat1.age} years old.")
print(f"{cat2.name} is {cat2.age} years old.")
print(f"{cat3.name} is {cat3.age} years old.")

# # Step 2: Create a Function to Find the Oldest Cat
def find_oldest_cat(cat_a, cat_b, cat_c):
    oldest = cat_a
    if cat_b.age > oldest.age:
        oldest = cat_b
    if cat_c.age > oldest.age:
        oldest = cat_c
    return oldest

# Step 3: Print the Oldest Cat's Details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


# Exercise 2 : Dogs
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Create Dog Objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

# Step 3: Print Dog Details and Call Methods
print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print("---")

print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare Dog Sizes
print("\n--- Comparaison des tailles")
if davids_dog.height > sarahs_dog.height:
    print(f"The biggest dog is {davids_dog.name}!")
elif sarahs_dog.height > davids_dog.height:
    print(f"The biggest dog is {sarahs_dog.name}!")
else:
    print("Both dogs are exactly the same size!")


# Exercise 3 : Who's the song producer?
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There's a lady who's sure",
    "All that glitters is gold",
    "And she's buying a stairway to heaven"
])
stairway.sing_me_a_song()


# Exercise 4 : Afternoon at the Zoo
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        print(f"Zoo '{self.name}' has been created!")

    def add_animal(self, *args):
        for animal in args:
            if animal not in self.animals:
                self.animals.append(animal)
                print(f"{animal} has been added to {self.name}.")
            else:
                print(f"{animal} is already in the zoo!")

    def get_animals(self):
        if not self.animals:
            print("No animals in the zoo.")
        else:
            print(f"Animals in {self.name}: {', '.join(self.animals)}")

    def sell_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal} has been sold from {self.name}.")
        else:
            print(f"{animal} not found in {self.name}.")

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)
        return grouped_animals

    def get_groups(self):
        animal_groups = self.sort_animals()
        print(f"\n--- Grouped Animals in {self.name} ---")
        for letter, list_of_animals in animal_groups.items():
            animals_string = ", ".join(list_of_animals)
            print(f"Letter {letter}: {animals_string}")


# Step 2: Create a Zoo Object
my_zoo = Zoo("San Diego Zoo")
print("=== 1. CREATING THE ZOO ===")
safari_zoo = Zoo("Pretoria Wild Safari")
print("\n=== 2. ADDING ANIMALS ===")
safari_zoo.add_animal("Lion", "Leopard", "Cheetah", "Zebra", "Chimpanzee", "Leopard")
print("\n=== 3. DISPLAYING ANIMALS ===")
safari_zoo.get_animals()
print("\n=== 4. SELLING ANIMALS ===")
safari_zoo.sell_animal("Cheetah")
safari_zoo.sell_animal("Elephant")
print("\n=== 6. FINAL VERIFICATION ===")
safari_zoo.get_groups()
safari_zoo.get_animals()