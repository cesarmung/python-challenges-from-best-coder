from EmployeeDatabase import companyRegistry


def main():
    Menu()


def Menu():
    user_choice = input("Would you like to see an employee's information? (yes/no)\n")
    keep_going = 'yes'

    while keep_going.lower() == 'yes':
        if user_choice.lower() == 'yes':
            employee_name = input("Enter the employee's name:\n")
            employee_field = input("Type the field you would like to look at: [Options: salary, job title, home address, or contact information.]\n")

            companyRegistry(employee_name, employee_field)

            keep_going = input("Would you like to see another employee's information? (yes/no) ")

            if keep_going.lower() == 'no':
                print("Goodbye!")

        else:
            print("Goodbye!")
            keep_going = 'no'
    

if __name__ == '__main__':
    main()