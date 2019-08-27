import math
class Shape:

    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Square(Shape):

    def __init__(self, length = 0):
        self.length = length
        Shape.__init__(self)
    
    def area(self):
        return self.length ** 2
    
    def perimeter(self):
        return self.length * 4

    def __str__(self):
        print ('This is a Square class')
class Circle(Shape):

    def __init__(self,radius = 0):
        self.radius = radius
        Shape.__init__(self)

    def area(self):
        return math.pi*(self.radius**2)

    def perimeter(self):
        return 2*math.pi*self.radius
    
    def __str__(self):
        print ('This is a Circle class')


class Text:

class SavedText:


if __name__ == "__main__":
    new_square = Square(5)
    new_square.__str__()
    print('perimeter:',new_square.perimeter())
    print('area:',new_square.area())

    new_circle = Circle(8)
    new_circle.__str__()
    print('perimeter:',new_circle.perimeter())
    print('area:',new_circle.area())