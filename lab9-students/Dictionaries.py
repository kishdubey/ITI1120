#Ex 1
def letter2number(lgrade):
    grade_dict={10:"A+", 9:"A", 8:"A-", 7:"B+", 6:"B", 5:"C+"} 
    return grade_dict[lgrade]

#Ex 2
def gov():
    gov_dict = {"CCC":"Civilian Conservation Corps", "FCC":"Federal Communications Commision",
                "FDIC":"Federal Deposit Insruance Corporation", "SSB":"Social Security Board", "WPA":"Work Progress Administration"
                }

    gov_dict["SEC"]="Securities and Exchange Commision"
    gov_dict["SSB"]="Social Security Administration"
    gov_dict.pop("CCC")
    gov_dict.pop("WPA")

    print(gov_dict)

#Ex 3
def lookup(d):
    first = input("Enter First Name ")
    last = input("Enter Last Name ")

    try:
        return d[first, last]
    except:
        print("Name not in phonebook")

#Ex 4 (6.15)
def lookup_mod():
    phone_book = {("Hon", "A") = [12344, 13414]}

#Ex 5
def reverse(d):
    reverse = {}
    for key in d:
        reverse[d[key]]=key

    return reverse

#Prog Ex 0
def get_year():
    val = True
    while(val):
        try:
            num = int(input("Please Enter 4 Digit Integer for Year: "))
            val = False
        except ValueError:
            print("Enter 4-Digit Integer Pls")
    return num





