# -*- coding: utf-8 -*-
"""basics01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1veoR3k2lRRkx5UrgywwKGCv63iEZYLi-

# Notes

gen

- double click to edit cell
- if possible, press ctrl / shift / alt + enter to run cells instead of clicking play button
  - for one thing keyboard shortcuts are just faster than constantly moving to the mouse and clicking but also sometimes the play button doesn't do what you expect it to do
    - ctrl + enter = run cell in place
    - shift + enter = run cell and move to next one (will create new CODE cell if next cell doesn't exist) 
      - ALSO USE THIS TO EXIT TEXT CELLS, can't do ctrl + enter to exit
    - alt + enter = run cell and insert new CODE cell immediately below - can go in between existing cells
- apparently python doesn't end lines in semicolons? wild
- single or double quotes for variables, doesn't matter. but if you start with a single quote you MUST end with a single quote, same with double
  - also colabs does that thing where it kinda autocompletes your typing for you in code (like it won't correct spelling, but if you hit a single quote it'll immediately enter the second closing quote for you. same with brackets and some tabbing stuff blah blah)


PUSHING TO GITHUB

- file > save copy in github
  - IF BRANCH DOESN'T EXIST, open in visual studio code
  - create new file, type whatever, name it readme.md (.md MUST BE LOWERCASE!)
  - save file
  - should show blue 1 on the left, click it, then push changes to github (include whatever message to indicate changes)
  - refresh github
  - hopefully colabs can now save copies to github!
  - if not idk troubleshoot with prof again


terminology
- EOL: end of line

---

---

# Practice
"""

import math

"""Create five variables"""

first_name = "MJ"
firstName = "AJ"
FirstName = "JJ"
FIRSTNAME = "PJ"
_firstname = "RJ"

print(first_name)
print(firstName)
print(FirstName)
print(FIRSTNAME)
print(_firstname)

print(first_name, firstName, FirstName, FIRSTNAME, _firstname) # Does Python automatically insert the spaces between the variables?
print(" ") # Aha so this inserts the line break because line 6 by itself didn't
print("hey")
print(" ")
print("hello", "again")
print("goodbye", " ", "again")
print("one" + "more" + " " + "test") # OHHHHHHHH using + collates strings, it's the comma that separates them and adds the space
print("last" + " one", "to make sure") # Excellent

"""Create ten variables"""

lastName = "Red" # I have zero brain to come up with a bunch of last names on the spot
LastName = "Orange"
last_name = "Yellow"
Last_Name = "Green"
LASTNAME = "Blue"
lastname = "Indigo"
lAsTnAmE = "Violet"
laastnaame = "Pink"
llastnname = "Black"
yeehaw = "White"

print(lastName)
print(LastName)
print(last_name)
print(Last_Name)
print(LASTNAME)
print(lastname)
print(lAsTnAmE)
print(laastnaame)
print(llastnname)
print(yeehaw)

num = 10

print(first_name)

"""- after running the code below I tried to print first_name again up here while editing it with a comment and it printed 90. so note that changes to a variable made later will hold for earlier code"""

first_name = 90 # Updating variable first_name

print(first_name) # Now it's printing the new value

"""---

---

# Data Types

Float
"""

num = 12.90 # Notice 0 gets omitted when printing, it's redundant
num

num1 = 12.398475938492563
num1

# Printing pi: import math library to get access
# Automatically stops at 15th decimal place so as not to run forever

math.pi

"""Boolean"""

game = True # True / False values capitalized in Python
playstation = False

type(num) # Prints data type

type(game)

type(math.pi)
type(playstation) # Huh. Does it only run the most recent (lowest) entry in the cell?

print(type(math.pi))
print(type(playstation))
print(playstation) # inch resting

"""List"""

listExample = ["hello", "world", "goodbye"] # SQUARE BRACKETS FOR LISTS!
listExample

print(listExample)

listExample
print(listExample) # So this just runs the recent one? Is it because it's redundant in this case? (Even though the type one from above isn't bc math.pi is a float...)

"""Create 10 lists, 10 booleans, 10 floats"""

list1 = [1, 2, 3] # BRACKETS
list2 = [4, 5, 6]
list3 = ["a", "b", "c"]           # Encase in quotes so they're strings, if just list4 = [a, b, c] those could be variables and in this case, are unassigned - might not run
list4 = ['d', 'e', 'f']           # Just do single quotes, prob faster in the long run (no shift)
list5 = ["g", "h", 'i', 10, game] # Can mix data types!
list6 = [list2, list3]            # Can I put a list in a list?
list7 = [3.4, num1, "yeehaw"]
list8 = ["monday", 'tuesday', 'wednesday', "thursday"]
list9 = ['friday', 'saturday', 'sunday']
list10 = []                       # Do we call this an empty list? 

bool1 = 0       # I think these can hold integers?
bool2 = 1
bool3 = True    # T/F capitalized for boolean values
bool4 = False
bool5 = True
bool6 = False
bool7 = 11
bool8 = 12
bool9 = 13.57   # What about decimals :0
bool10 = -6     # IIRC anything that isn't 0 is true so even if negative this would return True

float1 = 1.2
float2 = 2.3 
float3 = 3.456
float4 = 2452.9879235
float5 = 0.0
float6 = 0.0000000000001
float7 = 9.9999999999999
float8 = math.pi
float9 = 6.9    # Nice
float10 = 10.0

# Dictionary - this is just Python's name for an array
# CURLY BRACKETS

dictExample = {'key': 'value', 'key2': 'value2', 'key3': 'value3'}
dictExample

"""Create:
- dict1 = 10 foods
- dict2 = 10 names
- dict3 = 5 sports players 
"""

dict1 = {
    'fruit': 'apple',
    'vegetable': 'carrot',
    'tuber': 'potato',
    'legume': 'pinto',
    'yam': 'ube',
    'soup': 'french onion',
    'meat': 'beef',
    'dairy': 'milk',
    'dessert': 'cake',
    'granola': 'bar' # lol
}

dict2 = { # Can assign a list to the same key to save time
    'names': [
        'Anna', 
        'Burton', 
        'Chester', 
        'Diana', 
        'Elmer', 
        'Fred', 
        'George', 
        'Heather', 
        'Irene', 
        'Julia'
    ]
} 

dict3 = {
    'point guard': 'Elfrid Payton',
    'shooting guard': 'Austin Rivers',
    'small forward': 'RJ Barrett',
    'power forward': 'Obi Toppin',
    'center': 'Mitchell Robinson'
}

print(dict1)
print(dict2)
print(dict3)