# Static Methods

# Addition Static
def addition(a, b):
    return a + b

# Subtraction Static
def subtraction(a, b):
    return a - b

# Object Methods
class Calculator:
    result = 0

    # Constructor
    def __init__(self):
        pass

    # Addition
    def add(self, a, b):
        self.result = a + b
        return self.result

    # Subtraction
    def subtraction(self, a, b):
        self.result = a - b
        return self.result

