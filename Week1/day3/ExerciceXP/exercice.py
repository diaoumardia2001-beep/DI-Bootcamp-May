# # Exercise 1: Cats
# # Key Python Topics:

# # Classes and objects
# # Object instantiation
# # Attributes
# # Functions


# # Instructions:

# # Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.
# # class Cat:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# # cat1 = Cat("mimi", 4)
# # cat2 = Cat("george", 9)
# # cat3 = Cat("marie", 2)

# # def find_oldest_cat(cats):
# #     oldest_cat = None
# #     for cat in cats:
# #         if oldest_cat is None or cat.age > oldest_cat.age:
# #             oldest_cat = cat
# #     return oldest_cat

# # oldest_cat = find_oldest_cat([cat1, cat2, cat3])
# # oldest_cat = None
# # all_casts = [cat1, cat2, cat3]
# # oldest_cat = find_oldest_cat(all_casts)
# # print(f"the oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

# # Step 1: Create Cat Objects
# # Use the Cat class to create three cat objects with different names and ages.
class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
cat1 = cat("mimi", 4)
cat2 = cat("george", 9)
cat3 = cat("marie", 2)
print(f"{cat1.name} is {cat1.age} years old.")
print(f"{cat2.name} is {cat2.age} years old.")
print(f"{cat3.name} is {cat3.age} years old.")

# # Step 2: Create a Function to Find the Oldest Cat
# # Create a function that takes the three cat objects as input.
# # Inside the function, compare the ages of the cats to find the oldest one.
# # Return the oldest cat object.

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def find_oldest_cat(cat_a, cat_b, cat_c):
        oldest_cat = cat_a
        if cat_b.age > oldest_cat.age:
            oldest_cat = cat_b
            if cat_c.age > oldest_cat.age:
                oldest_cat = cat_c
        return oldest_cat
cat1 = Cat("mimi", 4)
cat2 = Cat("george", 9)
cat3 = Cat("marie", 2)
oldest_cat = Cat.find_oldest_cat(cat1, cat2, cat3)

# print(f"the oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


# Step 3: Print the Oldest Cat’s Details
# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def find_oldest_cat(cat_a, cat_b, cat_c):
        oldest = cat_a
        if cat_b.age > oldest.age:
            oldest = cat_b
        if cat_c.age > oldest.age:
            oldest = cat_c
        return oldest   
    oldest_cat = find_oldest_cat(cat1, cat2, cat3)
    print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


# Exercise 2 : Dogs
# Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.



# Key Python Topics:

# Classes and objects
# Object instantiation
# Methods
# Attributes
# Conditional statements (if)


# Instructions:

# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Create Dog Objects

# Create davids_dog and sarahs_dog objects with their respective names and heights.
davids_dog = Dog("Rex", 50)
print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()
print("---")
sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

# Step 3: Print Dog Details and Call Methods
# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.

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

# Exercise 3 : Who’s the song producer?
# Goal: Create a Song class to represent song lyrics and print them.
# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Lists
# Instructions:
# Create a Song class with a method to print song lyrics line by line.
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

# Step 1: Create the Song Class
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line, end="")
stairway = Song([
    "There's a lady who's sure",
    "All that glitters is gold",
    "And she's buying a stairway to heaven"
])
stairway.sing_me_a_song()


# Exercise 4 : Afternoon at the Zoo
# Goal:
# Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.
# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Lists
# Dictionaries (for grouping)
# String manipulation
# Instructions
# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.
#2. Implement the __init__() method:
# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.
class Zoo:
    # 2. Implement the __init__() method
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

# 3. Add a method add_animal(new_animal):
# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.
def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been successfully added to the zoo.")
        else:
            print(f"{new_animal} is already in the zoo!")
    
# 4. Add a method get_animals():
# This method prints all animals currently in the zoo.
def get_animals(self):
        print(f"\n--- Animals in {self.name} ---")
        if self.animals:
            for animal in self.animals:
                print(f"- {animal}")
        else:
            print("The zoo is currently empty.")

# 5. Add a method sell_animal(animal_sold):
# This method checks if a specified animal exists on the animals list and if so, remove from it.
def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold and removed from the zoo.")
        else:
            print(f"Error: {animal_sold} cannot be sold because it is not in the zoo.")
# 6. Add a method sort_animals():
# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.

def organize_animals(self):
    sorted_animals = sorted(self.animals)
    grouped_animals = {}
    for animal in sorted_animals:
        first_letter = animal[0].upper()
        if first_letter not in grouped_animals:
            grouped_animals[first_letter] = []
        grouped_animals[first_letter].append(animal)
    return grouped_animals


# 7. Add a method get_groups():
# This method prints the grouped animals as created by sort_animals().

def get_groups(self):
        animal_groups = self.sort_animals()
        print(f"\n--- Grouped Animals in {self.name} ---")
        for letter, list_of_animals in animal_groups.items():
            animals_string = ", ".join(list_of_animals)
            print(f"Letter {letter}: {animals_string}")

# Step 2: Create a Zoo Object
# Create an instance of the Zoo class and pass a name for the zoo.

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        print(f"Zoo '{self.name}' has been created!")

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal} has been added to {self.name}.")

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

    def get_groups(self):
        groups = {}
        for animal in self.animals:
            groups[animal] = groups.get(animal, 0) + 1
        print("Animal groups:", groups)


# Step 2: Create a Zoo Object
my_zoo = Zoo("San Diego Zoo")
print("=== 1. CREATING THE ZOO ===")
safari_zoo = Zoo("Pretoria Wild Safari")
print("\n=== 2. ADDING ANIMALS ===")
safari_zoo.add_animal("Lion")
safari_zoo.add_animal("Leopard")
safari_zoo.add_animal("Cheetah")
safari_zoo.add_animal("Zebra")
safari_zoo.add_animal("Chimpanzee")
safari_zoo.add_animal("Leopard")
print("\n=== 3. DISPLAYING ANIMALS ===")
safari_zoo.get_animals()
print("\n=== 4. SELLING ANIMALS ===")
safari_zoo.sell_animal("Cheetah")
safari_zoo.sell_animal("Elephant")
print("\n=== 6. FINAL VERIFICATION ===")
safari_zoo.get_groups()
safari_zoo.get_animals()

# Bonus : Modifiez la add_animal()méthode pour éviter *argsde la répéter à chaque fois pour un nouvel animal ; vous pouvez désormais passer plusieurs noms d’animaux séparés par une virgule.

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        print(f"Zoo '{self.name}' has been created!")

    def add_animal(self, *args):
        for animal in args:
            self.animals.append(animal)
            print(f"{animal} has been added to {self.name}.")

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

    def get_groups(self):
        groups = {}
        for animal in self.animals:
            groups[animal] = groups.get(animal, 0) + 1
        print("Animal groups:", groups)


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