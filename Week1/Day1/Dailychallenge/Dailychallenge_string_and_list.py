#Challenge 1
#Ask the user for a number and a length.
#Create a program that prints a list of multiples of the number until the list length reaches length.
#Examples
#number: 7 - length 5 ➞ [7, 14, 21, 28, 35]
#number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
#number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

number = int(input("enter a number:"))
length = int(input("enter a lenght:"))
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)
print(multiples)


#Challenge 2
#Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
#Examples
#user's word : "ppoeemm" ➞ "poem"
#user's word : "wiiiinnnnd" ➞ "wind"
#user's word : "ttiiitllleeee" ➞ "title"
#user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"


user_word = input("enter a word: ")
new_word = ""
for char in user_word:
    if not new_word or char != new_word[-1]:
        new_word += char
print(new_word)