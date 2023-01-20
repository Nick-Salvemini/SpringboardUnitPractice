# CLASS INHERITANCE
# pass the class being inherited (parent class) as the argument of the child class

from classes import Triangle

class ColoredTriangle(Triangle):
    def __init__(self, a, b, color):
        # call the constructor of the parent class, including the arguments, and then any additional arguments
        super().__init__(a,b)
        self.color = color

    def describe(self):
        msg = super().describe()
        return msg + f', and I am {self.color}'