#Exercise 1: Converting Lists into Dictionaries
#Key Python Topics:
#Creating dictionaries
#Zip function or dictionary comprehension
#Instructions:
#You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
#Lists:
#keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30]
#Expected Output:
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
keys = ['ten', 'twenty', 'thirty']
values = [10, 20,30]
my_dict = dict(zip(keys, values))
print(my_dict)

# Exercise 2: Cinemax #2
#Key Python Topics:
#Conditional statements
#Loops
#Functions
#Dictionaries
#Instructions:
#Write a program that calculates the total cost of movie tickets for a family based on their ages.
#Family members’ ages are stored in a dictionary.
#The ticket prices are as follows:
#under 3 years: Free
#3 to 12 years: $10 
#over 12 years: $15
#Family Data:
#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#Loop through the family dictionary to calculate the total cost.
#Print the ticket price for each family member.
#Print the total cost at the end.

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
def calculate_ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else: 
        return 15
total_cost = 0
for member, age in family.items():
    ticket_price = calculate_ticket_price(age)
    print(f'{member.capitalize()} : ${ticket_price}')
    total_cost += ticket_price
print(f'Total cost : ${total_cost}')

#Bonus:
#Allow the user to input family members’ names and ages, then calculate the total ticket cost.

def calculate_ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else: 
        return 15
family = {}
print("Enter family members' names and ages. Type 'quit' to stop.")
while True:
    name = input("Enter the name of the family member : ")
    if name.lower() == 'quit':
        break
        
    age_input = input(f"Enter the age of {name} : ")
    if age_input.lower() == 'quit':
        break
    
    age = int(age_input)
    family[name] = age
total_cost = 0

for member, age in family.items():
    ticket_price = calculate_ticket_price(age)
    print(f"- {member.capitalize()} ({age} years) : ${ticket_price}")
    total_cost += ticket_price

print("-" * 30)
print(f"Total cost to pay : ${total_cost}")

#Exercise 3: Zara
#Key Python Topics:
#creating dictionaries
#accessing and modifying dictionary elements
#dictionary methods like .pop() and .update()
#Instructions:
#Create and manipulate a dictionary that contains information about the Zara brand.
#Brand Information:
#name: Zara
#creation_date: 1975
#creator_name: Amancio Ortega Gaona
#type_of_clothes: men, women, children, home
#international_competitors: Gap, H&M, Benetton
#number_stores: 7000
#major_color: 
    #France: blue, 
    #Spain: red, 
    #US: pink, green
zara_info = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
print(zara_info)

#Create a dictionary called brand with the provided data.
#Modify and access the dictionary as follows:
#Change the value of number_stores to 2.
#Print a sentence describing Zara’s clients using the type_of_clothes key.
#Add a new key country_creation with the value Spain.
#Check if international_competitors exists and, if so, add “Desigual” to the list.
#Delete the creation_date key.
#Print the last item in international_competitors.
#Print the major colors in the US.
#Print the number of keys in the dictionary.
#Print all keys of the dictionary.

zara_info["number_stores"] = 2
print(f"zara sells {zara_info['country_creation']} {zara_info['type_of_clothes']} clothes")
zara_info["country_creation"] = "spain"
if "international_competitors" in zara_info:
    zara_info["international_competitors"].append("desigual")

zara_info.pop("creation_date")

def new_func(zara_info):
    print(zara_info["international_competitors"][-1])
    print(zara_info["major_color"]["US"])
    print(len(zara_info))
    print(zara_info.keys())

new_func(zara_info)

#Bonus:
#Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

more_on_zara = {"creation_date": 1975, "number_stores": 7000}
zara_info.update(more_on_zara)
print(zara_info)

#Exercise 4 : Some Geography
#Key Python Topics:
#Functions with multiple parameters
#Default parameter values
#String formatting
#Step 1: Define a Function with Parameters
#Define a function named describe_city().
#This function should accept two parameters: city and country.
#Give the country parameter a default value, such as “Unknown”.
def describe_city(city, country="unknown"):
    print(f"{city} is in {country}.")
    describe_city("Reykjavik", "Iceland")
#Step 2: Print a Message
#Inside the function, set up the code to display a sentence like “ is in “.
#Replace <city> and <country> with the parameter values.
    describe_city("Paris")
#Step 3: Call the Function
#Call the describe_city() function with different city and country combinations.
#Try calling it with and without providing the country argument to see the default value in action.
#Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").
#Résultat attendu :
#Reykjavik is in Iceland.
#Paris is in Unknown.
describe_city("Reykjavik", "Iceland")
describe_city("Paris")

#Exercise 5 : Random
#Goal: Create a function that generates random numbers and compares them.
#Key Python Topics:
#random module
#random.randint() function
#Conditional statements (if, else)
#Step 1: Import the random Module
#At the beginning of your script, use import random to access the random number generation functions.
import random
#Step 2: Define a Function with a Parameter
#Create a function that accepts a number between 1 and 100 as a parameter.
def compare_random_number(user_number):
    if 1 <= user_number <= 100:
        random_number = random.randint(1, 100)
        print(f"your number: {user_number}, random number: {random_number}")
        if user_number > random_number:
            print("your number is higher than the random number.")
        elif user_number < random_number:
            print("your number is lower than the random number.")
        else:
            print("your number is equal to the random number.")
    else:
        print("please enter a number between 1 and 100.")

