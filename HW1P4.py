import random

class Database:
    def __init__(self):
        self.shapes = []
        self.size = 0

    def sort(self):
        self.shapes.sort(key=lambda x: x.zIndex)

    def getShapes(self):
        return self.shapes

    def addShape(self, shape):
        self.shapes.append(shape)
        self.size += 1

    def printShapes(self):
        print("There are {} shapes in the database".format(self.size))

        for shape in self.shapes:
            shape.display()

class Shape:
    def __init__(self, zIndex, shapeType=None):
        self.shapeType = shapeType
        self.zIndex = zIndex

    def display(self):
        print(self.shapeType + " " + str(self.zIndex))

class Triangle(Shape):
    def __init__(self, zIndex):
        Shape.__init__(self, zIndex, 'Triangle')

class Square(Shape):
    def __init__(self, zIndex):
        Shape.__init__(self, zIndex, 'Square')

class Circle(Shape):
    def __init__(self, zIndex):
        Shape.__init__(self, zIndex, 'Circle')


database = Database()
for i in range(10):
    triangle = Triangle(random.randint(0, 1000))
    database.addShape(triangle)

for i in range(10):
    square = Square(random.randint(0, 1000))
    database.addShape(square)

for i in range(10):
    circle = Circle(random.randint(0, 1000))
    database.addShape(circle)

database.sort()
database.printShapes()

