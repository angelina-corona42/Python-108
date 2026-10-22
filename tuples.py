"""
TUPLES are IMMUTABLE (you can't change them after creation)
Created with round brackets ()
"""

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# Accessing Items 
print(my_tuple[0])
print(my_tuple[-1])

#Tuples can not be changed (Try it) 
temp_tuple = ("apple", "banana", "cherry")
temp_list = list(temp_tuple) # this is now a list to change value(s) of tuple
temp_list [0] = "kiwi"
temp_tuple = tuple(temp_list) # inverse of the above code to chage back to tuple


print(temp_list)
print(temp_tuple)

# Single Item Tuple - , is needed to make it a tuple rather than string
single = ("water",) 
print(type(single))

# type string
not_tuple = ("apple")
print(type(not_tuple))

# Joining, Slicing, Lopping 

more = ("date", "elderberry")
print(my_tuple + more) # + joins tuples into a NEW tuples 

print(more * 2) # * REPEATS the tuple

print(my_tuple[1: ]) # slicing works just like lists

for item in my_tuple: 
    print(item) # Prints each item on its own line


""" MINI CHALLENGE: THE TRAVEL BAG

You are packing for a trip! You have a tuple that stores the items you are taking.

1. Create a tuple called "travel_bag" with at least 5 items (e.g. "shirt", "toothbrush", etc.)
2. Print the SECOND and FOURTH items in your bag.
3. Check if "shoes" is in your travel bag — if it is, print "You're ready to walk!"
    otherwise, print "You forgot your shoes!"
4. Make a new tuple called "essentials" with 3 must-have items.
5. Combine both tuples into one called "final_bag" (hint: the + operator).
6. Print how many total items you now have using len().
7. Print the last item in your "final_bag".
"""

travel_bag = ("jeans", "shirt", "socks", "underwear", "hair-brush")

# 2. Printed 2nd and 4th item
print(travel_bag [1])
print(travel_bag [3])

# 3. Check if shoes 
if "shoes" in travel_bag:
    print("You're ready to walk!")
else:
    print("You forgot your shoes!")

# 4. New Tuple 
essentials = ("toothbrush", "toothpaste", "deodorant")

# 5. Combine Tuple
final_bag = (travel_bag + essentials)
print("Total items in bag: ", len(final_bag))

# 6. Print Last Item
print (final_bag [7])


