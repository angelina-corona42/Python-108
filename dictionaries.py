"""
Dictionaries store information using key-value pairs. Dictionaries use curly brackets {}.
"""

# BASIC DICTIONARY

student = {
    "name": "Leo",
    "age": 24,
    "major": "Computer Science"
}

print(student)

# ACCESS A VALUE - Dictionaries are accessed using keys.
print(student["name"])

# GET METHOD
print(student.get("major"))

# ADD A NEW KEY AND VALUE
student["graduation_year"] = 2025
print(student)

# CHANGE A VALUE
student["age"] = 30
print(student)

# REMOVE A KEY
student.pop("major")
print(student)

# CHECK IF A KEY EXISTS
if "name" in student:
    print("Name exists")

# NESTED DICTIONARY - A nested dictionary is a dictionary inside another dictionary.

students = {
    "student1": {
        "name": "Leo",
        "age": 20
    },

    "student2": {
        "name": "Alex",
        "age": 21
    }
}

print(students["student1"])

print(students["student2"]["name"])

# LIST OF DICTIONARIES
"""
A list of dictionaries is like a table: each dictionary is one row (one record).
This is the shape of a store catalog, an api response (JSON) and the documnts,
stored in the database like MongoDB
"""

products = [
    {
        "id": 1,
        "title": "Mouse",
        "price": 14.99
    },

    {
        "id": 2,
        "title": "Keyboard",
        "price": 30
    }
]

# Access a value inside the first dictionary.
print(products[0]["title"])

# LOOP THROUGH A LIST OF DICTIONARIES
for product in products:
    print(f"{product['title']}: ${product['price']}")

# ADD ANOTHER DICTIONARY
products.append({
    "id": 3,
    "title": "Monitor",
    "price": 120
})

print(products)

# LEN
print(len(products))

# UPDATE
student.update({
    "age": 19,
    "gpa": 3.8
})

print(student)

# TUPLE - Tuples use parentheses ().
grades = (90, 85, 88)
print(grades)

# SUM - Adds the numbers together.
print(sum(grades))

# LEN (Length) - Counts how many values are inside the tuple.
print(len(grades))


"""
MINI CHALLENGE: STUDENT REPORT CARD

You need to store and analyze a student's grades.
1. Create a dictionary called "report_card" with keys:
    -"name"
    - "subject"
    - "grades" (use a tuple with 3 numbers)

Example: {"name": "Leo", "subject": "Math", "grades": (90, 85, 88)}
2. Print the student's name and subject.
3. Calculate the average of the 3 grades (HINT: use sum() and len()).
4. Add a new key called "average" with the calculated result.
5. If the average is 90 or above → print "Excellent!"
    If between 70 and 89 → print "Good job!"
    Otherwise → print "Needs improvement!"
6. Remove the "subject" key and print the updated dictionary."""

# Complete mini challenge here:

# 1 & 2: Create dict / print name and subject  
report_card = {
    "name" : "Angelina", 
    "subject" : "Math", 
    "grades" : (95, 82, 75)
}
print(report_card["name"])
print(report_card["subject"])

# 3. Calc average
average_grade = sum(report_card["grades"]) / len(report_card["grades"])
print(average_grade)

# 4. Add a new key & value
report_card ["average"] = average_grade
print(report_card)

# 5. If section

if report_card["average"] >= 90:
    print("Excellent!")
elif report_card["average"] >= 80:
    print("Good job!")
else:
    print("Needs Improvement!")

