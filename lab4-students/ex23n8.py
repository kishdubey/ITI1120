def is_divisible(n,m):
     '''(int, int)->bool
     returns True if n is divisible by n, and False otherwise.'''
     return n%m==0

def is_divisible23n8(n):

     for i in range(n):
          if  ((is_divisible(i,2) or is_divisible(i,3)) and not(is_divisible(i,8))):
               print(i)

num = int(input("Please enter a non-negative integer "))
is_divisible23n8(num)







     
