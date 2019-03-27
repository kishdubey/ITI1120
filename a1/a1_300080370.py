#Family name: Kish Dubey
# Student number:  300080370
# Course: IT1 1120 
# Assignment Number 1
import math
import turtle
'''
References: I used "https://kite.com/python/examples/4653/datetime-round-datetime-to-any-time-interval-in-seconds" for learning how to round to the nearest 5 minutes  in python.
'''
###################################################################
# Question 1
def pythagorean_pair(a,b):
    ''' (integer,integer)->boolean
     Returns True if a and b are integers that results in an integer c, such that a^2+b^2 = c^2, where c remains to be an integer. 
     Else returns False

     Precondition(s): a and b must be integers, which result in an integer, c
     '''
    c=math.sqrt((a**2+b**2))
    return (c==math.floor(c))

################################################################### 
# Question 2
def mh2kh(s):
    ''' (number)->number
     Returns s, which is speed in miles/hour, in kilometers/hour
     '''
    return(s*1.60934)
################################################################### 
#Question 3
def in_out(xs,ys,side):
    '''(number, number, number)->boolean
    The function has inputs xs and ys which are the x and y coordinates of the square, with length of side s which is also inputted.  The function prompts the user to enter x and y coordinates of a query point. The function will return True if the coordinate point is within the square, or False if the quiery point is outside the square.
    Precondition(s): side is a non-negative number greater than 1
    '''
    x = float(input("Enter a number for the x coordinate of a query point:"))
    y = float(input("Enter a number for the y coordinate of a query point:"))
    return (xs<=x<=side) and (ys<=y<=side)
