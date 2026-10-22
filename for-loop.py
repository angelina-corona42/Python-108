"""
A for loop is a Python is a control structure that lets you repeat a block, of code for each item in a sequence. 

for new_variable in sequence:
    # code block run for each item in the sequence
"""

fruits = ["apple", "banana", "cherry"]
for fruits in fruits: # for each fruit in the list fruits 
    print(fruits)

print ("----------------------") 

# Loop through a string 
for letter in "Hello":
    print(letter) # prints out every letter 

print ("----------------------") 

# range() function generates a sequence of #s (ONLY NUMBERS)
# S = Start , E = End , ST = Step 

for x in range(5): # counting the index 
    print(x)

print ("----------------------") 

# START and END range()
#              S  E
for x in range(2, 6): 
    print(x)

print ("----------------------") 

# STEP (Skips Numbers)
#                     ST
for x in range(0, 10, 2): #Skips it by 2 due to the order (S, E, ST)
    print(x)

print ("----------------------") 

# ELSE in for loops 
# Do not use inside the for loop
for x in range(3):
    print(x)
else:
    print("loop done")

# Else is most useful w/ break:
for number in [3, 2, 7, 9]:
    if number % 2 == 0:
        print("Found an even number")
        break # Stops loop when there is a specific condition that is met (Only specific to loops) 
else:
    print("No even numbers found")

print ("----------------------") 

# BREAK and CONTINUE (Only specific to for loops)
for x in range(20):
    if x == 5:
        continue # skip over 5 
    if x == 8:
        break    # stops loop at index 8
    print(x)

print ("----------------------") 

"""
MINI CHALLENGE: Multiplication Table

1. Ask the user to enter a number and store it in a variable called num.
2. Use a for loop with range(1, 11) to repeat 10 times (from 1 to 10).
3. Inside the loop, multiply num by the current loop value (i).
"""

num = int(input("Enter a number: "))

for i in range(1, 11): # this allows it to repeat 10x
    print(f"{num} X {i} = {num * i}")
