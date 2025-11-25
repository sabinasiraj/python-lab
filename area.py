from graphics.RectFunctions import*
from graphics.CirFunctions import*
from graphics.DGraphics.SphereFunctions import*
from graphics.DGraphics.cuboidfunctions import*

l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
print("Rectangle Area =", RectArea(l, b))
print("Rectangle Perimeter =", RectPerimeter(l, b))

r = int(input("Enter radius of Circle: "))
print("Circle Area =", CirArea(r))
print("Circle Perimeter =", CirPerimeter(r))

r = int(input("Enter radius of Sphere: "))
print("Sphere Area =", SpArea(r))
print("Sphere Volume =", SpPerimeter(r))
l = int(input("Enter cuboid length: "))
b = int(input("Enter cuboid breadth: "))
h = int(input("Enter cuboid height: "))
print("Cuboid Area =", CubArea(l, b, h))
print("Cuboid Perimeter =",CubPerimeter(l, b, h))
