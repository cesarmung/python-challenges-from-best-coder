user_name = input("What is your name? ")

print("Hello ", user_name, ". Welcome to the Python Pizza chooser.", sep='')
pizza_type = input("Would you like to order a cheese pizza, a pepperoni pizza, or a supreme pizza? ")

while (pizza_type.lower() != 'cheese' and pizza_type.lower() != 'pepperoni' and pizza_type.lower() != 'supreme'):
    pizza_type = input("You may choose to order a cheese, pepperoni, or supreme pizza only. Please choose again. ")

number_pizzas = 0
user_decision = 'yes'

while (user_decision.lower() == 'yes'):
    if pizza_type.lower() == 'cheese':
        number_pizzas += 1

    elif pizza_type.lower() == 'pepperoni':
        number_pizzas += 1

    elif pizza_type.lower() == 'supreme':
        number_pizzas += 1
    
    else:
        pizza_type = input("You may choose to order a cheese, pepperoni, or supreme pizza only. Please choose again. ")
    
    user_decision = input("Would you like to order another pizza?(yes/no) ")

    if user_decision.lower() == 'yes':
        pizza_type = input("Would you like to order a cheese pizza, a pepperoni pizza, or a supreme pizza? ")

print("Thank you ", user_name, ". The ", number_pizzas, " pizzas you ordered will be ready in 30 minutes.", sep='')