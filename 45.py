#shapeCalculator.py
from math import pi

def rectArea(length, width):
    area=length * width
    return area

def circleArea(radius):
    area=pi*radius*radius
    return area

def welcome():
    print("Welcome to the shape calculator!")
    name=input("What is your name? ")
    return name

def askDimension(dimension):
    value = float(input("what is the " + dimension +"? "))
    return value

def main():
    name = welcome()
    print(name+", ", end="")
    x = askDimension("length")  #enter 4
    y = askDimension("width")   #enter 3

    print("The area of the rectangle is " + str(rectArea(x,y)))
    
    rad = askDimension("radius")   #enter 10
    a= circleArea(rad)
    print("The area of the circle is {0:0.5} sq. cm.".format(a))
    
main()
