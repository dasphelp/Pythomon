# Daniel Phelps
# Assignment 10.1: Your Own Class
# Create a class to model Pokemon.

# ACKNOWLEDGEMENTS
# I used the Pokemon Chimchar's base statistics from the website 'Pokemon Database' https://pokemondb.net/pokedex/chimchar as a model for the base stats of my Pokemon. 
# I borrowed the abstraction of mechanisms that are present in the Pokemon video games, but I did not borrow any of the actual programming logic behind them for this project.
# For example, I know that in the games, Fire moves do extra damage against Grass pokemon, but I came up with how to impement this and other mechanisms like this into code on my own.

# Import random for rng in stat and damage calculators.
import random

# Import time to create natural pauses in terminal experience.
import time

# This class models Pokemon with their states and behaviors as featured in the Pokemon videogames.
class Pokemon():

    # Stores battle moves that are specific to each Pokemon type.
    # Can be accessed by all objects of class 'Pokemon'.
    move_dictionary = {"Grass":["Vine Whip","Pound"], "Fire":["Ember","Tackle"], "Water":["Bubble","Scratch"]}

    # Initialize variables.
    # Takes str 'type' (Pokemon type), str 'species' (species of Pokemon), and str 'nickname' (nickname given to Pokemon) as inputs.
    # If no inputs are given, an object containing a random Pokemon is created.
    def __init__(self, type=None,species=None, nickname=None):
        # Stores Pokemon by type.
        self.__pokemon_dictionary = {"Grass":["Turtwig","Budew","Shaymin","Tangela","Leafeon"],"Fire":["Chimchar","Slugma","Houndour","Vulpix","Flareon"],"Water":["Piplup","Buizel","Seel","Psyduck","Vaporeon"]}
        # Creates an object containing a Pokemon with a random type if no type is inputted.
        # Stores type into '__type'.
        if type == None:
            self.__type = list(self.__pokemon_dictionary.keys())[random.randint(0,2)]
        else:
            self.__type = type
        # Creates an object containing a Pokemon with a random species if no species is inputted.
        # Stores species into '__species'.
        if species == None:
            self.__species = self.__pokemon_dictionary[self.__type][random.randint(0,2)]
        else:
            self.__species = self.__pokemon_dictionary[self.__type][self.__pokemon_dictionary[self.__type].index(species)]
        # '__level' represents a Pokemon's level, an indicator of their abilites. As "__level" increases, so do the rest of the Pokemon's stats.
        self.__level = 5
        # '__hp' represents a Pokemon's HP, or hit points.
        self.__hp = random.randint(42,48)
        # '__temp_hp' keeps track of a Pokemon's hit points as it battles.
        self.__temp_hp = self.__hp
        # '__attack' is a Pokemon's attack power. It is used in damage calculations during battles.
        self.__attack = random.randint(55,62)
        # '__defense' is a Pokemon's defense power. It is used in damage calculations during battles.
        self.__defense = random.randint(42,46)
        # '__nickname' is the nickname the user can give to their pokemon.
        self.__nickname = nickname
        # '__experience' represents a Pokemon's experience. Experience is gained from winnning battles, and when a Pokemon's experience reaches a certain point, they can level up.
        self.__experience = 0
        # '__experience_cap' is the point that '__experience' has to reach for a Pokemon to level up.
        self.__experience_cap = self.__level * 10


    # Get-Set Methods

    # Returns '__nickname'.
    def get_nickname(self):
        return self.__nickname
    # Takes str 'nickname' (nickname given to Pokemon) as input.
    # Reassigns the variables '__nickname', setting the nickname for a pokemon.
    def set_nickname(self, nickname):
        self.__nickname = nickname
        self.__init__(self.__type,self.__species,self.__nickname)

    # Returns '__hp'.
    def get_hp(self):
        return self.__hp
    # Takes str 'hp' (HP given to a pokemon) as input.
    # Converts 'hp' into an int and assigns it to '__hp'.
    def set_hp(self, hp):
        self.__hp = int(hp)


    # Just some get methods

    # Returns '__pokemon_dictionary'.
    def get_pokemon_dictionary(self):
        return self.__pokemon_dictionary
    # Returns '__species'.
    def get_species(self):
        return self.__species
    # Returns '__type'.
    def get_type(self):
        return self.__type
    # Returns '__attack'.
    def get_attack(self):
        return self.__attack
    # Returns '__defense'.
    def get_defense(self):
        return self.__defense
    # Returns 'stats', which is a string listing the Pokemon's name as well as their stats.
    def get_stats(self):
        stats = f"{self.__nickname}'s Stats:\nLevel: {self.__level}\nHP: {self.__hp}\nAttack: {self.__attack}\nDefense: {self.__defense}"
        return stats


    # If '__experience' has reached '__experience_cap', '__level_up' is called and '__experience' is reset to its overlap of '__experience_cap'.
    def __check_experience(self):
        if self.__experience >= self.__experience_cap:
            self.__level_up()
            self.__experience = self.__experience_cap - self.__experience
            return True
        else:
            return False

    # Increases the Pokemon's level, '__level', by 1, and updates the rest of the Pokemon's stats by a number between 0 and 3.
    def __level_up(self):
        self.__level += 1
        self.__hp += random.randint(0,3)
        self.__attack += random.randint(0,3)
        self.__defense += random.randint(0,3)
        print(f"{self.__nickname} has now leveled up to level {self.__level}!\n{self.get_stats()}")

    # Initiate battle between user's Pokemon and another random Pokemon.
    def wild_encounter(self):
        # Create object '__foe' as private variable containing an implementation of Pokemon class with a random Pokemon.
        self.__foe = Pokemon()
        species = self.__foe.get_species()

        print(f"You have found a wild {species} with {self.__foe.get_hp()} HP!")
        time.sleep(.5)

        print(f"Go {self.__nickname}!")

        # Reset user's Pokemon's hitpoints.
        self.__temp_hp = self.__hp

        # Cycle between the user's turn and the opponent's turn until either the user's Pokemon's or the foe Pokemon's hitpoints reaches 0.
        while self.__foe.get_hp() > 0 and self.__temp_hp > 0:
            # User's turn.
            self.__my_attack(species)
            print("")
            # Break cycle if one of the Pokemon has run out of hit points.
            if self.__foe.get_hp() == 0 or self.__temp_hp == 0:
                break
            time.sleep(2)
            # Opponents turn.
            self.__foe_attack(species)
        time.sleep(1)

        # User wins battle if foe Pokemon runs out of hitpoints first.
        if self.__foe.get_hp() == 0:
            # Calculates earned experience based on the level of the defeated Pokemon.
            experience = self.__foe.__level * 4
            experience += random.randint(-3,3)
            # Adds the earned experience to '__experience'.
            self.__experience += experience
            print(f"The wild {species} has fainted. {self.__nickname} has earned {experience} points of experience!")
            time.sleep(1)
            # Runs '__check_experience' to check if the user's Pokemon can level up.
            if self.__check_experience():
                pass
            else:
                print(f"{self.__experience_cap - self.__experience} points remaining to level up.")
        else:
            # Print losing message if user's Pokemon runs out of hitpoints first.
            print("Your pokemon has fainted!")
            time.sleep(1)
            print("You used a potion to restore its health.")
        print("")
        # Reset '__temp_hp' for next battle.
        self.__temp_hp = self.__hp

    # User's turn during battle.
    # Takes str 'species' (species of user's Pokemon) as input.
    def __my_attack(self,species):
        # Gets moves available to user's Pokemon.
        move1 = self.move_dictionary[self.__type][0]
        move2 = self.move_dictionary[self.__type][1]
        # Get move option display.
        movebox = self.__get_movebox(move1, move2)
        time.sleep(.5)

        # Display move display.
        print(f"Use a move against the wild {species}!\n{movebox}")

        # Get attack from user and assign it to attack.
        while True:
            attack = input("||/")
            # Make sure the user enters a move.
            if attack in self.move_dictionary[self.__type]:
                break
            else:
                print("You did not enter your move in correctly. Please try again.")
        
        print(f"{self.__nickname} used {attack} against the wild {species}!")
        
        # Calculate damage.
        # If the attack is a type attack, special damage is factored into the calculations.
        if attack in ["Vine Whip","Ember","Bubble"]:
            special, message = self.__compare_types(self.get_type(),self.__foe.get_type())
            damage = round((special + self.__attack - self.__foe.get_defense()) / 2.5)
        elif attack in ["Pound","Tackle","Scratch"]:
            damage = round((40 + self.__attack - self.__foe.get_defense()) / 2.5)
            message = ""
        
        # Apply damage to foe Pokemon's hitpoints.
        foe_hp = self.__foe.get_hp() - damage
        if foe_hp > 0:
            self.__foe.set_hp(foe_hp)
        else: 
            self.__foe.set_hp(0)
        time.sleep(1)

        print(f"The wild {species} is hit with {damage} damage!")
        time.sleep(1)
        if message != "":
            print(message)
            time.sleep(1)

        print(f"The wild {species} now has {self.__foe.get_hp()} HP!")

    # Foe's turn during battle.
    # Takes str 'species' (species of user's Pokemon) as input.
    def __foe_attack(self,species):
        # Finds random attack for the foe Pokemon to use (within their type).
        attack = self.move_dictionary[self.__foe.__type][random.randint(0,1)]

        print(f"The wild {species} used {attack} against {self.__nickname}!")
        
        # Calculate damage.
        # If the attack is a type attack, special damage is factored into the calculations.        
        if attack in ["Vine Whip","Ember","Bubble"]:
            special, message = self.__compare_types(self.__foe.get_type(),self.get_type())
            damage = round((special + self.__foe.get_attack() - self.__defense) / 2.5)
        else:
            damage = round((40 + self.__foe.get_attack() - self.__defense) / 2.5)
            message = ""

        # Apply damage to the user's Pokemon's hitpoints.
        my_hp = self.__temp_hp - damage
        if my_hp > 0:
            self.__temp_hp = my_hp
        else:
            self.__temp_hp = 0
        time.sleep(1)

        print(f"{self.__nickname} is hit with {damage} damage!")
        time.sleep(1)
        if message != "":
            print(message)
            time.sleep(1)
        
        print(f"{self.__nickname} now has {self.__temp_hp} HP!")

    # Creates string display for available moves in battle.
    # Takes strs 'move1' and 'move2' (moves available to user's Pokemon) as inputs.
    # Returns 'movebox' (formatted display containing available moves in battle) as output.
    def __get_movebox(self, move1, move2):
        movebox = f"{move1}{move2}"
        length = len(movebox) + 5
        movebox = ""
        for i in range(length):
            movebox += "-"
        movebox += f"\n|{move1} | {move2}|\n"
        for i in range(length):
            movebox += "-"
        return movebox

    # Calculates damage difference based on Pokemons' type difference in battle.
    # Takes strs 'type1' (the type of the attacking Pokemon) and 'type2' (the type of the defending Pokemon) as inputs.
    # Returns int 'special' (special damage) and str 'message' (effectiveness of attack) as outputs. 
    def __compare_types(self, type1, type2):
        types = [type1, type2]
        # Converts types into numbers to be mathematically compared.
        for i in range(len(types)):
            if types[i] == "Grass":
                types[i] = 0
            elif types[i] == "Fire":
                types[i] = 1
            elif types[i] == "Water":
                types[i] = 2
        
        dif = types[0] - types[1] 
        
        # Calculates special damage based on 'dif'
        if dif == 2:
            special = 20
        elif dif == 1:
            special = 80
        elif dif == 0:
            special = 20
        elif dif == -1:
            special = 20
        elif dif == -2:
            special = 80

        # Assigns message according to attack effectiveness.   
        if special == 20:
            message = "It was not very effective."
        else:
            message = "It was super effective!"

        return special, message
        

