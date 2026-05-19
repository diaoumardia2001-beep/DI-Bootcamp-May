# Exercise 1 : Hello World
# Instructions
# print the following output using one line of code:
print("hello world")
print("hello world")
print("hello world")

# Exercise 2 : Some Math
# Instructions
#write code that calculates the result of:
print(99**3 * 8)
# Exercise 3 : What Is The Output ?
# Instructions
# predict the output of the following code snippets:
#comment what you guess, then run the code and compare
print(5 < 3) # False
print(3 == 3) # True    
print(3 == "3") # False

#typeError: '>' not supported between instances of 'str' and 'int'
print("Hello" == "hello") # False
# Exercise 4: Your computer brand
# Instructions
# create a variable called computer_brand which value is the brand of your computer
# using the computer_brand variable, print a sentence that states the brand of your computer
#following:
# "I have a <computer_brand> computer."
computer_brand = "Dell"
print("I have a " + computer_brand + " computer.")


# Exercise 5 : Your Information
# Instructions
#Create a variable called name, and set it’s value to your name.
#Create a variable called age, and set it’s value to your age.
#Create a variable called shoe_size, and set it’s value to your shoe size.
#Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
#Have your code print the info message.
#Run your code.
name = "Dia"
age = 25
shoe_size = 44
info = "my name is " + name + " and I am " + str(age) + " years old and my shoe size is " + str(shoe_size)
print(info)

#Exercise 6 : A et B
# Instructions
#Create two variables, a and b.
#Each variable’s value should be a number.
#If a is bigger than b, have your code print "Hello World".
a =30
b = 20
if a > b:
    print("Hello World")


#Exercise 7: Odd or Even
# Instructions
#Write code that asks the user for a number and determines whether this number is odd or even.
number = int(input("enter a number: "))
if number % 2 == 0:
    print("the number is even")
else:  print("the number is odd")

#Exercise 8: What’s your name?
# Instructions
#Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.
name = input("what is your name?")
if name == "Omar":
    print("we have the same name")
else:
    print("we don't have the same name")

#Exercise 9: Tall enough to ride a roller coaster
# Instructions
#Write code that will ask the user for their height in centimeters.
#If they are over 145 cm, print a message that states they are tall enough to ride.
#If they are not tall enough, print a message that says they need to grow some more to ride.
height = int(input("what is your height in cm?"))
if height > 145:
    print("you are tall enough to ride")
else:
    print("you need to grow some more to ride")

    
