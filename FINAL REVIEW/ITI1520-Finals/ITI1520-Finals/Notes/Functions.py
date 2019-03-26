#Mershab Arafat
#Summary of Functions and Loops including useful ones

import random

def sum_elements(l):
    s = 0
    for i in l:
        s += i
    return s

def sum_indices(l):
    s = 0
    for i in range(len(l)):
        s+=l[i]
    return s

#SORTING ALGORITHM
#MUST KNOW THIS

def selection_sort(l):
    for i in range(len(l)):
        #assume the smallest # is the current number
        minIndex = i
        for j in range(i,len(l)):
            # If this number is smaller than our current smaller number, then this is the new smallest number
            if l[j] < l[minIndex]:
                minIndex = j

        #now that we know what the smallest number is, we replace the current number with the smallest number
        #unless the smallest number is the current number (then it wont change anything)
        if i != minIndex:
            buffer = l[i]
            l[i] = l[minIndex]
            l[minIndex] = buffer

    return l

#Find and return the minimum value/element in the array
def min_value(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min

#Find and return the maximum value/element in the array
def max_value(l):
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return max

#Find and return the index of the minimum value in the array
def min_index(l):
    min = 0
    for i in range(len(l)):
        if l[i] < l[min]:
            min = i
    return min

#SelectionSort algorithm using the minIndex
def selection_sort_v2(l):
    for i in range(len(l)):

        #Find the index of the minimum value in the array, but this value will be rescaled to the smaller array passed into the 'min_index' function.
        #That is why 'i' is added to scale this minimum index value to the scale of the entire list
        #if you do not understand this map out what this entire function does
        minIndex = min_index(l[i:]) + i

        #replacement algorithm from first selectionsort
        if i != minIndex:
            buffer = l[i]
            l[i] = l[minIndex]
            l[minIndex] = buffer
    return l

#average value in a list
def average(l):
    return sum_elements(l)/len(l)
