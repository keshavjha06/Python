def increment(number, by):
    return number + by


print(increment(2, by=1))

# Default arguments


def increment(number, by=1):
    return number + by


print(increment(2, 6))

# xargs


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# keyword args:
# **arg
def getStudentMarks(**args):
    for key, value in args.items():
        print("%s == %s" % (key, value))

getStudentMarks(keshav=10, tom=20, peter=30)

getStudentMarks(key="apple", sellerName="Xeon")

#lambda functions:Anonymous function:

cube = lambda x: x*x*x

print(cube(4))

total = lambda marks: marks + 30

print(total(100))