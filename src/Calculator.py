import math
# Static Methods For Each Calculation

# Addition Static
def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


# Subtraction Static
def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


# Multiplication Static
def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c


# Division Static
def division(a, b):
    a = float(a)
    b = float(b)
    c = round(b / a, 9)  # Second Parameter Rounds By (Decimal Places)
    return c


# Squared Number Static
def squared(a):
    a = int(a)
    b = a * a
    return b


# Square Root Static
def square_root(a):
    return round(math.sqrt(float(a)), 9)


# Object Methods
class Calculator:
    result = 0

    # Constructor
    def __init__(self):
        pass

    # Addition
    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    # Subtraction
    def subtraction(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    # Multiplication
    def multiplication(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    # Division
    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    # Squared Number
    def squared(self, a):
        self.result = squared(a)
        return self.result

    def square_root(self, a):
        self.result = square_root(a)
        return self.result
