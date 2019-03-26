# an implementation with while loop
def linear_search_v1(lst, value):
     """ (list, object) -> int
     Return the index of the first occurrence of value in lst, or return
     -1 if value is not in lst.
     >>> linear_search_v1([2, 5, 1, -3], 5)
     1
     >>> linear_search_v1([2, 4, 2], 2)
     0
     >>> linear_search_v1([2, 5, 1, -3], 4)
     -1
     >>> linear_search_v1([], 5)
     -1
     """

     i = len(lst)-1 # The index of the next item in lst to examine.
     # Keep going until we reach the end of lst or until we find value.
     while lst[i] != value:
          print(lst[i])
          i=i-1
     # If we fell off the end of the list, we didn't find value.
     if i == len(lst):
          return -1
     else:
          return i


# an implementation with for loop
def linear_search_v2(lst, value):
     """ same docstring as above
     """

     for i in range(len(lst)-1, 0, -1):
          print(lst[i])
          if lst[i] == value:
               return i
     return -1


# an implementation with sentinel

# all three versions are correct and do roughly n operations on a list of size n
# the following solution uses no branching (i.e. if statements)

def linear_search_v3(lst, value):
     """ same docstring as above
     """
     i=len(lst)-1
     lst.append(value)
     
     # Keep going until we find value.
     while lst[i] != value:
          i=i-1
     # Remove the sentinel.
     lst.pop()
     # If we reached the end of the list we didn't find value.
     if i == len(lst):
          return -1
     else:
          return i

#Prog Ex 2
def min_or_max_index(lst, b):
    mina = lst[0]
    mini = 0
    maxa = lst[0]
    maxi = 0
    if(b):
        for i in range(len(lst)):
            if lst[i]<mina:
                mina = lst[i]
                mini = i

        return (mina, mini)

    else:
        for a in range(len(lst)):
            if lst[a]>maxa:
                maxa = lst[a]
                maxi = a

        return (maxa, maxi)

#Prog Ex 3
def first_one(l):
     first=0
     last = len(l) - 1
     res = -1

     while(first<=last):
         mid = (first+last)//2
         #print(first, last, mid)
         if l[mid]==1:
             res = mid
             last = mid-1
         elif l[mid]<1:
             first = mid+1
         else:
             last = mid-1
     return res


             
            
    
        

            
