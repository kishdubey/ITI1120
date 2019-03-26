def ah(l,x,y):
    '''
    Precondition: x<=y
    '''
    counter = 0
    temp = l[0]
    for item in l:
        if (item>=x) and (item<=y):
            counter+=1
            if temp>item:
                temp = item
    return counter, temp

def is_perfect(n):
    '''
    Perfect number is sum of all of its positive divisors, excluding itself. 
    '''
    sum=0
    for i in range(1, n):
        if n%i==0:
            sum+=i

    return(sum==n)

def is_perfect_modified():
    #19 days -> 5th
    #13 years -> 6th
    perfect = []
    for a in range(1, 35000000):
        sum=0
        for i in range(1, a):
            if a%i==0:
                sum+=i

        if sum==a:
            perfect.append(a)
    print(perfect)

def arithmetic(l):
    dif = l[1] - l[0]
    for i in range(len(l) - 1):
        if not (l[i + 1] - l[i] == dif):
             return False
    return True

def is_sorted(l):
    for i in range(len(l)-1):
        if not (l[i] <= l[i+1]):
            return False
    return True
                   
            
        
        
    
            


            
        
            
