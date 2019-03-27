import string
def validFile():
    '''
    (None)->String or None
    Testing whether the name given is a valid name for a file or not. None is returned if not.
    '''
    file = input("Enter the name of the file:").strip()
    try:
        f=open(file)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file = None
    return file

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    file = None
    while file==None:
        file=validFile()
    return open(file)

def remove_punctuation(words):
    '''
    (Sring)->String
    The function returns the string with the punctuation removed
    '''
    new = ""
    for char in words:
        if char not in string.punctuation:
            new+=char.lower()
    return new

def process_lines(ls):
    '''
    (String)->String 2D List
    Turns the text given into a processed 2D List
    '''
    l = []
    for p in ls:
        sen = remove_punctuation(p)
        lw = sen.split() #slpit lines
        n = []
        for w in lw:
            if is_word(w) and len(w)>1:
                n.append(w)
        l.append(n)
    return l
        

def make_dict(lsw):
    dic={}
    l = len(lsw)
    for a in range(l):
        for word in lsw[a]:
            if word in dic:
                dic[word].add(a+1)
            else:
                dic[word]={a+1}
    return dic

def is_word(word):
    '''
    (String)->Booleanl
    The function retruens True if the word has all letters and false otherwise
    '''
    for char in word:
        if not char.isalpha():
            return False
    return True
    
def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    lst=fp.read().splitlines()
    l=process_lines(lst)
    dic=make_dict(l)
    return dic

def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    query = query.split()
    if len(query)==0: return set()
    co = set(D[query[0]])
    for word in query:
        co = set.intersection(set(D[word]), co)

    return sorted(list(co))

def is_valid(D,query):
    query = query.split()

    if query=="":
        return ""
    
    for word in query:
        if word not in D:
            return word
    return None
    

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

while query!="q":
    query = remove_punctuation(query)
    inputt=is_valid(d, query)

    if inputt!=None:
        print("Word '"+inputt+"' not in the file.")
    else:
        co = find_coexistance(d, query)
        if len(co)==0:
            print("The one or more words you entered does not coexis in the file:")
        else:
            print("The one or more words you entered coexisted in the following lines of the file:")
            for a in co:
                print(a, end=" ")
            print("\n")
    query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

    

