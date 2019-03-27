def longest_run(l):
    '''
    (list of numbers)->integer
    The function returns the length of the longest run (sequence of repeated values) in a given list of numbers. 
    '''
    longest = None
    current = None
    longest_r = 0
    current_r = 0

    for i in range(len(l)):
            if current == l[i]:
                current_r = current_r+1
            else:
                current = l[i]
                current_r = 1
            if current_r > longest_r:
                longest_r = current_r
    return longest_r
        
if __name__ == "__main__":
    user_input = input("Please input a list of numbers separated by space: ").strip().split()
    user_list = []

    for i in range(len(user_input)):
        user_list.append(float(user_input[i]))

    print((longest_run(user_list)))