#Step 3: Generate a Random Number 
#Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.
import random
def compare_random_number(user_number):
    if 1 <= user_number <= 100:
        random_number = random.randint(1, 100)
        print(f"your number: {user_number}, random number: {random_number}")
        if user_number > random_number:
            print("your number is higher than the random number.")
        elif user_number < random_number:
            print("your number is lower than the random number.")
        else:
            print("your number is equal to the random number.")
    else:
        print("please enter a number between 1 and 100.")

#Step 4: Compare the Numbers
#If they are the same, print a success message. Otherwise, print a fail message and display both numbers.
compare_random_number(50)
#Step 5: Call the Function
#Call the function with a number between 1 and 100.
compare_random_number(50)


# Exercise 6 : Let’s create some personalized shirts !
#Goal: Create a function to describe a shirt’s size and message, with default values.
#Key Python Topics:
#Functions with parameters and default values
#Keyword arguments
#Step 1: Define a Function with Parameters
#Define a function called make_shirt().
#This function should accept two parameters: size and text.
def make_shirt(size="large", text="I love Python"):
    print(f"Shirt size: {size}, Message: {text}")

#Step 2: Print a Summary Message
#Set up the function to display a sentence summarizing the shirt’s size and message.
def make_shirt(size="large", text="I love Python"):
    print(f"Shirt size: {size}, Message: {text}")   

#Step 3: Call the Function
#Step 4: Modify the Function with Default Values
#Modify the make_shirt() function so that size has a default value of “large” and text has a default value of “I love Python”.
def make_shirt(size="large", text="I love Python"):
    print(f"Shirt size: {size}, Message: {text}")
#Step 5: Call the Function with Default and Custom Values
#Call make_shirt() to make a large shirt with the default message.
#Call make_shirt() to make a medium shirt with the default message.
#Call make_shirt() to make a shirt of any size with a different message.
make_shirt()
make_shirt(size="medium")
make_shirt(size="small", text="Hello, World!")
#Step 6 (Bonus): Keyword Arguments
#Call make_shirt() using keyword arguments (e.g., make_shirt(size="small", text="Hello!")).
make_shirt(size="small", text="Hello!")

#Exercise 7 : Temperature Advice
#Goal: Generate a random temperature and provide advice based on the temperature range.
#Key Python Topics:
#Functions
#Conditionals (if / elif)
#Random numbers
#Floating-point numbers (Bonus)
#Handling seasons (Bonus)
#Step 1: Create the get_random_temp() Function
#Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.
import random
def get_random_temp():
    return random.randint(-10, 40)  

#Step 2: Create the main() Function
#Create a function called main(). Inside this function:
#Call get_random_temp() to get a random temperature.
#Store the temperature in a variable and print a friendly message like:
#“The temperature right now is 32 degrees Celsius.”
def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")

#Step 3: Provide Temperature-Based Advice
#Inside main(), provide advice based on the temperature:
#Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
#Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
#Between 16°C and 23°C: e.g., “Nice weather.”
#Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
#Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”
def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 24:
        print("Nice weather.")
    elif 24 <= temp < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")


#Step 4: Floating-Point Temperatures (Bonus)
#Modify get_random_temp() to return a random floating-point number using random.uniform() for more accurate temperature values.
def get_random_temp():
    return random.uniform(-10, 40)

#Step 5: Month-Based Seasons (Bonus)
#Instead of directly generating a random temperature, ask the user for a month (1-12) and determine the season using if/elif conditions.
#Modify get_random_temp() to return temperatures specific to each season.
def get_random_temp(month):
    if month in [12, 1, 2]:  # Winter
        return random.uniform(-10, 10)
    elif month in [3, 4, 5]:  # Spring
        return random.uniform(0, 20)
    elif month in [6, 7, 8]:  # Summer
        return random.uniform(15, 40)
    elif month in [9, 10, 11]:  # Fall
        return random.uniform(5, 25)
    else:
        raise ValueError("Invalid month. Please enter a number between 1 and 12.")
def main():
    month = int(input("Enter the month (1-12): "))
    temp = get_random_temp(month)
    print(f"The temperature right now is {temp:.2f} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 24:
        print("Nice weather.")
    elif 24 <= temp < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")
main()

#Exercise 8: Pizza Toppings
#Key Python Topics:
#
#Loops
#Lists
#String formatting
#instructions:
#Write a loop that asks the user to enter pizza toppings one by one.
#Stop the loop when the user types 'quit'.
#For each topping entered, print:
#"Adding [topping] to your pizza."
#After exiting the loop, print all the toppings and the total cost of the pizza.
#The base price is $10, and each topping adds $2.50.
toppings = []
base_price = 10.0
price_per_topping = 2.50
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_cost = base_price + len(toppings) * price_per_topping
print(f"Your pizza has the following toppings: {', '.join(toppings)}.")
print(f"The total cost of your pizza is: ${total_cost:.2f}.")


