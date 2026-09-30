def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


# Arguments
greet("Keshav", "Jha")
greet("John", "Smith")

# Types of functions:
# optional/default parameter:
def getCountryName(name="India"):
    print(name)

getCountryName()
getCountryName("UK")
getCountryName(100)

# pass a list to a function:
def getNames(list):
    for x in list:
        print(x)

names = ["Java", "Python", "DotNET", "Ruby"]
getNames(names)

# function with return
def sum(a, b):
    c = a + b
    return c

s1 = sum(10, 20)
print(s1)

def getCapitalName(countryName):
    if countryName == "India":
        return "New Delhi"
    elif countryName == "USA":
        return "Washington DC"

print(getCapitalName("India"))
print(getCapitalName("USA"))

def launchBrowser(browserName):
    if browserName == "chrome":
        print("launch google chrome")
    elif browserName == "firefox":
        print("launch firefox")
    else:
        print("no browser is defined")

launchBrowser("chrome")

# Recursion in Python:
def fact(num):
    if (num > 1):
        num = num * fact(num - 1)
    return num

print(fact(4))
print(fact(5))

#other types:
def login(username, password):
    print("login with %s and %s" % (username, password))

login("Keshav", "Pass@123")

def login(username, password):
    print(username, password)

login("keshav", "test123")

login(username = "keshavtest", password="test@123")
