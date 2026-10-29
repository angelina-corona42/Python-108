"""
A function is a block of code that only runs when it is called. 
We can pass data to a function (parameters), and they can run data

def function_name(parameters):
    # Code block (indented)
    # reform actions using the parameters
    return value # optional
"""

# Simple Function w/o Parameters 
def my_function():
    print("This is my function")

my_function() # Calling the function, you have to include ()

# Function with Parameters
# Parameters allows us to pass information into a function 

def print_full_name(fname , lname):
    print(f"The name is: {fname} {lname}")

print_full_name("Angie", "Corona") # Assign values in the function call

# Functions that RETURN values
# Instead of printing, functions can send back (return) data
def get_full_name(fname, lname):
    return f"{fname, lname}" # Sends back the full name as text

# Store the return value in a variable
full_name = get_full_name("Angie", "Corona")
print(full_name)

# Functions with default parameters 
# A default parameters means the function will use that value, 
# if no argument is provided when calling the function
def greet(name="Student"):
    print(f"Hello, {name}! Welcome to class.")

    greet() # Calling with no argument -> use the default

    greet("Angie") # Calling with argument -> overrides the default

# Passing a List into a Function
def print_items(items):
    for item in items:
        print("-", item)

print_items(["apple", "banana", "cherry"]) 

"""
MINI CHALLENGE: PASSWORD STRENGTH

Create a function called check_password().
1. The function should accept one parameter:
      - password
2. Inside the function:
      - If the password length is 8 or more:
            return "Strong Password"
      - If the password length is between 5 and 7:
            return "Medium Password"
      - Otherwise:
            return "Weak Password"
3. Ask the user to enter a password.
4. Call the function and store the returned result.
5. Print the result.
BONUS:
If the password contains an exclamation mark (!),
print "Special character detected!"
"""
def check_password(password):
    if len(password) >= 8:
        return "Strong Password"
    elif len(password) >= 5:
        return "Medium Password"
    else:
        return "Weak Password"


password = input("Enter a password: ")

result = check_password(password)

print(result)

if "!" in password:
    print("Special character detected!")