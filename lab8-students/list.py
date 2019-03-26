def create_books_2DList(file_name):
    text = open(file_name).read().splitlines()
    ny_table = []

    for t in text:
        t = t.split("\t")
        
        name = t[0].strip()
        
        author = t[1].strip()

        publisher = t[2].strip()

        date = t[3].strip()
        date = date.split("/")
        date_s = date[2]+"-"+date[0]+"-"+date[1]

        category = t[4].strip()

        ny_table.append([date_s, name, author, publisher, category])

    return ny_table

def search_by_year(books, y1, y2):
    print("All titles between "+str(y1)+" and "+str(y2)+" y2:")

    for row in range(len(books)):
            temp = books[row][0]
            temp.split("-")
            if int(temp[0])>=y1 and int(temp[0])<=y2:
                print(books[row][1]+", by "+books[row][2]+"("+books[row][0]+")")
                
file_name=input("Enter the name of the file: ")
file_name=file_name.strip()
my = create_books_2DList(file_name)
print(my)
search_by_year(my, 2005, 2005)


##    Each line in a file contains the information
##for a separate book, which includes: title, author, publisher, date it first reached
###1 on one of the best seller lists, and category (fiction or nonfiction).

