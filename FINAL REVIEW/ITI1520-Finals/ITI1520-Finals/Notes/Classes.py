#Mershab
#Class Structure

class Point:
    #Every funtion has an '__init__' function
    #This one has the x and y coordinates, and the '=0' part means that if the user does not input an x and y coordinate its default is 0
    def __init__(self,xcoord=0,ycoord=0):
        self.x = xcoord
        self.y = ycoord
    #Creating a string representation of the point
    def __repr__(self):
        return "Point[ " + self.x + " , " + self.y + "]"
    #Modifying pythons '==' operation to work with the new point class
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    #Move function changes the x and y coordinates by adding the step value
    def move(self,xstep,ystep):
        self.x += xstep
        self.y += ystep

#Car class that has a location (Point) and a color (String)
class Car:
    def __init__(self, point=Point(0,0),color="Black"):
        self.location = point
        self.color = color

    #Move up, down, left, right functions use the Point.move() function to change the xa dn y coordinates appropriately
    def MoveUp(self):
        self.location.move(0,1)
    def MoveDown(self):
        self.location.move(0,-1)
    def MoveRight(self):
        self.location.move(1,0)
    def MoveLeft(self):
        self.location.move(-1,0)