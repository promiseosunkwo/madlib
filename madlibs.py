# madlib is a game of adding strings or concatination of string

youtuber = "Promise"

# Diffrent ways of concatination
# print("my name is " + youtuber)
# print("my name is {}".format(youtuber))
# print(f"my name is {youtuber}")

name = input("What is your name? ")
age = input("How old are you? ")
home = input("Where do you live? ")
food = input("What is your favourite food? ")
drink = input("What is your favourite drink? ")

madblibs = f"My name is {name}! I am {age} years old. I live in {home} and i love \
{food} and use {drink} to wash it down!"

print(madblibs)