10 > 3
print(10 > 3)
print(10 >= 3)
print(10 < 20)
print(10 == 20)
print(10 == "10")
print(10 != 20)

"bag" > "apple"
print("bag" > "apple")  # True because b > a
print("bag" == "Bag")  # False because b != B
print(ord("a"))  # 97
print(ord("A"))  # 65

# Logical operators
high_income = False
good_credit = True
student = False
if not student and (high_income or good_credit):
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# chaining comparison operators
age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")

#Exercise

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c") # c