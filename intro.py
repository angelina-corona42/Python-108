#Shortcut to run the code in the terminal is click on the play button in the top right corner

print("Hello World!") #Needs to have quotes around the string to print it correctly in the terminal

print(2) #Print a single number

print(5+3) #Prints the result of a simple addition operation

print(True) #Prints the boolean value True, for boolean values, the first letter must be capitalized

""" This is a multi-line comment, it can be used to write longer explanations or notes about the code. It starts and ends with three double quotes."""

# Creating a variable = value

name = "Angelina"
age = 25
print(name, age)

# Concatination (putting things together)
# You can not add strings and numbers together
# print("Hello my name is " + name + " and my age is " + age) 

print("Hello my name is " + name + " and my age is " + str(age)) #str converts to string 

#Mini Challenge 
"""Write a brief story using 5 variables and print in terminal
    Use different data types (str, int,...)
    Use concatinate to create a story"""

name = "Angie"
age = 26
weather = "sunny"
dog = "Koda"
treats = 5



"""print("My name is " + name + ". I am " + str(age) + ". I was thiniking about walking my dog " + dog + "and it is "
    
    
    + str(age) + ". I was thinking about walking my dog " + dog + " and it is " + weather + " outside but I only have " + str(treats) "treats")"""


place = "Disneyland"
activity = "rollercoaster"
members = 3


# F-STRING: always start with f""
print(f"The last time I went to {place}, I had a great time {activity} with {members} of my friends.")

# Multiline f format: f""" """ f''' '''
print(f"""The last time I went to {place}, 
            I had a great 
        time {activity} with {members}
                                    of my friends.""")

# Type Function: type()
# returns class type of variable 
print(type(name))
print(type(age))
print(type(True))

# Input Function: input() empty variable that gets updated by user
# Lets the user interact with the terminal 

user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# input() always returns a string 
print(type(input("Enter your name: ")))

#Ex: converting input to in 
new_age = int(input("Enter your age: "))
print(age + new_age)

'''
Pizza Calculator

Ask how many slices of pizza and how many people. (2 user inputs)
Use math operators to calculate slices per person. (divide the inputs)
Show the result with an f-string. 
'''

slices = int(input("Enter amount of slices: "))
people = int(input("Enter amount of people: "))
slice_per_person = slice / people
print(f'''{slices} + {people} + {slice_per_person}''')