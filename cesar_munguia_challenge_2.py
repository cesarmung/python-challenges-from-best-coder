name = input("Enter your name: ")
birth_Year = int(input("Enter your birth year: "))

current_Age = 2022 - birth_Year

print("Your name is " + name + 
". You were born in ", birth_Year,
". That makes you approximately ", current_Age,
" years old.", sep='')