def main():
    # Grabs the private data attribute '__pokemon_dictionary' from 'Pokemon' class using the method 'get_pokemon_dictionary' in the class
    pokemon_dictionary = Pokemon().get_pokemon_dictionary()
    input("Welcome to Pythomon! Enter any character on your keyboard to begin! ")
    time.sleep(1)
    print("In the world of Pythomon, you get to select a Pokemon companion and watch it grow as you battle with it against other pokemon.")
    time.sleep(4)
    print("You will begin by getting to choose your own!")
    time.sleep(2)
    # Get arguments to create 'Pokemon' object from user.
    while True:
        types = "What type of Pokemon will you choose? "
        for i in range(len(pokemon_dictionary)):
            if i == (len(pokemon_dictionary)-1):
                types += f"or {list(pokemon_dictionary.keys())[i]}?"
            else:
                types += f"{list(pokemon_dictionary.keys())[i]}, "
        print(types)
        type = input("||/")
        if type in pokemon_dictionary:
            break
        else:
            print("You did not enter the type in correctly. Please try again. (Enter the name of the type as it is spelled above with capitals.)")
            time.sleep(1)
    while True:
        pokemon =f"{type} Pokemon: "
        for j in range(len(pokemon_dictionary[type])):
            if j == (len(pokemon_dictionary[type]) - 1):
                pokemon += f"and {pokemon_dictionary[type][j]}."
            else:
                pokemon += f"{pokemon_dictionary[type][j]}, "
        print(pokemon)
        time.sleep(2)
        print("Who will be your companion?")
        species = input("||/")
        if species in pokemon_dictionary[type]:
            break
        else:
            print("You did not enter the Pokemon's name in correctly. Please try again. (Enter the Pokemon's name as it is spelled above with capitals.)")
            time.sleep(1)
    time.sleep(1)
    print(f"Congratulations! You and {species} are now companions! Give a nickname to your Pokemon!")
    nickname = input("||/")
    # Create object 'starter' from class 'Pokemon' using data gathered from user.
    starter = Pokemon(type, species, nickname)
    print("Now that you have found a companion, you can interact with the world of Pythomon...")
    time.sleep(3)
    while True:
        actions = f"Actions available:\nBattle: Challenge a Pokemon in the wild to gain experience!\nEat Vitamins: Give your Pokemon more or fewer hitpoints!\nCheck Stats: Check {nickname}'s stats!\nRename: Give your Pokemon a new nickname!\nHelp: Review the list of commands.\nExit: Exit the game."
        print(actions)
        command = input("||/")
        # If user types 'Battle' into the shell, 'wild_encounter' method is run from 'Pokemon' class to start the battle.
        if command == "Battle":
            starter.wild_encounter()
            time.sleep(2)
        # If user types 'Eat Vitamins' into the shell, 'set_hp' method is run from 'Pokemon' class to change the hitpoints of the Pokemon.
        elif command == "Eat Vitamins":
            # Use 'get_hp' method from 'Pokemon class' to get the private variable '__hp' from the class. 
            print(f"{nickname} currently has {starter.get_hp()} hitpoints.")
            time.sleep(1)
            print(f"How many hitpoints do you want {nickname} to have?")
            time.sleep(1)
            # Gathers data needed for 'set_hp'.
            hp = input("||/")
            time.sleep(1)
            # Runs class method.
            starter.set_hp(hp)
            # Uses 'get_hp' again to confirm the change.
            print(f"{nickname} now has {starter.get_hp()} hitpoints.")
            time.sleep(1)
        # If user types 'Check Stats' into the shell, 'get_stats' method is run from 'Pokemon' class to get the Pokemon's stats and print them.
        elif command == "Check Stats":
            # Runs class method and prints its return value.
            print(starter.get_stats())
            time.sleep(4)
        # If user types 'Rename' into the shell, 'set_nickname' method is run from 'Pokemon' class to change the Pokemon's nickname.
        elif command == "Rename":
            print(f"What would you like to rename your {species} as?")
            # Gathers data needed for 'set_nickname'.
            nickname = input("||/")
            # Runs class method.
            starter.set_nickname(nickname)
            # Uses 'get_nickname' from 'Pokemon' class to confirm the change.
            print(f"You have renamed your {species} {starter.get_nickname()}!")
            time.sleep(1)
        elif command == "Help":
            continue
        elif command == "Exit":
            print("Thank you for playing!")
            break
        else:
            print("You did not enter your command in correctly. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()