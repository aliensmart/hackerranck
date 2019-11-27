import sys
n = int(input(""))

phone_book = {}

for i in range(n):
    user = input()
    try:
        entry = user.split(' ')
        if entry:

            phone_book[entry[0]] = entry[1]
    except:
        h = 1
    
    


for i in range(n):
    query = input()
    phone_number = phone_book.get(query)
    if phone_number:
        print(query + "=" + phone_number)
    else:
        print("Not found")