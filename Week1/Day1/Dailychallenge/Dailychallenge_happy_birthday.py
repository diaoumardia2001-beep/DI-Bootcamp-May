#Instructions
#Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
#Display a little cake as seen below:
#The number of candles on the cake must correspond to the last digit of the person's age ; if they are 53 years old, add 3 candles.
#If they were born in a leap year, present two cakes !
from datetime import datetime

birthdate = input("enter your birthdate (DD/MM/YYYY): ")
day, month, year = map(int, birthdate.split("/"))

current_year = datetime.now().year
age = current_year - year

num_candles = age % 10
if num_candles == 0 and age > 0:
    num_candles = 10

candles = "i" * num_candles
top_candles = f"{candles:^11}"

print(f"\nHere is your cake for your {age} years old :\n")
print(f"   ___{top_candles}___")
print("      |:H:a:p:p:y:|")
print("    __|___________|__")
print("   |^^^^^^^^^^^^^^^^^|")
print("   |:B:i:r:t:h:d:a:y:|")
print("   |                 |")
print("   ~~~~~~~~~~~~~~~~~~~")
