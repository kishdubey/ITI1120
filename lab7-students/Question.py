def indexes(word, character):
    '''
    (string, string)->list of numbers
    '''
    index = []
    word = list(word)
    for i in range(len(word)):
        if word[i] == character:
            index.append(i)
    return index

def doubles(l):
    for i in range(len(l)-1):
        if l[i+1] == 2*l[i]:
            print(str(l[i+1]))

def four_letter(l):
    four = []
    for i in range(len(l)):
        if len(l[i]) == 4:
            four.append(l[i])
    return four

def inBoth(l1, l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                return True
    return False

def intersect(l1, l2):
    inter = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                inter.append(l1[i])
    return inter

def pair(l1, l2, n):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] + l2[j] == n:
                print(str(l1[i])+" "+str(l2[j]))

def pairSum(l, n):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == n:
                print(str(i)+" "+str(j))

def lastfirst(l):
    full = []
    first = []
    last = []

    for i in range(len(l)):
        l[i] = l[i].replace(",", "")

    for a in range(len(l)):
        l[a] = l[a].split()

    for b in range(len(l)):
        last.append(l[b][0])
        first.append(l[b][1])

    full.append(first)
    full.append(last)

    return full

def subsetSum(l, target):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(j+1, len(l)):
                if l[i] + l[j] + l[k] == target:
                    return True
    return False

def mystery(n):
    counter = 0
    while(n>=1):
        n=n/2
        if(n>=1): 
            counter+=1
    return counter

def inversions(s):
    sort = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    

    s_ = ""

    for a in range(len(s)):
        if s.count(s[a])>1:
            s_+=""
        else:
            s_+=s[a]
            
    length = len(s_)
    sort = sort[:length]
    counter = 0

    
    for i in range(length):
        if sort[i] != s_[i]:
            counter+=1

    return counter
        

    
    
    
