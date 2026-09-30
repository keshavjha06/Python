age = 25
height = 5.9
favorite_color = "blue"
print(f"Age: {age} | Type: {type(age)}")
print(f"Height: {height} | Type: {type(height)}")
print(f"Favorite Color: {favorite_color} | Type: {type(favorite_color)}")

# List
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"First fruit: {fruits[0]}")  # apple
print(f"Last fruit: {fruits[-1]}")  # elderberry
print(f"Fruits from index 1 to 2: {fruits[1:3]}")  # ['banana', 'cherry']

# Tuple
person = ("Keshav", 25, 5.9)
print("Age:", person[1])  # 25

# Dictionary
car = {
    "make": "Toyota",
    "model": "Camry",
    "year": 2020,
    "color": "Blue"
}
print("Car model:", car["model"])  # Camry
car["owner"] = "Keshav" # {'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'color': 'Blue', 'owner': 'Keshav'}
print("Updated car dictionary:", car)

# if-else
greeting = "Hello"
if greeting == "Hello":
    print("Hello there!")
    print("How can I assist you today?")
else:
    print("Greetings!")
print("Program has completed.")

b = 15
if b > 10:
    print("Number is greater than 10")
else:
    print("Number is 10 or less")
print("Comparison code is completed.")

#for loop
numbers = [1, 4, 7, 10]
for i in numbers:
    print(i * 3)

#if-elif-else
user = 10
user = 15
if 5 <= user <= 11:
    print("Good Morning")
elif 12 <= user <= 17:
    print("Good Afternoon")
elif 18 <= user <= 21:
    print("Good Evening")
else:
    print("Good Night")
print("Greeting code has completed.")


