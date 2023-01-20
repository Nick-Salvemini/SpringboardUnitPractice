from math import sqrt
from random import randint

class Triangle:
    '''
    A class used to represent and calculate a right triangle

    Attributes
    __________________
    a: int
        length of side a
    b: int
        length of side b
    '''

    # equivelent of JS constructor
    def __init__(self,a,b):
    # self needs to be called in init and all methods within the class
        self.a = a
        self.b = b

    def __repr__(self):
    # an instance method that will change what is shown when calling an instance of this class
        return f'Triangle(a={self.a} b={self.b})'

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    # dunder/special methods (methods with 2 underscore before and after)  are used to define behavior of a class
    
    @classmethod
    # this tells python that the method that follows will be a class method
    # instead of self, it takes the class as an argument, usually written as 'cls', which the '@classmethod decorator will automatically include
    def random(cls):
        '''
        Class method that generates and triangle with random side lengths
        '''
        return cls(randint(1,20), randint(1,20))
    
    def get_hypotenuse(self):
        '''
        calculate the hypotenuse (3rd side of right triangle)
        '''
        return sqrt(self.a ** 2 + self.b ** 2)

    def get_area(self):
        '''
        calculate the area of the right triangle
        '''
        return (self.a * self.b)/2

    def describe(self):
        '''
        gives a description of the triangle
        '''
        return f'I am a triangle with sides: {self.a} & {self.b}'

    # class methods don't operate on an instance of the class, but on the class itself. for example, a 'factory method', a method that creates an instance of the class for us

    