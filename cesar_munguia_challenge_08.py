def main():
    getUserPass()

## converts tuple to a list
## appends the new password to list
def StoredPasswords(checkPass):

    commmon_passwords = ['123456', '123456789', '12345', 'qwerty', 'password', '12345678', '111111', '123123', '1234567890', '1234567',
                        'qwerty123', '000000', '1q2w3e', 'aa12345678', 'abc123', 'password1', '1234', 'qwertyuiop', '123321', 'password123',
                        '1q2w3e4r5t', 'iloveyou', '654321', '666666', '987654321', '123', '123456a', 'qwe123', '1q2w3e4r', '7777777',
                        '1qaz2wsx', '123qwe', 'zxcvbnm', '121212', 'asdasd', 'a123456', '555555', 'dragon', '112233', '123123123',
                        'monkey', '11111111', 'qazwsx', '159753', 'asdfghjkl', '222222', '1234qwer', 'qwerty1', '123654', '123abc']

    ##    if checkPass in commmon_passwords:
    #         index = commmon_passwords.index(checkPass)
    # 
    #         print(f'Your password was found at index {index} in the list of most commmon passwords.')
    #         print(f'The actual position of the password in the list is {index + 1}.')

    #         found = 'Your password is too common. Please consider changing it.'

    ##        return found

    ##    tuple_to_list = list(commmon_passwords)

    list_containing_new_password = commmon_passwords.append(checkPass)

    print("The new password has been appended to the new list of common passwords")
    print(commmon_passwords)


## this function checks whether the user's password meet the requirements
# and it allows the user to enter a password until the password is appropiate
def password_validation(password):

    ## initiliaze everything to False
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_character = False

    keep_going = 'y'
    while keep_going == 'y':
        ## checks whether the password is more than or equal to 8 characters
        if len(password) >= 8:
            correct_length = True

            ## checks whether the password:
            # - contains a lowercase letter
            # - contains a number
            # - contains a special character
            # - contains an uppercase letter
            for character in password:
                if character.isupper():
                    has_uppercase = True
                if character.islower():
                    has_lowercase = True
                if character.isdigit():
                    has_digit = True
                if ('!' in password) or ('@' in password) or ('%' in password) or ('^' in password) or ('&' in password) or ('*' in password) or ('(' in password) or (')' in password):
                    has_special_character = True
                    ## if it contains a restriscted special character
                    # let the user try again
                    if ('#' in password) or ('$' in password) or ('_' in password) or ('-' in password) or ('+' in password) or ('=' in password):
                        has_special_character = False

            keep_going = 'n'  
        else:
            print("Your password needs the following criteria: needs to be 8 characters long, at least have one number, at least have one lowercase character, at least have one uppercase character, at least have one special character [ !@%^&*() ], and cannot include the special characters [ #$_-+= ]")
            password = input("Please enter another password that meets the requirements: ")

            keep_going = 'y'            
        
        # checks whether all requirements are valid
        if correct_length == True and has_uppercase == True and has_lowercase == True and has_digit == True and has_special_character == True:
            valid_password = 'Your password meets the criteria.'

            keep_going = 'n'

            return valid_password
        else:
            print("Your password needs the following criteria: needs to be 8 characters long, at least have one number, at least have one lowercase character, at least have one uppercase character, at least have one special character [ !@%^&*() ], and cannot include the special characters [ #$_-+= ]")
            password = input("Please enter another password that meets the requirements: ")

            keep_going = 'y'


## gets input from user
## calls the functions used
def getUserPass():

    user_username = input("Create a username: ")

    user_password = str(input("Create a password: "))

    check_password_criteria = password_validation(user_password)
    print(check_password_criteria)

    StoredPasswords(user_password)


if __name__ == '__main__':
    main()