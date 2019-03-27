def split_tester(N, d):
    '''
    (string, string)->boolean
    The function takes as input a number N, and the number of digits of seperation in that number, breaks down the number by that seperation and outputs either True or False on whether the sequeunce is increasing or not.
    Precondition: N and d are positive integers inputted as strings
    '''
    substring = ""
    temp = 0
    val = True

    for i in range(0, len(N), int(d)):
        substring+=N[i:int(d)+i]+", "
        if(temp > int(N[(i):int(d)+(i)])):
            val = False
        temp = int(N[(i):int(d)+(i)])

    if(N == d):
        print(N)
    else:
        print(substring[:-2])
    return val
          
def ascii_name_plaque(name):
    '''
    (string)->none
    The function displays a plaque surrounding the string input given. The plaques are shown by printing * multiple times creating a pattern.
    '''
    stars = ("*")*len(name)
    blank = (" ")*len(name)
    print("******"+stars+"******")
    print("*     "+blank+"     *")
    print("*     "+name+"     *")
    print("*     "+blank+"     *")
    print("******"+stars+"******")

            
if __name__ == "__main__":
    ascii_name_plaque("Welcome to my increasing splits tester")
    name = input("What is your name? \t")
    ascii_name_plaque(name+", "+"Welcome to my increasing splits tester")

    flag = True
    while flag:
        question= input(name+", would you like to test if a number admits an increasing-split of given size? ")
        question=(question.strip()).lower()
        
        if question=='no':
            flag = False 
            
        elif question =='yes':
            print("Good Choice!")
            N = input("Enter a positive integer: ")

            if N[0]=="-" or (N[0]=="0" and len(N) == 1):
                print("The input has to be a positive integer.Try again.")
                flag = True

            elif not(N.isdigit()):
                print("The input can only contain digits. Try again.")
                flag = True
            
            else:
                d = input("Input the split. The split has to divide the length of "+N+" "+"i.e "+str(len(N))+"\n")
                if not(len(N)%int(d)) == 0:
                    print(d+" does not divide "+str(len(N))+". Try again.")
                    flag = True
                else:
                    if split_tester(N, d):
                        print("The sequence is increasing")
                    else:
                        print("The sequence is not increasing")
        else:
            print("Please enter yes or no. Try again.")
            flag = True
    ascii_name_plaque("Good bye "+name)
