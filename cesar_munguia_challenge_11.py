import random

class Humanoid:
    def __init__(self, height, weight, hair_color, eye_color):
        self.__height = height
        self.__weight = weight
        self.__hair_color = hair_color
        self.__eye_color = eye_color
    
    
    def set_height(self, height):
        self.__height = height
    
    def set_weight(self, weight):
        self.__weight = weight

    def set_hair_color(self, hair_color):
       self.__hair_color = hair_color

    def set_eye_color(self, eye_color):
         self.__eye_color = eye_color
        
    def get_height(self):
        return self.__height
    
    def get_weight(self):
        return self.__weight
    
    def get_hair_color(self):
        return self.__hair_color
    
    def get_eye_color(self):
        return self.__eye_color


class Humans(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color):
        Humanoid.__init__(self, height, weight, hair_color, eye_color)



class Elves(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color):
        Humanoid.__init__(self, height, weight, hair_color, eye_color)


class Dwarves(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color):
        Humanoid.__init__(self, height, weight, hair_color, eye_color)


def characterCreation():
    strength = random.randint(1, 18)
    dexterity = random.randint(1, 18)
    constitution = random.randint(1, 18)
    intelligence = random.randint(1, 18)
    wisdom = random.randint(1, 18)
    charisma = random.randint(1, 18)

    user_character = input("Do you wish to be a human, elf, or dwarf?\n")
    character_height = input("Enter height [3ft - 7ft]:\n")
    character_weight = input("Enter weight [60lbs - 300lbs]:\n")
    character_hair_color = input("Enter hair color [Options: white, silver, gray, brown, green, blue, yellow, pink, red, blonde]:\n")
    character_eye_color = input("Enter eye color [Options: white, black, red, green, blue, brown, pruple, amber]:\n")

    if user_character == 'human':
        human = Humans(character_height, character_weight, character_hair_color, character_eye_color)
        human.set_height(character_height)
        human.set_weight(character_weight)
        human.set_hair_color(character_hair_color)
        human.set_eye_color(character_eye_color)

        height = human.get_height()
        weight = human.get_weight()
        hair_color = human.get_hair_color()
        eye_color = human.get_eye_color()

        print("You have the option to add 2 points to any attribute of your choice!")
        print("Options: strength, dexterity, constitution, intelligence, wisdom, charisma.")
        add_to_attribute = input("Enter the attribute you'd like to add the points to: ")

        if add_to_attribute == 'strength':
            strength += 2
        elif add_to_attribute == 'dexterity':
            dexterity += 2
        elif add_to_attribute == 'constitution':
            constitution += 2
        elif add_to_attribute == 'intelligence':
            intelligence += 2
        elif add_to_attribute == 'wisdom':
            wisdom += 2
        elif add_to_attribute == 'charisma':
            charisma += 2
        
        print(f'Your height: {height}ft.')
        print(f'Your weight: {weight}lbs.')
        print(f'Your hair color: {hair_color}.')
        print(f'Your eye color: {eye_color}.')

        print( )

        print(f'ATTRIBUTES (with {add_to_attribute} points added):')
        print("--------------------")
        print(f'Strength: {strength}.')
        print(f'Dexterity: {dexterity}.')
        print(f'Constitution: {constitution}.')
        print(f'Intelligence: {intelligence}.')
        print(f'Wisdom: {wisdom}.')
        print(f'Charisma: {charisma}.')


    elif user_character == 'elf':
        elf = Elves(character_height, character_weight, character_hair_color, character_eye_color)
        elf.set_height(character_height)
        elf.set_weight(character_weight)
        elf.set_hair_color(character_hair_color)
        elf.set_eye_color(character_eye_color)

        height = elf.get_height()
        weight = elf.get_weight()
        hair_color = elf.get_hair_color()
        eye_color = elf.get_eye_color()

        print("You have 100% Resistance to Sleep!")
        print("You gain +2 to your Dexterity and Charisma scores!")

        print("--------------------")

        print(f'Your height: {height}ft.')
        print(f'Your weight: {weight}lbs.')
        print(f'Your hair color: {hair_color}.')
        print(f'Your eye color: {eye_color}.')

        print( )

        print("ATTRIBUTES:")
        print("--------------------")
        print(f'Strength: {strength}.')
        print(f'Original dexterity: {dexterity} ---> New dexterity: {dexterity + 2}')
        print(f'Constitution: {constitution}.')
        print(f'Intelligence: {intelligence}.')
        print(f'Wisdom: {wisdom}.')
        print(f'Original charisma: {charisma} ---> New charisma: {charisma + 2}')
        

    elif user_character == 'dwarf':
        dwarf = Dwarves(character_height, character_weight, character_hair_color, character_eye_color)
        dwarf.set_height(character_height)
        dwarf.set_weight(character_weight)
        dwarf.set_hair_color(character_hair_color)
        dwarf.set_eye_color(character_eye_color)

        height = dwarf.get_height()
        weight = dwarf.get_weight()
        hair_color = dwarf.get_hair_color()
        eye_color = dwarf.get_eye_color()

        print("You have 20% Resistance to magic!")
        print("You gain +2 to your Strength and Constitution scores!")
        print("You also lose 2 points to your Charisma score :(")

        print("--------------------")

        print(f'Your height: {height}ft.')
        print(f'Your weight: {weight}lbs.')
        print(f'Your hair color: {hair_color}.')
        print(f'Your eye color: {eye_color}.')

        print( )

        print("ATTRIBUTES:")
        print("--------------------")
        print(f'Original strength: {strength} ---> New strength: {strength + 2}.')
        print(f'Dexterity: {dexterity}.')
        print(f'Original constitution: {constitution} ---> New constitution: {constitution + 2}.')
        print(f'Intelligence: {intelligence}.')
        print(f'Wisdom: {wisdom}.')
        print(f'Original charisma: {charisma} ---> New charisma: {charisma - 2}')



def main():
    characterCreation()


if __name__ == "__main__":
    main()