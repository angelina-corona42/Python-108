"""
Operators are like "symbols" or "shortcuts" that tell the computer,
to do something with values (numbers, text, ect...).
They are used to preform oerations on variables and values

"""

# ARITHMRTIC OPERATOR - used with numeric values to preform basic math 
x = 1
y = 2
res = 0

res = x + y
print(res)

res = x - y
print(res)

res = x * y
print(res)

res = x / y
print(res)

res = x % y #MODDULUS
print(res)

res = x ** y 
print(res)

res = x // y #FLOOR DIVISION
print(res)

# ASSIGNMENT OPERATOR - used to assign values to variables
# = means "put this value inside the (variable)"
# shourcuts: +=, -=, *=, /=

x = 5
x += 5 # x = x + 5
x -= 3 
x *= 3
x /= 3
print(x)

# COMPARISON OPERATOR: used to compare two values (same as if else)
# == (equal to), != (Not equal to), < > (Less than or Greater than), <= >= (Less/Greater/Equal to)

# LOGICAL OPERATOR - used to combine conditional statements (used with booleans)
# and - both must be TRUE 
# or - one must be TRUE 
# not - flips TRUE to FALSE 

x = 3 
y = 10
z = 10

print(x == y and y == z) # False, because both arent True 
print (x == y or y == z) # True, because one is TRUE 
print (not x == y)       # True, because x != to y 

# IDENTITY OPERATOR - used to compare the objects, not if they are equal to, 
# but if they are actually the same object with the same memory location 
# is - checks if two things are the exact same object in memory 
# is not - checks if they are NOT the same object in memory 

x = 3 
y = 3 

print( x is y)
print(x is not y)


# MEMBERSHIP OPERATOR - used to test a sequence is presented in an object 
# in - checks if something is in a sequence is presented in an object 
# not in - checks if something is NOT in a sequence 

x = [1, 2, 3, 4, 5] # This is a list 

print(4 in x)       # True becasue 4 is in the list
print(9 not in x)   # True because 9 is not in list 





