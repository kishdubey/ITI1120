class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle(Point):

    def __init__(self, pointL, pointR, color):

        self.pointL = pointL
        self.pointR = pointR
        self.color = color

    def get_bottom_left(self):
        '''
        ()->Point Object
        The function returns the point object with the bottom-left coordinates 
        '''
        return self.pointL

    def get_top_right(self):
        '''
        ()->Point Object
        The function returns the point object with the top-right coordinates
        '''
        return self.pointR

    def get_color(self):
        '''
        ()->String
        The function returns the color of the rectangle
        '''
        return self.color

    def reset_color(self, color):
        '''
        (String)->None
        The function sets the color of the rectangle as the one given
        '''
        self.color = color

    def get_perimeter(self):
        '''
        ()->Integer
        The function returns the perimeter of the rectangle
        '''
        return 2*(self.pointR.get()[0] - self.pointL.get()[0]) + 2*(self.pointR.get()[1] - self.pointL.get()[1])

    def get_area(self):
        '''
        ()->Number
        The function returns the area of the rectangle
        '''
        return (self.pointR.get()[0] - self.pointL.get()[0]) * (self.pointR.get()[1] - self.pointL.get()[1])

    def move(self, dx, dy):
        '''
        (Number, Number)->None
        THe function modifies the bottom-left and top-right point objects of the rectangle object by the dx and dy given.
        '''
        self.pointL.move(dx, dy)
        self.pointR.move(dx, dy)
    
    def intersects(self, other):
        '''
        (Rectangle)->Boolean
        The function returns True if the Rectangle objects have atleast one point in common, and False otherwise.
        '''

        xls = self.pointL.get()[0]
        yls = self.pointL.get()[1]

        xrs = self.pointR.get()[0]
        yrs = self.pointR.get()[1]


        xlo = other.pointL.get()[0]
        ylo = other.pointL.get()[1]

        xro = other.pointR.get()[0]
        yro = other.pointR.get()[1]


        if yrs<ylo or yro<yls:
            return False
        if xrs<xlo or xro<xls:
            return False
        return True
    
    def contains(self, x, y):
        '''
        (Number, Number)->Boolean
        The function returns True if the coordiante is inside or on the boundary of the Rectangle, and False otherwise. 
        '''
        if(x<=self.pointR.get()[0] and x>=self.pointL.get()[0]) and (y<=self.pointR.get()[0] and y>=self.pointL.get()[1]):
            return True
        return False

    def __repr__(self):
        '''
        ()->String
        The function returns the way the Rectangle Object is represented
        '''
        return "Rectangle(" + self.pointL.__repr__() + ", "+self.pointR.__repr__()+", '"+self.color+"')"

    def __eq__(self, other):
        '''
        (Rectangle)->Boolean
        The function returns True if the two Rectangle objets' values of top-right point, bottom-left point and color are the same, and False otherwise.
        '''
        if self.pointL == other.pointL and self.pointR == other.pointR and self.color == other.color:
            return True
        else:
            return False

    def __str__(self):
        '''
        ()->String
        The function returns a formatted display for the Rectangle 
        '''
        return "I am a "+self.color+" rectange with bottom left corner at "+str(self.pointL.get())+" and top-right corner at "+str(self.pointR.get())
    
class Canvas:

    def __init__(self):
        self.rec = []

    def add_one_rectangle(self, rect):
        '''
        (Rectangle)->None
        '''
        self.rec.append(rect)

    def total_perimeter(self):
        '''
        ()->Number
        The function returns the total perimeter of the rectangles in the canvas object
        '''
        p = 0
        for rectangle in self.rec:
            p+=rectangle.get_perimeter()

        return p

    def min_enclosing_rectangle(self):
        '''
        ()->Rectangle
        '''
        minx = self.rec[0].get_bottom_left().get()[0]
        miny = self.rec[0].get_bottom_left().get()[1]
        
        maxx = self.rec[0].get_top_right().get()[0]
        maxy = self.rec[0].get_top_right().get()[1]

        for rectangle in self.rec:
            r = rectangle.pointR.get()
            l = rectangle.pointL.get()

            if r[0]>maxx:
                maxx = r[0]
            if r[1]>maxy:
                maxy = r[1]
            if l[0]<minx:
                minx=l[0]
            if l[1]<miny:
                miny = l[1]
                
        return Rectangle(Point(minx, miny), Point(maxx, maxy), "red")

    def common_point(self):
        '''
        ()->Boolean
        The function returns True if thre is a retangle that has a common point with every rectangle, and False otherwise
        '''
        for a in range(len(self.rec)-1):
            for b in range(a+1, len(self.rec)):
                if self.rec[a].intersects(self.rec[b]) == False:
                    return False
        return True

    def count_same_color(self, color):
        '''
        (String)->Integer
        The function returns the number of rectangles with the same color as the one given
        '''
        counter = 0
        for item in self.rec:
            if item.get_color() == color:
                counter+=1

        return counter
    def __repr__(self):
        '''
        ()->String
        THe function returns a nicely formatted string message of the convas object
        '''
        l = []
        for i in self.rec:
            l.append(i.__repr__())
        return 'Canvas(' + str(self.rec) + ')' +str(l)

    def __len__(self):
        '''
        ()->Integer
        The function returns the length of the canvas object list of rectangles
        '''
        return len(self.rec)
