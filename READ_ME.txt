Github Link
https://github.com/dasphelp/Pythomon

Documentation for Python script '10_1_your_own_class.py'
by Daniel Phelps


# ACKNOWLEDGEMENTS:
# Pokemon are intellectual property owned by The Pokemon Company.
# I used the Pokemon Chimchar's base statistics from the website 'Pokemon Database' https://pokemondb.net/pokedex/chimchar as a model for the base stats of my Pokemon. 
# I borrowed the abstraction of mechanisms that are present in the Pokemon video games, but I did not borrow any of the actual programming logic behind them for this project.
# For example, I know that in the games, Fire moves do extra damage against Grass pokemon, but I came up with how to impement this and other mechanisms like this into code on my own.


Class Documentation

Classes:
 -'Pokemon'
 --The 'Pokemon' class models Pokemon, fictional creatures originally created by Satoshi Tajiri. 
   These Pokemon have states and behaviors just like creatures in the real world, and many of the methods and attributes of the Pokemon class model their states and behaviors.
   The rest of the methods and variables aid the system to help interact with the Pokemon's data.
   Some of these methods include: battling, leveling up, and checking stats.
   Some of the attributes include: species, attack, defense, and experience.
	Class Attributes:
	 -'move_dictionary'
	   ---'move_dictionary' stores all of the moves available to Pokemon in battle as a dictionary.
	      The types of the moves are the keys of the dictionary, and the moves belonging to each type are the values of each key in lists.
	Data Attibutes (Private):
	 -'__pokemon_dictionary'
	   ---'__pokemon_dictionary' stores all the species of Pokemon available as a dictionary.
	      The types of Pokemon are the keys of the dictionary, and the Pokemon belonging to each type are the values of each key in lists.
	 -'__type'
	   ---'__type' stores the type of a Pokemon as a string.
	 -'__species'
	   ---'__species' stores the species of a Pokemon as a string.
	 -'__level'
	   ---'__level' stores the level of a Pokemon as an int. The level of a Pokemon is an indicator of its abilities.
	 -'__hp'
	   ---'__hp' stores the maximum hitpoints of a Pokemon as an int.
	 -'__temp_hp'
	   ---'__temp_hp' stores the hitpoints of a Pokemon during battle as an int. 
	 -'__attack'
	   ---'__attack' stores the attack power of a Pokemon as an int.
	 -'__defense'
	   ---'__defense' stores the defense power of a Pokemon as an int.
	 -'__nickname'
	   ---'__nickname' stores the nickname given to a Pokemon as a string.
	 -'__experience'
	   ---'__experience' stores the experience points of a Pokemon as an int.
	      A pokemon gains experience points after winning a battle, and once these points reach a certain number, the Pokemon levels up.
 	 -'__experience_cap'
	   ---'__experience_cap' stores the number that a Pokemon's experience must reach in order to level up as an int.
	Methods (NOTE: ALL CLASS METHODS TAKE IN SELF [OBJECT] AS FIRST ARGUMENT):
	 -'get_nickname'
	   ---'get_nickname' returns 'self.__nickname'.
	 -'set_nickname'
	   ---'set_nickname' renames the user's Pokemon.
	      It takes string argument 'nickname' (nickname to give to the Pokemon) as input.
	 -'get_hp'
	   ---'get_hp' returns 'self.__hp'.
	 -'set_hp'
	   ---'set_hp' takes int argument 'hp' as input.
	      It sets the Pokemon's HP stat to 'hp', a given number.
	 -'get_pokemon_dictionary'
	   ---'get_pokemon_dictionary' returns 'self.__pokemon_dictionary'.
	 -'get_species'
	   ---'get_species' returns 'self.__species'.
	 -'get_type'
	   ---'get_type' returns 'self.__type'.
	 -'get_attack'
	   ---'get_attack' returns 'self.__attack'.
	 -'get_defense'
	   ---'get_defense' returns 'self.__defense'.
	 -'get_stats'
	   ---'get_stats' creates a string compiling all of the Pokemon's stats and assigns it to the variable 'stats'.
	      'stats' is then returned.
	 -'__check_experience'
	   ---'__check_experience' checks if 'self.__experience' has reached 'self.__experience_cap'.
	      If it has, the Pokemon levels up, its experience is reset, and the method returns boolean value 'True'.
	      Otherwise, the method returns boolean value 'False'.
	 -'__level_up'
	   ---'__level_up' raises the Pokemon's level by 1 and increases all of its stats.
	 -'wild_encounter'
	   ---'wild_encounter' initiates a battle between the user's Pokemon and a random Pokemon.
	      The method also prints a win/lose statement and updates the user's Pokemon's experience after a win.
	 -'__my_attack'
	   ---'__my_attack' takes the string argument 'species' (the species of the user's Pokemon) as input.
	      It runs the user's turn in battle, requesting an attack in shell and dealing out damage.
	 -'__foe_attack'
	   ---'__foe_attack' takes the string argument 'species' (the species of the foe Pokemon) as input.
	      It runs the foe's turn in battle, picking a random move for it and dealing out damage.
	 -'__get_movebox'
	   ---'__get_movebox' takes the string arguments 'move1' and 'move2' (moves available to the user's Pokemon) as inputs.
	      It creates a formatted box containing the available moves as a string, assigning the string to the variable 'movebox'.
	      'movebox' is then returned.
	 -'__compare_types'
	   ---'__compare_types' takes the string arguments 'type1' (the type of the attacking Pokemon) and 'type2' (the type of the defending Pokemon) as inputs.
	      It compares the types of the Pokemon to figure out if there is a type advantange between the two.
	      Grass Pokemon do more damage to Water Pokemon, Water to Fire, and Fire to Grass.
	      Grass Pokemon do less damage to Grass and Fire Pokemon, Water to Water and Grass, and Fire to Fire and Water.
	      Advantage/disadvantages are represented by a number that will be factored into damage calculations during a battle (type advantages mean higher numbers).
	      This number is returned as 'special' and a message that states the advantage status is returned as 'message'.


Demo Program: Description and Instructions

Description

My demo program is a shell that initiates my little game 'Pythomon'. 
It is based off of the Pokemon video games, specifically their battling, stats, and experience level mechanisms.
You get to choose a Pokemon, give it a nickname, and battle with it as it grows in experience!

Instructions

Since my demo program is a shell, all instructions on how to manuever through the program are built into its terminal interface.
To start the program, open up your terminal, navigate to the directory that contains the program, and run 'python' or 'python3' or 'python2', followed by '10_1_your_own_class.py'.

