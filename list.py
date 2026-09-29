values = [1, 2, "John", 4, 5]
print(values[2])  # John
print(values[-1])  # 5
print(values[2:])  # ['John', 4, 5]
print(values[2:4])  # ['John', 4]
print(values[:2])  # [1, 2]
print(values[::2])  # [1, 'John', 5]
print(values[::-1])  # [5, 4, 'John', 2, 1]

# List methods
values.append(6)  # [1, 2, 'John', 4, 5, 6]
values.insert(0, 0)  # [0, 1, 2, 'John', 4, 5, 6]
values.pop()  # 6
print(values)  # [0, 1, 2, 4, 5]
values.remove('John')  # [0, 1, 2, 4, 5]
del values[0]
print(values)  # [1, 2, 4, 5]
values.clear()
print(values)  # []
