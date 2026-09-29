# Tuple is a collection of immutable objects
numbers = (1, 2, 3, 4, 5)
print(numbers[0]) # 1
print(numbers[-1]) # 5
print(numbers[2:4]) # (3, 4)
print(numbers[:2]) # (1, 2)
print(numbers[::2]) # (1, 3, 5)
print(numbers[::-1]) # (5, 4, 3, 2, 1)

# Tuple methods
print(numbers.count(1)) # 1 (number of occurrences of 1)
print(numbers.index(3)) # 2 (index of the first occurrence of 3)