# self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# constructor name should be __init_
# new keyword is not required when you create object


class Calculator:
    num = 100  # class variables

    # default constructor
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + self.num  # or Calculator.num


obj = Calculator(2, 3)  # syntax to create objects
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.Summation())

# exercise
class BasicCalculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def addition(self):
        return self.first_number + self.second_number

    def subtraction(self):
        return self.first_number - self.second_number

    def multiplication(self):
        return self.first_number * self.second_number

    def division(self):
        return self.first_number / self.second_number


basic_calculator = BasicCalculator(10, 5)
print(f"Addition: {basic_calculator.addition()}")
print(f"Subtraction: {basic_calculator.subtraction()}")
print(f"Multiplication: {basic_calculator.multiplication()}")
print(f"Division: {basic_calculator.division()}")


def CalculateAverage(num1, num2, num3):
    return (num1 + num2 + num3) / 3


average = CalculateAverage(10, 20, 30)
print(f"The average of 10, 20, and 30 is {average}")
