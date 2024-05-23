class PlayerCharacter:
    
    def __init__(self, health, armor_rating, attack_power):
        self.__user_health = health
        self.__user_armor_rating = armor_rating
        self.__user_attack_power = attack_power
    
    def set_health(self, health):
        self.__user_health = health
    
    def set_armor_rating(self, armor_rating):
        self.__user_armor_rating = armor_rating

    def set_attack_power(self, attack_power):
        self.__user_attack_power = attack_power
    
    def get_health(self):
        return self.__user_health

    def get_armor_rating(self):
        return self.__user_armor_rating

    def get_attack_power(self):
        return self.__user_attack_power


def main():

    my_health = int(input("Enter your health (1 - 100): "))
    my_armor_rating = int(input("Enter your armor rating (1 - 20): "))
    my_attack_power = int(input("Enter your attack power (1 - 20): "))


    while ( (my_health < 1 or my_health > 100) or 
            (my_armor_rating < 1 or my_armor_rating > 20) or 
            (my_attack_power < 1 or my_attack_power > 20)):

        print("One or more of your values is not in the appropiate range please enter your values again.")

        my_health = int(input("Enter your health (1 - 100): "))
        my_armor_rating = int(input("Enter your armor rating (1 - 20): "))
        my_attack_power = int(input("Enter your attack power (1 - 20): "))

    wizard = PlayerCharacter(my_health, my_armor_rating, my_attack_power)

    wizard.set_health(my_health)
    wizard.set_armor_rating(my_armor_rating)
    wizard.set_attack_power(my_attack_power)

    wizard_health = wizard.get_health()
    print("HEALTH: ")
    print(wizard_health)

    wizard_armor_rating = wizard.get_armor_rating()
    print("ARMOR RATING: ")
    print(wizard_armor_rating)

    wizard_attack_power = wizard.get_attack_power()
    print("ATTACK POWER: ")
    print(wizard_attack_power)


if __name__ == "__main__":
    main()