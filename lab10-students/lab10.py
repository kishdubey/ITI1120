import math

class Point:
    'class that represents a point in the plane'

## exectuting Point(2,3)
## 1. creates an object of type point
## 2. calls an objects __init__ method
## 3. produces an object's memory address

## Assigning to a new variable using dot operator
## CREATES THAT VARIABLE INSIDE OF THE OBJECT

## Variables INSIDE of an object are called INSTANCE variables

## __init__ is method that is called to initialize the object (create it and initialize its variables)
## the first parameter of method is usually called self
## self refers to the object that is being initialized


#    constructor
#    notice two underscores
    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point, float, float) -> None
        >>> p=Point(2,3)
        >>> p.x
        >>> 2
        >>> p.y
        >>> 3

        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,float)->None
        set x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,float)->None
        set y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        return a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,float,float)->None
        change the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point('+str(self.x)+','+str(self.y)+')'

    def distance(self, other):
        return math.sqrt(pow(other.x - self.x,2) + pow(other.y - self.y,2))

    def up(self):
        #self.move(0,1)
        Point.move(self, 0, 1)

    def down(self):
        Point.move(self, 0, -1)

    def left(self):
        Point.move(self, -1, 0)

    def right(self):
        Point.move(self, 1, 0)
class Animal:
    'represents an animal'

    def __init__(self, species='animal', language='make sounds', age="0"):
        self.spec = species
        self.lang = language
        self.age = age

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a', self.spec,'and I', self.lang)

    def getAge(self):
        return self.age
    


class Bird(Animal): # class Bird inherits all atributes (data and method) from class Animal 
    'represents a bird'

    def speak(self):
        'prints bird sounds'
        print(self.language * 3)



class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit    

    def __repr__(self):
        'return formal representation'
        return 'Card('+self.rank+','+self.suit+')'

    def __eq__(self, other):
        'self == other if rank and suit are the same'
        return self.rank == other.rank and self.suit == other.suit

    def __gt__(self, other):
        return self.rank>other.rank

    def __ge__(self, other):
        return self.rank>=other.rank

    def __lt__(self, other):
        return self.rank<other.rank

    def __le__(self, other):
        return self.rank<=other.rank



class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = []          # deck is initially empty

        for suit in Deck.suits: # suits and ranks are Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank,suit))

    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        random.shuffle(self.deck)


    def __len__(self):
        'returns size of deck'
        return len(self.deck)

    def __repr__(self):
        'returns canonical string representation'
        return 'Deck('+str(self.deck)+')'

    def __eq__(self, other):
        '''returns True if decks have the same cards
           in the same order'''
        return self.deck == other.deck

class BankAccount:
    def __init__(self, balance=0):
        self.bal = balance

    def withdraw(self, amount):
        self.bal-=amount

    def deposit(self, amount):
        self.bal+=amount

    def balance(self):
        return self.bal

    def __repr__(self):
        return str(self.bal)

class PingPong:
    def __init__(self, p="PONG"):
        self.p = p
        
    def next(self):
        if self.p == "PING":
            self.p = "PONG"
            print(self.p)
        else:
            self.p="PING"
            print(self.p)

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
        
    def __eq__(self, other):
        return self.items == other.items

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return "Queue("+str(self.items)+")"

class Vector(Point):
    def __add__(self, other):
        self.x = self.x+other.x
        self.y = self.y+other.y
        return self
    def __mul__(self, other):
        return self.x*other.x + self.y*other.y
    def __repr__(self):
        return "Vector("+str(self.x)+","+str(self.y)+")"

class Marsupial:
    def __init__(self, color):
         self.col = color
         self.pouch = []

    def put_in_pouch(self, val):
        self.pouch.append(val)

    def pouch_contents(self):
        return self.pouch

    def __repr__(self):
        return "I am a "+self.col+" Marsupial"


class Kangaroo(Marsupial):
    def __init__(self, color, x, y):
        self.col = color
        self.pouch = []
        self.x = x
        self.y = y

    def jump(self, dx, dy):
        self.x+=dx
        self.y+=dy

    def __str__(self):
        return "I am a "+self.col+" Kangaroo located at coordinates("+str(self.x)+","+str(self.y)+")"

class Points(Point):
    def __init__(self, l=[]):
        self.l = l

    def add(self, x, y):
        self.l.append(Point(x, y))

    def left_most_point(self):
        minx = self.l[0].x
        miny = self.l[0].y
        for a in self.l:
            if a.x<minx:
                minx = a.x
                miny = a.y
            elif a.x == minx:
                if a.y<miny:
                    minx = a.x
                    miny = a.y

        a = Point(minx, miny)
        return a

    def __len__(self):
        return len(self.l)

    def __repr__(self):
        return str(self.l)

    

    

    

    
         
    
        
    
    
