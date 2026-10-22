"""
Sets are UNORDERED, UNINDEXED, and have NO DUPLICATES 
Created with curly brackets {}
"""

fruits = {"apple", "banana", "cherry"}
print(fruits)

# Everytime you do a NEW run it won't be the same order 

# NO DUPLICATES ALLOWED - console will not display duplicates
fruits = {"apple", "banana", "apple"}
print(fruits)

# Remove duplicates from a list 
emails = ["a@.com", "b@.com", "a@.com", "a@.com", "c@.com", "a@.com"]
unique_emails = set(emails)
print(unique_emails)
print(list(unique_emails))


# Add Items - Only does this one at a time 
fruits.add("orange")
print(fruits)

# Adding Multiple Items 
fruits.update(["kiwi", "mango"])
print(fruits)

# Removing an Item - has to be the exact same as in the set 
fruits.remove("banana")
print(fruits)

# If you are not sure an item exsists, use discard() to avoid errors
fruits.discard("water")
print(fruits)

# SET OPERACTIONS (like in math)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2)) # Combine both sets (no duplicates)

print(set1.intersection(set2)) # Common Elements (value that both sets have)

print(set1.difference(set2)) # What unique in Set 1

print(set1.symmetric_difference(set2)) # Everything EXCEPT for whats shared


"""
MINI CHALLENGE: STUDY GROUPS
Two study groups are preparing for an exam.

1. Create two sets:
    - group_a = {"Leo", "Sam", "Alex", "Nina"}
    - group_b = {"Nina", "Jordan", "Sam", "Taylor"}
2. Print:
    - Students who are in BOTH groups (intersection)
    - Students who are in exactly ONE group (symmetric difference)
3. The exam sign-in sheet is a LIST with repeats (some people signed twice):
       signed_in = ["Leo", "Nina", "Leo", "Maya", "Nina", "Sam"]
   Use a set to print how many DIFFERENT students showed up.
4. Print which students from group_a did NOT show up.
5. Some people who showed up aren't in either group. Find who they are.
   (hint: combine the two groups first, then compare with who showed up)
6. If nobody is unregistered, print "Everyone belongs to a group!"
   Otherwise print "Unregistered students:" followed by their names.
"""

# 1. Create variable
group_a = {"Leo", "Sam", "Alex", "Nina"}
group_b = {"Nina", "Jordan", "Sam", "Taylor"}

# 2. Print BOTH groups
print(group_a.intersection(group_b))

# Print who is in ONE
print(group_a.symmetric_difference(group_b))

# 3. Sign In Sheet 
signed_in = ["Leo", "Nina", "Leo", "Maya", "Nina", "Sam"]
showed_up = set(signed_in) # set removes repeats 
print("Difference students who showed up:", len(showed_up))

# 4. Students who did NOT show up 
print("Group A students who did NOT show up: ", group_a.difference(showed_up))

# 5. Combine 
all_registered = group_a.union(group_b)
unregistered = showed_up.difference(all_registered)

if len(unregistered) == 0:
    print("Everyone belongs to a group!")
else:
    print("Unregistered students:", unregistered)












