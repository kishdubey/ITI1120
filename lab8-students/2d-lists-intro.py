# one way to create a 2D list that represents a 10x10 matrix filled with ones.

m=[] # creates an empty list
for i in range(10):
     l=[1]*10 #creatats a list of 10 ones
     m.append(l)



#printing elements of a 2D lists m by looping over elements

for item in m:
     for x in item:
          print(x,  end=" ")
     print()

print("\n\n\n\n")
print("printing again \n")
# printing elements of a 2D lists m by looping over indices

for i in range(len(m)):
     for j in range(len(m[i])):
          print(m[i][j], end=" ")
     print()



     




