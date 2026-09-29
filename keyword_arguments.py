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
