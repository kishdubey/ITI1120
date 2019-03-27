def count_pos(l):
    '''
    (list of numbers)->integer
    The function returns the number of elements in the given list that are positive.
    '''
    counter=0
    for i in range(len(l)):
        if l[i]>0:
            counter+=1
    return counter

if __name__ == "__main__":
    user_input = input("Please input a list of numbers separated by space: ").strip().split()
    user_list = []

    for i in range(len(user_input)):
        user_list.append(float(user_input[i]))

    print("There are "+str(count_pos(user_list))+" positive numbers in your list")
