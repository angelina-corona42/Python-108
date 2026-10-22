# If statements allow Python to make decisions
# depending on whether a condition is True or False.

# ----- BASIC IF STATEMENT ------

x = 10

if x > 0:
    print("X is positive")

# ---- IF / ELSE IF / ELSE -----

if x > 0:
    print("X is positive")
elif x == 0:
    print("X is zero")
else:
    print("X is negative")


# ---- COMPARISON OPERATORS ----

# >   greater than
# <   less than
# >=  greater than or equal to
# <=  less than or equal to
# ==  equal to
# !=  not equal to


# ---- SHORTHAND IF -----

if x > 5:
    print("X is greater than 5")


# ----- MODULUS ------
# % gives the remainder after division

if x % 2 == 0:
    print("X is even")
else:
    print("X is odd")


# ----- NESTED IF -----
# A nested if statement is an if statement inside another if statement.

if x > 0:
    if x < 20:
        print("X is positive and less than 20")



# ----- AND ------
# Both conditions must be True.

age = 20

if age >= 18 and age <= 20:
    print("Age is between 18 and 20")


# ---- OR ----
# Only one condition needs to be True.

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It is the weekend")



# ----- CLUB MINI CHALLENGE: ------
""" Ask the user to enter their age and store it in a variable called age. Ask the user if they have a valid ID.(The user should enter "yes" or "no".) Store the answer in a variable called has_id.
            Determine admission rules:
                If age is 21 or older AND has_id is "yes":
                    print "Access Granted"
                If age is 21 or older BUT has_id is "no":
                    print "Access Denied - ID Required"
                If age is between 18 and 20 inclusive:
                    print "Access Limited"
            Otherwise:
                print "Access Denied - Too Young"
        Create a variable called can_enter:
            Set it to True only if the user is 21 or older AND has_id is "yes".
        Otherwise set it to False.
BONUS:
 If can_enter is True:
     print "Welcome inside!"
 Otherwise:
     print "Please see the front desk."
EXTRA BONUS:
 If the user enters a negative age,
 print "Invalid age entered."
"""
# Complete mini challenge here:



