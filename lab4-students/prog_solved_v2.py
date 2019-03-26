def is_eligible(age, citizenship, prison):
     return ((age>=18) and ((citizenship.lower().strip()==("canadian")) or (citizenship.lower()== ("canada"))) and (prison.lower()==("no")))
     
def call_is_eligibible():
     name=input("What is your name? ")
     age= int(input("How old are you? "))
     citizenship = input("What is your country of citizenship? ")
     prison = input("Are you currently in prison? Answer with \"yes\" or \"no\". ")

     if is_eligible(age, citizenship, prison):
          print(name, ", you are eligible to vote")
     else:
          print(name, ", you are ineligible to vote") 
    
def mess(phrase):
     acc=''
     for char in phrase:
          if char in "rstvwxyz":
               acc = acc + char.upper()
               #phrase = phrase.replace(char, char.upper())
          elif char in " ":
               acc = acc + "-"
               #phrase = phrase.replace(char, "-")
          else:
               acc = acc + char
     return acc

def pyramid(num, symbol):
     for i in range(1, num+1):
          print(symbol*i)

def full_pyramid(num, symbol):
     half = 9
     for i in range(1, num, 2):
          print((" "*(half))+(symbol*i))
          half-=1

def divisors(num):
     for i in range(1, num+1):
          if (num%i==0):
               print(i)

def prime(num):
     if num>=2:
          for i in range (2, num+1):
               if (num%i==0):
                    print(str(num)+" is not Prime")
                    break
               else:
                    print(str(num)+" is Prime")
                    break
     else:
          print("Not Prime")
'''
def primee(num):
     if num>=2:
          for i in range (2, num+1):
               if (num%i==0):
                    return False
     return True
                    #break
               else:
                    return True
                    break
 '''              
def prime_smaller(num):
     for x in range (num+1):
         if primee(x)==True:
              print(x)

               
     

          
     
     




     
