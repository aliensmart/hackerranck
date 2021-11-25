def second_low():
    marksheet = []
    for _ in range(0,int(input())):
        marksheet.append([input(), float(input())])
    
    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    # print(sorted(marksheet))
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
    
# second_low()

def secon_low():
    # Nested list containing the student name and score eg: [['Nami', 23.4], ['Killy', 4.5]]
    rank_list = [[input('Enter Student Name: '), float(input("Enter your Student Score: "))] for s in range(int(input("Enter number of student: ")))]
    # will store all scores as array then use set to remove duplicates then sorte them
    # and use the second element in the array as second lowest
    second_highest = sorted(list(set(record for name, record in rank_list)))[1]
    names_list = [name for name, rank in sorted(rank_list) if rank == second_highest]
    print('\n'.join(names_list))
    
    # print(names_list)
    
secon_low()