# List Section 
weather = ["Sunny", "Partly Cloudy", "Cloudy", "Rainy"]
print(weather)

print("--------------")

# Access by index
print(weather[2])

print("--------------")

# Replace value
weather.append("Humid")
print(weather)

print("--------------")

# Removing items
weather.remove("Sunny")
print(weather)

print("--------------")

# Length of list 
print(len(weather))

print("--------------")

# Dictionary Section

registration = {

    "name" : "Leticia",
    "age" : 29,
    "program" : "FSDI-Hybrid"
}

print(registration)
print(len(registration))

print("--------------")

# Accessing Value 
print(registration["name"])
print(len(registration))

print("--------------")

# Adding a New Key
registration["email"] = "leticiac@gmail.com" #not an actual email
print(registration)
print(len(registration))

print("--------------")

# Update Value
registration.update({
    "program" : "FSDI-Online"
})
print(registration)
print(len(registration))

print("--------------")

# Remove a Key 
registration.pop("age")
print(registration)
print(len(registration))

print("--------------")






