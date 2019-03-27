import random

# Read and understand the docstrings of all of the functions in detail.

def make_deck(num):
    '''(int)->list of int
        Returns a list of integers representing the strange deck with num ranks.

    >>> deck=make_deck(13)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404, 105, 205, 305, 405, 106, 206, 306, 406, 107, 207, 307, 407, 108, 208, 308, 408, 109, 209, 309, 409, 110, 210, 310, 410, 111, 211, 311, 411, 112, 212, 312, 412, 113, 213, 313, 413]

    >>> deck=make_deck(4)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    '''
    a=100
    b=200
    c=300
    d=400
    deck = []

    for i in range(1, num+1):
        deck.append(a+i)
        deck.append(b+i)
        deck.append(c+i)
        deck.append(d+i)
        
    return deck
def shuffle_deck(deck):
    '''(list of int)->None
       Shuffles the given list of strings representing the playing deck

    Here you should use random.shuffle function from random module.
    
    Since shufflling is random, exceptionally in this function
    your output does not need to match that show in examples below:

    >>> deck=[101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    >>> shuffle_deck(deck)
    >>> deck
    [102, 101, 302, 104, 304, 103, 301, 403, 401, 404, 203, 204, 303, 202, 402, 201]
    >>> shuffle_deck(deck)
    >>> deck
    [402, 302, 303, 102, 104, 103, 203, 301, 401, 403, 204, 101, 304, 201, 404, 202]
    '''
    d = deck
    random.shuffle(d)

def deal_cards_start(deck):
    '''(list of int)-> list of int

    Returns a list representing the player's starting hand.
    It is  obtained by dealing the first 7 cards from the top of the deck.
    Precondition: len(dec)>=7
    '''
    d = deck
    start_deck = []
    for i in range(7, -1, -1):
        start_deck.append(d.pop())
        
    return start_deck
def deal_new_cards(deck, player, num):
    '''(list of int, list of int, int)-> None
    Given the remaining deck, current player's hand and an integer num,
    the function deals num cards to the player from the top of the deck.
    If len(deck)<num then len(deck) cards is dealt, in particular
    all the remaining cards from the deck are dealt.

    Precondition: 1<=num<=6 deck and player are disjoint subsets of the strange deck. 
    
    >>> deck=[201, 303, 210, 407, 213, 313]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 313, 213, 407, 210]
    >>> deck
    [201, 303]
    >>>

    >>> deck=[201, 303]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 303, 201]
    >>> deck
    []
    '''
    d = deck
    p = player

    if(len(d) > num):
        for i in range(num, 0, -1):
            p.append(d.pop())
    else:
        for b in range(len(d), 0, -1):
            p.append(d.pop())
def print_deck_twice(hand):
    '''(list)->None
    Prints elements of a given list deck in two useful ways.
    First way: sorted by suit and then rank.
    Second way: sorted by rank.
    Precondition: hand is a subset of the strange deck.
    
    Your function should not change the order of elements in list hand.
    You should first make a copy of the list and then call sorting functions/methods.

    Example run:
    >>> a=[311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]
    >>> print_deck_twice(a)

    101 104 105 202 204 301 303 305 306 311 313 401 407 408 409 410 

    101 301 401 202 303 104 204 105 305 306 407 408 409 410 311 313 
    >>> a
    [311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]

    '''
    deck_c = []
    for i in range(len(hand)):
        deck_c.append(hand[i])

    deck_c = hand[:]
    deck_c.sort()

    print(" ".join(str(x) for x in deck_c))
    
    rank = []

    for a in range(len(deck_c)):
        if deck_c[a]%100 == 1:
            rank.append(deck_c[a])

    for b in range(len(deck_c)):
        if deck_c[b]%100 == 2:
            rank.append(deck_c[b])

    for c in range(len(deck_c)):
        if deck_c[c]%100 == 3:
            rank.append(deck_c[c])

    for d in range(len(deck_c)):
        if deck_c[d]%100 == 4:
            rank.append(deck_c[d])

    for e in range(len(deck_c)):
        if deck_c[e]%100 == 5:
            rank.append(deck_c[e])

    for f in range(len(deck_c)):
        if deck_c[f]%100 == 6:
            rank.append(deck_c[f])

    for g in range(len(deck_c)):
        if deck_c[g]%100 == 7:
            rank.append(deck_c[g])

    for h in range(len(deck_c)):
        if deck_c[h]%100 == 8:
            rank.append(deck_c[h])

    for j in range(len(deck_c)):
        if deck_c[j]%100 == 9:
            rank.append(deck_c[j])

    for k in range(len(deck_c)):
        if deck_c[k]%100 == 10:
            rank.append(deck_c[k])

    for l in range(len(deck_c)):
        if deck_c[l]%100 == 11:
            rank.append(deck_c[l])

    for m in range(len(deck_c)):
        if deck_c[m]%100 == 12:
            rank.append(deck_c[m])

    for n in range(len(deck_c)):
        if deck_c[n]%100 == 13:
            rank.append(deck_c[n])

    print(" ".join(str(y) for y in rank))
def is_valid(cards, player):
    '''(list of int, list of int)->bool
    Function returns True if every card in cards is the player's hand.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.

    Precondition: cards and player are subsets of the strange deck.
    
    >>> is_valid([210,310],[201, 201, 210, 302, 311])
    310 not in your hand. Invalid input
    False

    >>> is_valid([210,310],[201, 201, 210, 302, 310, 401])
    True
    '''
    for i in range(len(cards)):
            if player.count(cards[i])<1:
                print(str(cards[i])+" not in your hand. Invalid input")
                return False   
    return True
            
