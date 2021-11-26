# A function inside a class is called a 'method'
class Rectangle:
    def __init__(self, c, l, w):                                                # Arguments: self, color, length, width
        self.color  = c
        self.length = l
        self.width  = w
    def area(self):
        self.area = self.length * self.width
        return self.area
    def per(self):
        self.perimeter = (2*self.length) + (2*self.width)
        return self.perimeter
    def diagonal(self):
        self.diagonal = ( (self.width**2) + (self.length**2) )**(1/2)
        return self.diagonal
    def vol(self, h):
        self.height = h
        self.volume = self.length * self.width * self.height
        return self.volume

myRect1 = Rectangle('red', 2, 1)                                                # Rectangle 1
area1   = myRect1.area()
per1    = myRect1.per()
diag1   = myRect1.diagonal()
vol1    = myRect1.vol(5)
myRect2 = Rectangle('blue', 4, 3)                                               # Rectangle 2

print('myRect1 color        = ', myRect1.color)
print('myRect1 length       = ', myRect1.length)
print('myRect1 area         = ', area1)
print('myRect1 perimeter    = ', per1)
print('myRect1 diagonal     = ', diag1)
print('myRect1 volume       = ', vol1)


print('\nmyRect2 color        = ', myRect2.color)
print('myRect2 length       = ', myRect2.length)