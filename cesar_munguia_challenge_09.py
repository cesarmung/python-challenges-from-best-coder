def main():
    Menu()


def Menu():
    user_choice = input("Do you want to add a new student to the gradebook? (yes/no) ")
    keep_going = 'yes'

    while keep_going.lower() == 'yes':
        if user_choice.lower() == 'yes':
            AddStudent()

            keep_going = input("Do you want to add another student? (yes/no) ")

            if keep_going.lower() == 'no':
                print("Goodbye!")

        else:
            print("Goodbye!")
            keep_going = 'no'


def AddStudent():
    MAX_NUM_GRADES = 3
    grades_list = []

    student_name = input("Please enter the name of the new student: ")

    for grade in range(MAX_NUM_GRADES):
        grade = input(f'Enter grade {grade +1}: ')

        grades_list.append(grade)
    
    StudentGradeBook(student_name, grades_list)


grade_book = {}
def StudentGradeBook(student_name, grades):
    grade_book[student_name] = grades

    print(grade_book)
    

if __name__ == '__main__':
    main()