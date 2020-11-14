#  Lab 5:  <Insert your name here>
#  Lab section: <insert 2 or 3>

# import the graphics package
from graphics import *


#####################################################################
# Part A:
#   Create/open a single graphics window:
#   1.  Its title is:  My Lab 5
#   2.  The window is 500 pixels wide and 250 pixels high
#   3.  The window's background is: tan
#
# All items created in the rest of the program should be placed in this window.

win = GraphWin("My Lab 5", 500, 250)

win.setBackground("tan")

#####################################################################
# Part B:
#   Create a green circle (with radius of 30 pixels),
#              centered at the point (125,125)

aCircle = Circle(Point(125,125), 30)
aCircle.setFill("green")

#####################################################################
# Part C:
#   Have the circle from Part B, draw itself in the window from Part A.


aCircle.draw(win)



#####################################################################
# Part D:
#   Draw a purple rectangle (height of 50 pixels, width of 20 pixels)
#           whose top-left corner is at point (50,10)

aRectangle = Rectangle(Point(50,10), Point(70,60))

aRectangle.setFill("purple")

aRectangle.draw(win)

#####################################################################
# Part E:
#   Draw a cyan triangle, whose vertices are at the points
#               (400,5), (495,245), and (305,200)

aPolygon = Polygon([Point(400,5), Point(495,245), Point(305,200)])

aPolygon.setFill("cyan")

aPolygon.draw(win)


#####################################################################
# Part F:
#   Create and draw 10 points, starting at (10,200),
#   with the x coordinates spaced 50 pixels apart,
#   all with y coordinate 200.
#   Use a for loop with range(something in here)

x=10
y=200
aPoint = Point(x, y)

for i in range (10,510,50):
    
    aPoint = Point(i, y)
    aPoint.draw(win)
    


#####################################################################
# Part G:
#   Instead of drawing the points in part F,
#   create and draw red circles of radius 30,
#   centered at each of the points from part F.

xa=10
ya=200
abPoint = Point(xa, ya)

for i in range (10,510,50):
    
    abPoint = Point(i, ya)
    abCircle = Circle(abPoint, 30)
    abCircle.setFill("red")


    abCircle.draw(win)


#####################################################################
# Part H;
#   Close the window.
win.getMouse() # pause for click in window
win.close()
