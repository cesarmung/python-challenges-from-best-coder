play = input("Do you wish to play?(yes/no) ")
user_number = 0
GUESS_NUMBER = 30

if play == 'yes':
    user_number = int(input("Choose a number from 1 - 50. "))
    if user_number == GUESS_NUMBER:
        print("Congratulations. You guessed the correct number")
    
    elif user_number == (GUESS_NUMBER - 5) or user_number == (GUESS_NUMBER + 5):
        print("You were within 5 numbers of the correct value")
    
    else:
        print("That is not the correct number")
else:
    print("Goodbye, ending the program...")
