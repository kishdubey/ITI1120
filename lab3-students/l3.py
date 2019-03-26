#Question 1
#############################################################################
def pay(hourly_wage, hours):
    '''
    (number, number)-> number
    The function returns the employees pay, after inputting the hours they worked, and the hourly_wage.
    
    Precondition: Inputs cannot be negative
    '''
    if(40<hours<=60):
        overtime=hours-40
        hours=hours-overtime
        return hours*hourly_wage+overtime*(1.5*hourly_wage)
    elif(hours>60): 
        overtime=hours-40
        hours = hours-overtime
        if(overtime>=20):
            dovertime = overtime-20
            dpay = dovertime*(2*hourly_wage)
            overtime = overtime-dovertime
            opay = overtime*(1.5*hourly_wage)
            odpay = dpay+opay
        return hours*hourly_wage+odpay
    else: return hours*hourly_wage

#############################################################################
#Question 2
def rps(choice_P1, choice_P2):
    '''
    (character, character) -> integer
    The function returns the result of the rps game, -1 if player 1 wins, or 1 if player  wins, or 0 if tie

    Precondition: Input has to be either 'R', 'P', or ‘S'
    '''
    if(choice_P1 == choice_P2):
        return 0
    elif(choice_P1 == 'R' and choice_P2 == 'S'):
        return -1
    elif(choice_P1 == 'S' and choice_P2 == 'R'):
        return 1
    elif(choice_P1 == 'S' and choice_P2 == 'P'):
        return -1
    elif(choice_P1 == 'P' and choice_P2 == 'S'):
        return 1
    elif(choice_P1 == 'P' and choice_P2 == 'R'):
        return -1
    elif(choice_P1 == 'R' and choice_P2 == 'P'):
        return 1
    
    
    
    
    
    
    


    

