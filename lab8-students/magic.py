def is_square(m):
     '''2d-list => bool
     Return True if m is a square matrix, otherwise return False
     (Matrix is square if it has the same number of rows and columns'''
     for i in range(len(m)):
          if len(m[i]) != len(m):
               return False
     return True

def maximum(m):
     '''(2D list)->number
     Returns the maximum element among all the numbers that are in even columns of m
     i.e the maximum element amoung all elements in 0th, 2th, 4th etc. column
     Precondition: m is a matrix filled with numbers with at least 1 row and 1 column
     
     >>> max_over_all_even_cols([1,1,1,1,1,1,1],[1,10,3,20,12,6,0] )
     12
     '''
     # your code goes here
     maxa = m[0][0]
     for row in range(len(m)):
          for col in range(0, len(m[0])):
               if m[row][col] > maxa:
                    maxa = m[row][col]
     return maxa

def print_matrix(m):
     '''(2D list)->None
     prints values in 2D list m row by row'''
     for row in m:
          for item in row:         #print item followed by 
               print(item, end=' ')    #a blank space
          print()                  # move to next line
          
def magic(m):
     '''2D list->bool
     Returns True if m forms a magic square
     Precondition: m is a matrix with at least 2 rows and 2 columns '''

     # this tests the condition that is implied by the definition
     # i.e. that m has to be a square matrix
     if(not(is_square(m))): # if matrix is not square
          return False      # return False

     # YOUR CODE GOES HERE
     sumr = []
     sumc = []
     diagr = 0
     diagl = 0
     for row in range(len(m)):
          sum_r = 0
          for col in range(len (m[0])):
               sum_r += m[row][col]
          sumr.append(sum_r)
     
     for j in range(len(m)):
          sum_c = 0
          for i in range(len(m[0])):
               sum_c += m[i][j]
          sumc.append(sum_c)

     
     for a in range(len(m)):
          diagr += m[a][a]

     for b in range(len(m)):
          diagl+=m[b][abs(len(m)-b-1)]
          
     print_matrix(m)
##     print(len(m))
     print(sumr)
##     print(sumc)
##     print(diagr)
##     print(diagl)

     for x in sumr:
          if x!= sumr[0]:
               print('a')
               return False

     for y in sumc:
          if y!= sumc[0]:
               print('b')
               return False

     for e in range(len(m)):
          for f in range(len(m[0])):
               for g in range(e):
                    for h in range(f):
                         if m[e][f] == m[g][h]:
                              return False
     
     if sumr[0] == sumc[0] and sumc[0] == diagr and diagr == diagl:
          return True
     




# main
# TESTING OF magic functions

# this should print True

m0=[[2,7, 6],[9,5,1],[4,3,8]]
print(magic(m0))
    
# this should print True
m1 = [[16,3,2,13], [5,10,11,8],[9,6,7,12], [4,15,14,1]]
print(magic(m1))
    
# this should print False. Why? Which condition imposed on magic squares is not true for m3
m2 = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16]]
print(magic(m2))
    
#this should print False. Why? Which condition imposed on magic squares is not true for m3
m3 =  [[1,1],[1,1]]
print(magic(m3))

# #this should print False. Why? Which condition imposed on magic squares is not 
m3 =  [[1,1],[1,1],[1,2]]
print(magic(m3))
