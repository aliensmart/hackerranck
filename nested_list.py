def second_low():
    student_number = int(input("Enter the numer of students: "))
    scores_list = []
    for s in range(student_number):
        name = input('student name: ')
        score = float(input("enter the student score"))
        scores_list.append([name, score])
    
    print(scores_list)
    
second_low()
        