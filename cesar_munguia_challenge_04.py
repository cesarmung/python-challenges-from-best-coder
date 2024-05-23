play = input("Do you wish to play?(yes/no) ")
user_number = 0
GUESS_NUMBER = 41
user_attempts = 0

if play == 'yes':
    user_number = int(input("Choose a number from 1 to 50. "))

    while (user_number > 50 or user_number < 1):
        user_number = int(input("ERROR: Please pick a number from 1 to 50 only: "))
        user_attempts += 1
        
    keep_going = 'y'

    while(keep_going == 'y'):
        if user_number == GUESS_NUMBER:
            print("Congratulations! You guessed the correct number.")
            user_attempts += 1
            print("Attempts: ", user_attempts)
            keep_going = 'n'

        elif ((user_number >= 36 and user_number <=40) or (user_number >= 42 and user_number <= 46)):
            user_number = int(input("Your guess is within 5 digits of the correct number. Please try again. "))
            user_attempts += 1
            keep_going = 'y'

        else:
            user_number = int(input("That is not the correct number, try again. "))
            user_attempts += 1  
            keep_going = 'y'      
else:
    print("Goodbye, ending the program...")

