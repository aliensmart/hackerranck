# https://www.hackerrank.com/challenges/finding-the-percentage/problem

def find_percentage():
    n = int(input("Enter number of record to use: "))
    student_marks = {}
    for _ in range(n):
        # splitting the input data by the space
        # then retreving the first value to store in name
        # and the rest will be the list of number for line variable
        name, *line = input('Enter name and scores separated with spaces: ').split()
        
        # we will convert all string input into float using map function
        # then store the values in a new list
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input("Name of the query: ")
    result = "{:.2f}".format(sum(student_marks[query_name])/len(student_marks[query_name]))
    print(result)

if __name__ == '__main__':
    find_percentage()