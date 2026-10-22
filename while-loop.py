"""
A while lopp repeats a block of code as long as a condition is TRUE
Be careful - if the condition never becomes FALSE, you'll get an INFINATE LOOP!
(If you are in a inf loo, press CTRL + C in the terminal)
Can use any conditions you want

while condition:
    # code block runs as long as the condition is TRUE
"""

# INFINITE LOOP
count = 1

while count <= 5:
    print("Count is", count)
    count += 1 # Adds one to itself which allows the condition to become FALSE

print ("----------------------") 

# Using break to STOP the loop when the condition is met 
number = 0 

while True: # Forcing infinite loop 
    print(number)
    number += 1 
    if number == 5:
        break

print ("----------------------") 

# Using CONTINUE to skip an iteration
count = 0 
while count < 5:
    count += 1
    if count == 3:
        continue # skips 3 
    print(count)
else:
    print("Loop finish")

print ("----------------------") 

# While loops LISTS 
tasks = ["Dishes", "Homework", "Walk dog"]

while tasks: 
    current = tasks.pop() #.pop removes and gives back the LAST item
    print("Doing: ", current)

print ("----------------------") 

# HADLING BAD INPUT (try / except) - they need to be together
# int("abc") crashes the program with ValueError
# try / except lets us CATCH the error and keep running the loop

while True:
    answer = input("Enter a whole number: ")
    try: 
        number = int(answer) # if this line crashes, Python jumps to "except"
        break 
    except ValueError:
        print("That is not a whole number, try again")

print(f"Thanks! You entered {number}")

"""
MINI CHALLENGE: Password Gate

# 1. Ask the user to enter a password
# 2. Check if it's correct (password: "secret123")
# 3. If it's wrong, print "Wrong! Try again." and ask again
# 4. When they enter the correct password, print "Access granted!"
# Solution:
password = ""                        # Start empty
while password != "secret123":       # Keep looping while password is wrong
    password = input("Enter password: ")
    if password != "secret123":      # If wrong
        print("Wrong! Try again.")
# Once they finally type "secret123", the while condition (password != "secret123") becomes false, so the loop stops.
print("Access granted!")
"""

password = ""                        # Start empty
while password != "secret123":       # Keep looping while password is wrong
    password = input("Enter password: ")
    if password != "secret123":      # If wrong
        print("Wrong! Try again.")
# Once they finally type "secret123", the while condition (password != "secret123") becomes false, so the loop stops.
print("Access granted!")



    