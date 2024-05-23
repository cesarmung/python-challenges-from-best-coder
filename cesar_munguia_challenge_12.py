def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n - 1))


def findPrime(n):
    if n > 1:
        for integer in range(2, n):
            if n % integer == 0:
                print("This is not a prime number")
                break
            else:
                print("This is a prime number")
                break


def printFactorial(n):
    number1 = []
    for number in range(n, 0, -1):
        number = str(number)
        number1.append(number)

    string = ' x '.join(number1)

    return string


def Menu():
    keep_going = 'y'

    while keep_going == 'y':
        number = int(input("Enter a nonnegative number:\n"))
        while (number <= 0):
            number = int(input("Enter a number greater than 0:\n"))
    
        user_choice = input("Would you like find the factorial or find out whether your number is prime? [Options: factorial, prime]\n")

        if user_choice == 'factorial':
            factorial_number = factorial(number)
            result = printFactorial(number)

            print(f'The factorial value of {number} is:')
            print(f'{factorial_number} ({result})')  

            keep_going = input("Would you like to enter a new number? (y/n)\n")

        elif user_choice == 'prime':
            findPrime(number)

            keep_going = input("Would you like to enter a new number? (y/n)\n")
    
    print("Goodbye! :)")
        
def main():
    Menu()


if __name__ == "__main__":
    main()