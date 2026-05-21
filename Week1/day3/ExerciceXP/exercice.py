# Exercise 1: Cats
# Key Python Topics:

# Classes and objects
# Object instantiation
# Attributes
# Functions


# Instructions:

# Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("mimi", 4)
cat2 = Cat("george", 9)
cat3 = Cat("marie", 2)

def find_oldest_cat(cats):
    
    oldest_cat = cat_list[0] 
    for cat in cat_list: 
        if cat.age > oldest_cat.age:
            oldest_cat = cat
            return oldest_cat
all_cast = [cat1, cat2, cat3]
oldest_cat = find_oldest_cat(all_cast)
print(f"the oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
