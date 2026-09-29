# for loops
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# for else
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x} , {y})")

# Iterable
# print(type(5))
# print(type(range(5)))

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)

# while loop
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# infinite loop

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
