# A list stores multiple items inside one variable.
# Lists use square brackets [].


# SIMPLE LIST 

fruits = ["apple", "banana", "cherry"]
print(fruits)

# INDEXING 
# Index positions start at 0.

print(fruits[0])
print(fruits[1])
print(fruits[2])

# NEGATIVE INDEXING 
# Negative indexing counts backward from the end.
# -1 means the last item.

print(fruits[-1])
print(fruits[-2])

# SLICING

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Start at index 2 and stop before index 5
print(numbers[2:5])

# Start at the beginning and stop before index 4
print(numbers[:4])

# Start at index 6 and go to the end
print(numbers[6:])

# Get the last 3 items
print(numbers[-3:])

# Skip every other item
print(numbers[::2])


# CHANGE AN ITEM 

fruits[1] = "mango"
print(fruits)


# APPEND: Adds one item to the end of the list.

fruits.append("orange")
print(fruits)



# INSERT: Adds an item at a specific index.

fruits.insert(1, "kiwi")
print(fruits)


# EXTEND: Adds multiple items to a list.

fruits.extend(["grape", "pear"])
print(fruits)


# REMOVE: Removes an item by value.

fruits.remove("apple")
print(fruits)


# POP: Removes an item by index.
# If no index is given, it removes the last item.

fruits.pop()
print(fruits)


# Example with an index:
# fruits.pop(0)


# CLEAR: Removes everything from the list.
# fruits.clear()


# FOR LOOP: Goes through each item in the list.
for fruit in fruits:
    print(fruit)


# LEN (Length) Tells us how many items are in the list.
print(len(fruits))


# COUNT: Counts how many times a value appears.

numbers = [4, 2, 6, 1, 7, 9, 2]
print(numbers.count(2))


# INDEX: Finds the index position of a value.

print(numbers.index(1))

# SORT: Sorts the list.

numbers.sort()
print(numbers)

#Sort in reverse order.

numbers.sort(reverse=True)
print(numbers)

# REVERSE: Reverses the current order.

numbers.reverse()
print(numbers)

# CHECK IF AN ITEM EXISTS

if "mango" in fruits:
    print("Mango is in the list")


# ---- GROCERY LIST MINI CHALLENGE: ----
""" You're building a grocery list app.

1. Create a list called "groceries" with at least 5 items.
2. Print the first and last item using indexing.
3. Use slicing to print just the first 3 items.
4. Add "eggs" to the end of the list using append().
5. Insert "milk" at the very beginning of the list.
6. Remove one item using remove().
7. Check if "bread" is in the list — print a message either way.
8. Sort the list alphabetically and print it.
9. Print how many items are in the final list.
"""

# Complete mini challenge here:

# 1. Create List 
groceries = ["Eggs", "Bread", "Rice", "Vegtables", "Milk"]

# 2. Print 1st Item 
print(groceries[0])

# 3. Slice (1st three items)
print(groceries[0:3])

# 4. Add Item 
groceries.append("Water")
print(groceries)

# 5. Insert Item 
groceries.insert(0, "Milk")
print(groceries)

# 6. Remove Item 
groceries.remove("Milk")
print(groceries)

# 7. Check if "bread" is on list
if "Bread" in groceries:
    print("Already added")
else:
    print("Not added")

# 8. Sort alphabetically
groceries.sort()
print(groceries)

# 9. How many items
print(len(groceries))