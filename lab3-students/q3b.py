#Question 3B
a = int(input("Enter integer:"))

def is_divisible(n, m):
    '''
    (integer, integer)->boolean
    The function return true if n is divisible by n, and False otherwise. In addition the function prints whether n and m are divisible.
    '''
    if(n/m == n//m):
        #print(str(n)+" is divisble by "+str(m))
        return True
    
    else:
        #print(str(n)+" is not divisble by "+str(m))
        return False



def is_divisible23n8(test):
    '''
    (integer) -> string
    The function returns "yes" if test is divisible by 2 or 3 but not 8, otherwise return "no"
    '''
    if(is_divisible(test, 2) or is_divisible(test, 3) == True):
        print(str(test)+" is divisible by 2 or 3 but not 8")
        return"yes"
    else:
        print("It is not true that"+str(test)+"is divisible by 2 or 3 but not 8")
        return "no"        

is_divisible23n8(a)