def is_discardable_kind(cards):
    '''(list of int)->True
    Function returns True if cards form 2-, 3- or 4- of a kind of the strange deck.
    Otherwise it returns False. If there  is not enough cards for a meld it also prints  a message about it,
    as illustrated in the followinng example runs.
    
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.
    
    >>> is_discardable_kind([207, 107, 407])
    True
    >>> is_discardable_kind([207, 107, 405, 305])
    False
    >>> is_discardable_kind([207])
    Invalid input. Discardable set needs to have at least 2 cards.
    False
    '''
    if(len(cards) >= 2):
        ending = cards[0]%100
        for i in range(1, len(cards)):
            if cards[i]%100 != ending:
                return False
        return True
    else:
        print("Invalid input. Discardable set needs to have at least 2 cards.")
        return False
def is_discardable_seq(cards):
    '''(list of int)->True
    Function returns True if cards form progression of the strange deck.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.

    >>> is_discardable_seq([313, 311, 312])
    True
    >>> is_discardable_seq([311, 312, 313, 414])
    Invalid sequence. Cards are not of same suit.
    False
    >>> is_discardable_seq([311,312,313,316])
    Invalid sequence. While the cards are of the same suit the ranks are not consecutive integers.
    False
    >>> is_discardable_seq([201, 202])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    >>> is_discardable_seq([])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    '''
    dup = cards[:]
    if len(cards)>=3:
        dup = [x//100 for x in cards]
        for i in range(len(dup)-1):
            if dup[i] != dup[i+1]:
                print("Invalid sequence. Cards are not of same suit")
                return False

        dup2 = cards[:]
        dup2.sort()
        dif = dup2[1] - dup2[0]
        
        for a in range(len(dup2)-1):
            if dup2[i+1] - dup2[i] != dif:
                print("Invalid sequence. While the cards are of the same suit the ranks are not consecutive integers.")
                return False
            
        return True
    else:
        print("Invalid sequence. Discardable sequence needs to have at least 3 cards.")
        return False
def rolled_one_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 1
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> rolled_one_round(player)
    Discard any card of your choosing.
    Which card would you like to discard? 103
    103
    No such card in your hand. Try again.
    Which card would you like to discard? 102

    Here is your new hand printed in two ways:

    201 212 311 

    201 311 212 

    '''
    p = player
    repeat = True
    print("Discard any card of your choosing.")
    while(repeat):
        answer = int(input("Which card would you like to discard? "))
        if p.count(answer) == 1:
            p.remove(answer)
            repeat = False
        else:
            print("No such card in your hand. Try again.")

    print("Here is your new hand printed in two ways:")
    print_deck_twice(p)
    
def rolled_nonone_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 2, 3, 4, 5, or 6.
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 102 103 104
    103 not in your hand. Invalid input
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 403 203

    Here is your new hand printed in two ways:

    102 104 401 

    401 102 104 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 2:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412 413

    Here is your new hand printed in two ways:

    103 211 

    103 211 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 3:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412
    Invalid sequence. Discardable sequence needs to have at least 3 cards.

    >>> #example 4:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? alsj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? hlakj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? 22 33
    Yesor no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no
    '''
    p = player
    val = True
    while(val):
        choice = input("Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind?").strip().lower()
        if choice=="yes":
            user_input = input("Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space").strip().split()
            user_list = []

            for i in range(len(user_input)):
                user_list.append(int(user_input[i]))
            
            z=0
            a=0

            dup2 = user_list[:]
            dup2.sort()
            dif = dup2[1] - dup2[0]
        
            for h in range(len(dup2)-1):
                if dup2[h+1] - dup2[h] == dif and len(dup2)<=2 and dup2[h+1]//100 == dup2[h]//100:
                    print("Invalid sequence. Discardable sequence needs to have at least 3 cards.")
                    z = -1
                    a = -1
                    val = False
                    
            if a==0:
                for a in range(len(user_list)):
                    if p.count(user_list[a]) < 1:
                        print(str(user_list[a])+" not in your hand. Invalid input")
                        z = -1
                        
            if z == 0:
                for b in range(len(user_list)):
                    p.remove(user_list[b])
                print("Here is your new hand printed in two ways:")
                print_deck_twice(p)
                    
        elif choice=="no":
            val = False

def roll_dice():
    '''
    (None)->integer
    Generates a random number between 1-6, to be used as the dice in the game
    '''
    return random.randint(1, 6)
# main
print("Welcome to Single Player Rummy with Dice and strange deck.\n")
size_change=input("The standard deck  has 52 cards: 13 ranks times 4 suits.\nWould you like to change the number of cards by changing the number of ranks? ").strip().lower()
if(size_change == "yes"):
    num = int(input("Enter a number between 3 and 99, for the number of ranks: "))
    print("You are playing with a deck of "+str(num)+" cards")
    deck = make_deck(num)
    
else:
    print("You are playing with a deck of 52 cards")
    deck = make_deck(52)

shuffle_deck(deck)
player = deal_cards_start(deck)
print("Here is your new hand printed in two ways:\n")
print_deck_twice(player)

counter = 1

while(len(player)>0):
    print("Welcome to round "+str(counter))
    roll = input("Please roll the dice.")
    rol = roll_dice()
    if roll == "":
        print("You rolled the dice and it shows:"+str(rol))
    else:
        print("You rolled the dice and it shows:"+str(rol))

    if 2<=rol<=6:
        print("Since your rolled, "+str(rol))
        rolled_nonone_round(player)
    else:
        rolled_one_round(player)

    print("Round "+str(counter)+" Completed")
    counter+=1
    
    
    
    



