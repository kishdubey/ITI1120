def sum_odd_while_v2(n):
    '''(int)->int
        Returns the sum of all odd integers between 5 and n
    '''
    odd_sum = 0
    i=5
    #while i<=n:
    #    while i<=n and i%2==1:
    #        odd_sum+=i
    #        i+=1
    #    i+=1
    while i<=n:
        odd_sum+=i
        i+=2
    return odd_sum

def user():
    condition = True
    while condition:
        x = int(input("Enter First Digit: \n"))
        y = int(input("Enter Second Digit: \n"))

        print(x+y)

        decision = input("Would you like to run the program again? Yes or no. \n")
        if(decision.lower(),strip() == "yes"):
            condition = True
        else:
            condition = False

def first_neg(a):
    i=0
    #while i<len(a):
    #    while a[i]<0:
    #        return i
    #    i+=1

    while i<len(a) and a[i]>=0:
        i+=1
    return i

def sum_5_consecutive_for(l):
    if len(l)<5:
        return False
    
    for i in range(len(l)-4):
        if l[i] + l[i+1] + l[i+2] + l[i+3] + l[i+4] == 0:
            return True
    return False
    
def sum_5_consecutive_while(l):
    
    i = 0
    if len(l) < 5:
        return False
    while i < len(l) - 4:
        if l[i] + l[i+1] + l[i+2] + l[i+3] + l[i+4] == 0:
            return True
        i += 1 
    return False

def various_lists():
    n = int(input("enter a positiveeven integer" ))

    a = []
    for i in range(n):
        a.append(n)

    b = []
    for i in range(n):
        b.append(random.randint(1,100))

    c=b

    for i in range(len(c)//2):
        c[i]=0
    print(b)
    print(c)

    d=b[:]

    e = []
    for i in range(0, len(b), 2):
        e = b[i]
    

    

def fib(n):
    a = []
    a.append(1)
    a.append(1)
    for i in range(2, n):
        a.append(a[i-2] + a[i-1])
    print(a)

def fib_while(n):
    a = []
    a.append(1)
    a.append(1)
    i = 2
    while(i<n):
        a.append(a[i-2] + a[i-1])
        i+=1
    print(a)

def inner_product(l1, l2):
    total = 0
    for i in range(len(l1)):
        total += l1[i] * l2[i]
    return total

def inner_product_while(l1, l2):
    total = 0
    i = 0
    while(i<len(l1)):
        total += l1[i] * l2[i]
        i+=1
    return total




    
        
        
        
