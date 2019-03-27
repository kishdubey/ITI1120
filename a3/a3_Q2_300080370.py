def two_length_run(l):
    '''
    (list of numbers)->boolean
    The function returns True if there are numbers in a given list has at least one run (of length at least two), and False otherwise.
    '''
    for i in range(len(l)-1):
            if l[i] == l[i+1]:
                return True
    return False
    

if __name__ == "__main__":
    user_input = input("Please input a list of numbers separated by space: ").strip().split()
    user_list = []

    for i in range(len(user_input)):
        user_list.append(float(user_input[i]))

    print((two_length_run(user_list)))



