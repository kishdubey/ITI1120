#Question 3A
n = int((input("Enter 1st integer:")))
m = int((input("Enter 2nd integer:")))

def is_divisible(n, m):
    '''
    (integer, integer)->boolean
    The function return true if n is divisible by n, and False otherwise. In addition the function prints whether n and m are divisible.
    '''
    if(n/m == n//m):
        print(str(n)+" is divisble by "+str(m))
        return True
    
    else:
        print(str(n)+" is not divisble by "+str(m))
        return False

is_divisible(n,m)

    