###################################################################
# Question 4
def safe(n):
    '''(number)->boolean
    Returns true if n does not have a 9 in it oand is not divisble by 9, else False
    Precondition(s): n is a non-negative number and has at most two digits
    '''
    return((n%9 != 0) and (n//10 != 9) and (n%10 != 9))

###################################################################
# Question 5
def quote_maker(quote, name, year):
    '''(string, string, integer)-> string
    The function returns a sentene as a string, which has combined the inputed quote, name, and year in a formed sentence
    '''
    return("In year, "+str(year)+" a person called name "+name+" said \""+quote+"\"")
###################################################################
# Question 6
def quote_displayer():
    '''(none) -> none
    The function will ask the user for a quote, name, and year then print the return statement from the quote_displayer by first calling it with the given inputs
    '''
    quote = input("Give me a quote:")
    name = input("Who said that?")
    year = input("What year did she/he say that?")
    print(quote_maker(quote,name,year))
###################################################################
# Question 7
def rps_winner():
    '''(none)->none
    The function displays the result of the rps game. The result is displayed as such: "Player 1 wins. That is true. It is a tie. That is not True" if player 1 wins, "Player 1 wins. That is false. It is a tie. That is not True", if player 2 wins, and finally "Player 1 wins. That is False
    It is a tie. That is not False" if it is a draw" 

    Precondition: Input has to be either "rock", "paper" or "scissors" in lower case
    '''
    choice_P1 = input("What choice did player 1 make? Type one of the following options: rock, paper, scissors:")
    choice_P2 = input("What choice did player 2 make? Type one of the following options: rock, paper, scissors:")

    result_draw = not(choice_P1 == choice_P2)
    result_p1 = (choice_P1 == "rock" and choice_P2 == "scissors") or (choice_P1 == "scissors" and choice_P2 == "paper") or (choice_P1 == "paper" and choice_P2 == "rock") 
    print("Player 1 wins. That is "+str(result_p1)+"\nIt is a tie. That is not "+str(result_draw))

###################################################################
# Question 8
def fun(x):
    '''(integer)->float
    The function returns a float value by plugging in the input, x, in a function, 10^(4y)=x+3 -> y=(log(x+3))/4

    Precondition: x should be a positive integer
    '''
    return ((math.log10(x+3))/4)
###################################################################
# Question 9
def ascii_name_plaque(name):
    '''
    (string)->none
    The function displays a plaque surrounding the string input given. The plaques are shown by printing * multiple times creating a pattern.
    '''
    stars = ("*")*len(name)
    blank = (" ")*len(name)
    print("******"+stars+"******")
    print("*     "+blank+"     *")
    print("*     "+name+"     *")
    print("*     "+blank+"     *")
    print("******"+stars+"******")
###################################################################
# Question 10
def draw_car():
    '''
    (none)->none
    The function draws after being called draws a colorful car by using the turtle graphics module.
    '''
    s=turtle.Screen()
    t=turtle.Turtle()

    t.speed(0)
    t.pensize(2)
    
    t.penup()
    t.setx(-200)
    t.sety(-100)

    t.pendown()
    t.begin_fill()
    t.fillcolor("#fc0000")
    t.pencolor("#020202")
    t.circle(70)
    t.end_fill()
    
    t.penup()
    t.goto(-200, -60)

    t.pendown()
    t.begin_fill()
    t.fillcolor("#e2df09")
    t.circle(30)
    t.end_fill()

    t.penup()
    t.goto(-200, -40)

    t.pendown()
    t.begin_fill()
    t.fillcolor("#d708e2")
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(200, -100)

    t.pendown()
    t.begin_fill()
    t.fillcolor("#fc0000")
    t.pencolor("#020202")
    t.circle(70)
    t.end_fill()

    t.penup()
    t.goto(200, -60)

    t.pendown()
    t.begin_fill()
    t.fillcolor("#e2df09")
    t.circle(30)
    t.end_fill()

    t.penup()
    t.goto(200, -40)

    t.pendown()
    t.begin_fill()
    t.fillcolor("#d708e2")
    t.circle(10)
    t.end_fill()
 
    t.left(315)
    t.forward(20)
    t.penup()

    t.goto(190, -35)

    t.pendown()
    t.left(240)
    t.forward(20)
    
    t.penup()
    t.goto(210, -30)
   
    t.pendown()
    t.left(15)
    t.forward(-20)

    t.penup()
    t.goto(205, -20)

    t.pendown()
    t.left(30)
    t.forward(-15)

    t.penup()
    t.goto(193, -20)

    t.pendown()
    t.left(100)
    t.forward(-20)

    t.penup()
    t.goto(-200, -40)


    t.pendown()
    t.left(-90)
    t.forward(20)
    t.penup()

    t.goto(-190, -35)

    t.pendown()
    t.left(240)
    t.forward(-20)
    
    t.penup()
    t.goto(-210, -30)
     
    t.pendown()
    t.left(-15)
    t.forward(22)

    t.penup()
    t.goto(-200, -20)
    
    t.pendown()
    t.left(-40)
    t.forward(20)

    t.penup()
    t.goto(-189, -30)

    t.pendown()
    t.left(100)
    t.forward(-20)
    
    t.penup()
    t.goto(-145, -70)

    t.begin_fill()
    t.fillcolor("#4bdb27")
    t.pendown()
    t.left(5)
    t.forward(-285)

    t.penup()
    t.goto(140, 50)

    t.pendown()
    t.left(90)
    t.forward(-60)
    t.forward(100)
    t.forward(-110)

    t.left(-90)
    t.forward(200)

    t.left(90)
    t.forward(192)
    t.end_fill()

    t.forward(-192)
    t.left(-90)
    t.forward(255)
    
    t.left(90)
    t.forward(140)

    t.left(90)
    t.forward(47)

    t.begin_fill()
    t.fillcolor("#b4c4b0")
    t.pencolor("#ffb2b2")
    t.forward(-70)
    t.left(-90)
    t.forward(50)
    t.left(90)
    t.forward(80)
    t.end_fill()


    t.penup()
    t.goto(-250, 120)
    

    t.pendown()
    t.begin_fill()
    t.fillcolor("#6b0000")
    t.left(60)
    t.forward(200)

    t.left(-60)
    t.forward(90)

    t.left(-90)
    t.forward(174)
    t.end_fill()

    t.begin_fill()
    t.fillcolor("#6b0000")
    t.forward(-174)
    t.left(90)
    t.forward(150)

    t.left(-75)
    t.forward(185)
    t.end_fill()

    t.pencolor("#000000")
    t.left(76)
    t.forward(100)

    t.left(-90)
    t.forward(70)

    t.left(-90)
    t.forward(30)
    t.forward(-70)

    t.left(90)
    t.forward(90)

    t.left(-90)
    t.forward(17)

    t.penup()
    t.goto(-263, 90)

    t.begin_fill()
    t.fillcolor("#fff200")
    t.pendown()
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.end_fill()

    t.penup()
    t.goto(0, 90)
    
    t.begin_fill()
    t.fillcolor("#fff200")
    t.pendown()
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.end_fill()

    t.penup()
    t.goto(220, 110)
    
    t.begin_fill()
    t.fillcolor("#fff200")
    t.pendown()
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.end_fill()
###################################################################
# Question 11
def alogical(n):
    '''
    (number)-> number
    The function returns the minimum number of times n can be divided by 2 to get a number equal to or smaller than 1.
    Precondition: n is bigger than 1
    '''
    return math.ceil(math.log2(n))
###################################################################
# Question 12
def time_format(h, m):
    '''
    (integer, integer)-> string
    The function returns the time expressed in a sentence by a string, when the hours in 24-hour notation (h) and minutes(m) are inputted.The minutes are rounded to the nearest 5 minutes.

    Precondition: h must be in between 0 and 23, and m must be between 0 and 59
    '''
    m=(m+2)//5*5
    if(m==60):
        m=0
        h=h+1
    if(m==0):
        if(h+1>=24):
            h=0
        return str(h)+" o' clock"
    elif(m==30):
        return "half past "+str(h)+" o' clock"
    elif(m<30):
        return str(m)+" minutes past "+str(h)+" o' clock"
    elif(m>30):
        if(h+1>=24):
            h=-1
        return str(60-m)+" minutes to "+str(h+1)+" o' clock"
###################################################################
# Question 13
def cad_cashier(price, payment):
    '''
    (number, number)->float
    The function returns the change from a given price and the payment made. Change has two decimal values. 
    Precondition: price and payment are non-negative and payment is greater than the price.10
    '''
    dollars = (payment-price)//1
    cents = ((((payment-price)-dollars)*100)+2)//5*5/100
    return dollars+cents
###################################################################
# Question 14
def min_CAD_coins(price, payment):
    '''
    (number, number)->integer, integer, integer, integer, integer
    The function returns the minimum number of coins that the cashier has to return when inputted a price and payment.
    Precondition: price and payment are non-negative numbers, and payment is greater than price
    '''

    change = cad_cashier(price, payment)
    centsChange = (change//1+(change-change//1))*100

    toonie=centsChange//200
    centsChange-=toonie*200
    loonie=centsChange//100
    centsChange-=loonie*100
    quarter=centsChange//25
    centsChange-=quarter*25
    dime=centsChange//10
    centsChange-=dime*10
    nickel=centsChange//5
    centsChange-=nickel*5

    return int(toonie), int(loonie), int(quarter), int(dime), int(nickel)
###################################################################
