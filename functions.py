def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


# Arguments
greet("Keshav", "Jha")
greet("John", "Smith")

# Types of functions:
def greet(name):
    print(f"Hi {name}")

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Keshav")
print(message)
file = open("content.txt", "w")
file.write(message)
