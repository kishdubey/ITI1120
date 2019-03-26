#Mershab Arafat
#Recursion with test cases

import random
import string

#Almost all recursive functions can be done using loops (usually while loops)

#Finding factorial using a for loop
def factorial_loops(n):
    s = 1
    for i in range(n+1):
        s*=n

#Recursively finding factorial
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)


#Sum of the digits in a number
#Example: 7982 -> 26
def sum_digits(n):
    if len(str(n)) == 1:
        return n
    else:
        return n%10 + sum_digits(n//10)

test = random.randint(10,1000000000)
print(test)
print(sum_digits(test))

print()

#Fibbionaci Sequence recursively done
def fibbionaci(n):
    if n==1:
        return n/(2*n+1)
    else:
        return n/(2*n+1) + fibbionaci(n-1)

print(fibbionaci(1))

print()

#Greatest Common divisor using Euclid's Algorithm recursively
def GCD(a,b):
    if b == 0:
        return a
    elif b==1:
        return b
    else:
        return GCD(b,a%b)

a = random.randint(0,100)
b = random.randint(0,100)
print("Greatest Common Denominator between " + str(a) + " and " + str(b) + ": ")
print(GCD(a,b))

print()

def is_palindrome(s):
    if len(s) == 1 or len(s) == 0:
        return True
    elif not s[0].isalpha():
        return is_palindrome(s[1:])
    elif not s[len(s)-1].isalpha():
        return is_palindrome(s[:len(s)-1])
    elif s[0].lower() == s[len(s)-1].lower():
        return is_palindrome(s[1:len(s)-1])
    elif s[0].lower() != s[len(s)-1].lower():
        return False

randomString = ''.join([random.choice(string.ascii_letters + string.digits + string.whitespace) for i in range(32) ])
print("Random String: ")
print(randomString)
print("Is it a palindrome?: ")
print(is_palindrome(randomString))

print()

print("True String: ")
print("A man, a plan, a canal -- Panama!")
print("Is it a palindrome?: ")
print(is_palindrome("A man, a plan, a canal -- Panama!"))
#Recursive sorting algorithm. log2 times faster than selectionSort
#Requires two functions, mergeSort and merge (found below)
def mergeSort(l):
    #base case:
    if len(l)< 2:
        return l
    #Recursive case
    else:
        middle = len(l)//2
        leftHalf = mergeSort(l[:middle])
        rightHalf = mergeSort(l[middle:])

        return merge(leftHalf,rightHalf)



#Merge the two unsorted lists
def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    outList = []

    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            outList.append(left[0])
            left.remove(left[0])
        else:
            outList.append(right[0])
            right.remove(right[0])

    while len(left) !=0:
        outList.append(left[0])
        left.remove(left[0])
    while len(right) != 0:
        outList.append(right[0])
        right.remove(right[0])

    return outList

print()

testList = [random.randint(0,99) for i in (range(10))]
print("Unsorted List:")
print(testList)
print("Sorted List:")
print(mergeSort(testList))

