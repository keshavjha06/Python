temperature = 15
if temperature > 30:
    print("It's a hot day.")
    print("Drink water.")
elif temperature > 20:
    print("It's a nice day.")
elif temperature > 10:
    print("It's a bit cold.")
else:
    print("It's cold.")
print("Done")

#Ternary operator
age = 15
message = "Eligible" if age >= 18 else "Not eligible"
print(message)
