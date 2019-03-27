import random
def binary_search(L, v):
     ''' (list, object) -> int
     Return the index of the first occurrence of value in L, or return
     -1 if value is not in L.
     '''
     b=0
     e = len(L) - 1

     while b != e + 1:
          mid = (b + e) // 2
          if L[mid] < v:
               b=mid+1
          else:
               e=mid-1
          
     if 0 <= b < len(L) and L[b] == v:
          return True
     else:
          return False

def uniqueNetwork(file_name):
    '''
    (str)->List of integers
    The function returns a list of integers which are the ids of all the users of the network. 
    '''
    net = open(file_name).read().splitlines()
    network = []

    for a in range(1,len(net)):
        user = int(net[a][:(net[a].index(" "))])
        if not(user in network):
            network.append(user)

        friend = int(net[a][(net[a].index(" ")):])
        if not(friend in network):
            network.append(friend)

    network.sort()
    return network

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is no line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).

    (id, list of friends)
    '''
    friends = open(file_name).read().splitlines()
    network=[]
    friendships = []

    for b in range(1,len(friends)):
        user = friends[b][:(friends[b].index(" "))]
        friend = friends[b][(friends[b].index(" ")):]
        friendships.append([int(user),int(friend)]) #putting every single friendship in a list

    unique = uniqueNetwork(file_name)
    
    for i in range(len(friendships)):
        user1 = friendships[i][0]
        user2= friendships[i][0]
        friend1 = friendships[i][1]
    
        if user1 in unique:
            network.append(((user1),[friend1]))
            unique.remove(user1)

        else:
            for a in range(len(network)):
                if user1 == network[a][0]: #checking if the friend is a user in the list, then getting its position with a
                    network[a][1].append(friend1)
                    
        if friend1 in unique:
            network.append(((friend1,[user2])))
            unique.remove(friend1)

        else:
            for j in range(len(network)):
                if friend1 == network[j][0]: #checking if the friend is a user in the list, then getting its position with j
                    network[j][1].append(user2)
                    
    network.sort()
    return network

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->int
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    friends1 = []
    friends2 = []
    for i in range(len(network)):
        if user1 == network[i][0]:
            friends1 = network[i][1].copy()

    for j in range(len(network)):
        if user2 == network[j][0]:
            friends2 = network[j][1].copy()
            
    for a in range(len(friends1)):
        if binary_search(friends2, friends1[a]):
            common.append(friends1[a])

    for b in range(len(friends2)):
        if binary_search(friends1, friends2[b]) and not(binary_search(common,friends2[b])):
            common.append(friends2[b])
                               
    return common
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE
  
            
    t = []
    for i in range(len(network)):
        if not(binary_search(network[i][1], user)):
            t.append((getCommonFriends(user, network[i][0], network), network[i][0]))
            
    maxa = 0
    recom = t[0][1]
    for a in range(len(t)):
        if maxa<len(t[a][0]) and t[a][1]!=user:
            maxa = len(t[a][0])
            recom = t[a][1]

        elif maxa==len(t[a][0]):
            if t[a][1]<recom and t[a][1]!=user:
                maxa = len(t[a][0])
                recom = t[a][1]

    if maxa==0:
        return None
    
    return recom
            
def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    
    counter = 0
    for i in range(len(network)):
        if len(network[i][1])>=k:
               counter+=1
    return counter

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    maxa = len(network[0][1])
    for i in range(len(network)):
        if len(network[i][1]) >= maxa:
               maxa = len(network[i][1])
    return maxa

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    for i in range(len(network)):
        if len(network[i][1]) == maximum_num_friends(network):
              max_friends.append(network[i][0])
    return max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''
    average = 0
    for i in range(len(network)):
        average+=len(network[i][1])

    return average/len(network)
def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    for i in range(len(network)):
        if len(network[i][1])==len(network)-1:
            return True
    return False


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    t = True
    while(t):
        ans = input("Enter an integer for a user ID: ")
        try:
            ans = int(ans)
            for i in range(len(network)):
                if network[i][0] == ans:
                    return ans
            else:
                print("That user ID does not exist. Try again.")
        except:
            print("That was not an integer. Please try again.")
##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
