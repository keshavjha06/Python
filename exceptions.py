ItemsInCart = 0
# 2 items will be added to cart

if ItemsInCart != 2:
    # raise Exception("Cart should have 2 items")
    pass

assert ItemsInCart == 0

# try, catch

try:
    with open("filelog.txt", "r") as reader:
        reader.read()

except:
    print("It's reached here because there is failure in try block")


try:
    with open("test.txt", "r") as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("execution completed")

#exercise 1
def add_to_cart(items_to_add):
    global ItemsInCart

    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")
    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")

    ItemsInCart += items_to_add
    print(f"{items_to_add} items added. Total in cart: {ItemsInCart}")


try:
    add_to_cart(2)
    add_to_cart(-1)
except Exception as error:
    print(error)

#exercise 2
person = ("Rahul", 25, 5.9)
print(f"Age: {person[1]}")

try:
    person[0] = "Aman"
except TypeError as error:
    print(f"Error: {error} - Tuples are immutable.")
