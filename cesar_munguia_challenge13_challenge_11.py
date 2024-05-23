import re

def main():

    keep_going = 'y'
    while keep_going == 'y':
        phone_number = input("Enter a phone number with the following format -> [XXX-XXX-XXXX]\n")

        match = re.search(r"([0-9])([0-9])([0-9])(\-)([0-9])([0-9])([0-9])(\-)([0-9])([0-9])([0-9])([0-9])", phone_number)

        if match:
            print("Valid phone number")

            keep_going = input("Would you like to enter a new phone number? [y/n]\n")
        else: 
            print("Invalid phone number") 

            keep_going = input("Would you like to enter a new phone number? [y/n]\n")

    print("Goodbye! :)")


if __name__ == "__main__":
    main()