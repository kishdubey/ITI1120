
########## task 1 ################

def orange(n):
    if n > 0:
        print(n,end=" ")
        orange(n-2)

orange(10)

print()

#riddle2

def guava(n):
    if n > 0:
        guava(n-2)
        print(n,end=" ")

guava(10)

print()

########## task 2 ################

def mulberry(n):
    if n == 1:
        return 1 
    else:
      return n + mulberry(n - 1) 

print( mulberry(4) )

########## task 3 ################

def cantaloupe(n): 
    if n > 0:
        print( n % 10)
        cantaloupe(n // 10)     
    
cantaloupe(7254)

########## task 4 ################
def almond(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        tmp=almond(lst[0:len(lst)-1])
        if tmp>lst[len(lst)-1]:
            return tmp
        else:
            return lst[len(lst)-1]

a = [2, 7, -11]
print( almond(a) )

########## task 5 ################
def fig(lst, high):
    if high == 0:
        return lst[0]
    else:
        tmp=fig(lst, high - 1)
        if tmp>lst[high]:
            return tmp
        else:
            return lst[high]

a = [2, 7, -11]
print( fig (a, len(a)-1) )

########## task 6 ################
def nox(s, ch):
    if len(s)==0:
        return s
    elif s[0]==ch:
        return nox(s[1:], ch)
    else:
        return s[0]+nox(s[1:], ch)

print( nox('Cacic', 'c' ))

########## exercise 1 ################
def m(n):
    if n==0:
        return 0
    else:
        a = n/(2*n+1)
        return a + m(n-1)

########## exercise 2 ################
def count_digits(n):
    if n==0:
        return 0
    else:
        return 1+count_digits(n//10)

########## exercise 3 ################
def is_palindrome(n):

    n = n.upper()
    
    if len(n)<1:
        return True
    else:
        if n[0]==n[-1]:
            return is_palindrome(n[1:-1])
        else:
            return False
        
########## exercise 4 ################
def to_alpha(s):
    a =""
    for char in s:
        if char.isalpha():
            a+=char
    return a
def is_palindrome_v2(n):

    n = n.upper()
    n = to_alpha(n)
    
    if len(n)<1:
        return True
    else:
        if n[0]==n[-1]:
            return is_palindrome(n[1:-1])
        else:
            return False

########## exercise 5################
def gcd(a, b):
    if b==0:
        return a

    else:
        c = a%b
        return gcd(b, c)
