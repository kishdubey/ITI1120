#Family name: Kish Dubey
# Student number:  300080370
# Course: IT1 1120 
# Assignment Number 2 Part 2

'''References: Help for 2.3, was found from observing the solution for finding the nth number in the Fibonacci Sequence. (https://gist.github.com/NordomWhistleklik/3873990)
               (https://stackoverflow.com/questions/6933741/python-find-all-subwords-that-can-be-found-inside-of-a-word) was used for 2.10
'''
############################################################
#Question 2.1
############################################################
def min_enclosing_rectangle(radius, x, y):
    '''
    (number, number, number)-> number, number
    The function when given, the radius of a circle, with x and y coordinates of the centre point of the circle returns the x and y coordinate of the bottom corner of the smallest axis-aligned rectangle that contains that circle. If the radius is negative , the function returns none.
    '''
    if radius<0:
        return None
    else:
        return (x-radius, y-radius)
############################################################
#Question 2.2
############################################################
def series_sum():
    '''
    (None)->number
    The function returns the sumer of a given series, 1000 + 1/1^2 + 1/2^2 + 1+3^2 + 1/4^2 + ... + 1/n^2, if the number inputted by the user is non negative. If that number is
    negative, then None is returned.
    '''
    n = int(input("Please enter a non-negative integer: ")) 
    sum=1000
    if n<0:
        return None
    else:
        for i in range(1, n+1):
            sum = sum + (1/pow(i, 2))
        return sum
############################################################
#Question 2.3~
############################################################
def pell(n):
    '''
    (integer)->integer
    The function returns the nth Pell Number, when n (the position) of the number is given. Pell number are defined by a given function. If the n given is negative, None is returned.
    '''
    if n<0:
        return None
    elif n==0 or n==1 or n==2:
        return n
    elif n>1:
        first = 1
        nextt = 2
        for i in range(n-2):
            sumPell = 2*nextt+first
            first = nextt
            nextt = sumPell
        return sumPell
############################################################
#Question 2.4
############################################################
def countMembers(s):
    '''
    (string)->integer
    The function returns the number of extraordinary numbers in the string inputted
    '''
    counter = 0
    for char in s: 
        if char in "efghijFGHIJKLMNOPQRSTUVWX23456!\\,":
            counter+=1
    return counter
############################################################
#Question 2.5
############################################################
def casual_number(s):
    '''
    (string)->integer
    The function returns the integer with commas removed, in cases where commas are used to represent thousand, hundred thousand, million etc. If the input does not look like a number, None is returned.
    '''
    new = ""
    if(s==s.upper() and s==s.lower()):
        for number in s:
            if number in "0123456789-":
                if s.count("-")<=1:
                    new+=number
                elif s.count("-")>1:
                    return None
                    
        for c in new:
            if len(new)<2:
                if c in "-":
                    return None
                
        return int(new)
    
    return None
############################################################
#Question 2.6
############################################################
def alienNumbers(s):
    '''
    (string)->integer
    The function returns the value of the charaters in a given string as per the NASA value sheet
    Precondition: No onput will be outside of this set {T,y, !,a, N, U}.
    '''
    sum = (s.count("T")*1024)+(s.count("y")*598)+(s.count("!")*121)+(s.count("a")*42)+(s.count("N")*6)+(s.count("U")*1)
    return sum
############################################################
#Question 2.7
############################################################
def alienNumbersAgain(s):
    '''
    (string)->integer
    The function return the value of the characters given in a string as per the NASA value sheet.
    Precondition: No onput will be outside of this set {T,y, !,a, N, U}
    '''
    counterT = 0
    countery = 0
    counterX = 0
    countera = 0
    counterN = 0
    counterU = 0

    for char in s:
        if char == "T":
            counterT+=1
        elif char=="y":
            countery+=1
        elif char=="!":
            counterX+=1
        elif char=="a":
            countera+=1
        elif char=="N":
            counterN+=1
        elif char=="U":
            counterU+=1

    return ((counterT*1024) + (countery*598) + (counterX*121) + (countera*42) + (counterN*6) + (counterU))    
############################################################
#Question 2.8
############################################################
def encrypt(s):
    '''
    (string)->string
    The function returns a modified version of the string inputtied s, by a given algorithm.
    '''
    reverse = s[::-1]
    encrypted = ""

    for i in range(0, round(len(s)/2)+1):
        encrypted = encrypted + reverse[i] + reverse[len(s) -1 -i]
    dif = len(encrypted) - len(s)

    if dif>0:
        encrypted = encrypted[:-dif]

    return encrypted
############################################################
#Question 2.9
############################################################
def oPify(s):
    ''''
    (string)->string
    The function returns the string inputted, by inputting either lower case or upper case "op" in between a pair of consecutive characters in a string whether being either lower case or upper case respectively.
    '''
    mod = ""

    for i in range(len(s)-1):
        first = s[i]
        nextt = s[i+1]

        if(first.isalpha()):
            if(first.isupper() and nextt.isalpha()):
                mod+=first+"O"
            elif not(first.isupper()) and nextt.isalpha():
                mod+=first+"o"
        
        if (nextt.isalpha()):
            if (nextt.isupper()) and first.isalpha():
                mod+="P"
            elif not(nextt.isupper()) and first.isalpha():
                mod+="p"

        if not(first.isalpha() and nextt.isalpha()):
            mod+=first
            
    return mod+s[-1]
############################################################
#Question 2.10
############################################################
def nonrepetitive(s):
    '''
    (string)->boolean
    The function returns True or False depending on whether the inputted string is nonrepetitive or repetitive respectively. A nonrepetitive word is a word that does not contain any subword twice in a row (A2.pdf)
    '''
    for i in range(1, len(s)):
        substring = s[:i]
        
        if substring * (len(s)//len(substring))+(substring[:len(s)%len(substring)]) == s and s.count(substring)>1:
            return False
    return True
