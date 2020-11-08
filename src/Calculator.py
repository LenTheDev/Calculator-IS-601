# Static Methods

# Addition Static
def addition(a, b):
    return a + b

# Object Methods
class Calculator:
    result = 0

    def __init__(self):
        x = 2 + 2
        self.result = x;
        pass

    # Addition
    def add(self, a, b):
        self.result = a + b
        return addition(a, b)

