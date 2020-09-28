import sys
from DICE_MECHANICS.Stat_rolls import STAT_ROLLS    #imports the "dice roll" function for stats
from DICE_MECHANICS.attribute_mods import modifier  #imports the attribute modifiers for each stat
from CLASSES import character_class                 #imports the individual classes from 'class' list
from SPECIESFILES import SPECIES , human , bothan , cerean , duro , ewok , gammorean , gungan , ithorian , kelDor , monCalamari , quarren , rodian , sullustan , trandoshan , twiLek , wookie , zabrak			    #imports individual species from the 'species' list

#Defines each specific 'Class' based on a separate list within the file 'character_class.py'
STARTER_CLASS = character_class.starting_classes
PRESTIGE_CLASS = character_class.prestige_classes
DROID_CLASS = character_class.droid_classifications

#######################################################################

		
### PRINTS starting  ATTRIBUTE SCORES ###
def stat_print():
	print("Your starting stats are: " +
	  "\n" + 'STR: ' + str(STR) + ' ' + str(modifier(STR)) \
         +"\n" + 'DEX: ' + str(DEX) + ' ' + str(modifier(DEX)) \
         +"\n" + 'CON: ' + str(CON) + ' ' + str(modifier(CON)) \
         +"\n" + 'INT: ' + str(INT) + ' ' + str(modifier(INT)) \
         +"\n" + 'WIS: ' + str(WIS) + ' ' + str(modifier(WIS)) \
         +"\n" + 'CHA: ' + str(CHA) + ' ' + str(modifier(CHA)))


#######################################################################


def stat_size():                                    #function dictating creature size in metric units (height/weight)

	size = ''
	if size == 'fine': 
		height = .1
		weight = .27
	elif size == 'diminutive' :
		height = .25
		weight = 1.0
	elif size == 'tiny' :
		height = .5
		weight = 2.9
	elif size == 'small' :
		height = 1.0
		weight = 12
	elif size == 'medium' :
		height = 1.8
		weight = 65
	elif size == 'large' :
		height = 3.9
		weight = 500
	elif size == 'huge' :
		height = 7
		weight = 3000
	elif size == 'gargantuan' :
		height = 15
		weight = 50000
	elif size == 'colossal' :
		height = 22
		weight = 144000
	else:
		size == 'medium'
		height = 1.0
		weight = 12
		
	return height , weight
		
################################################################################


### Questions for user to answer about character 
character_name = input("What is the name of this character? ")
name_verify = input("Are you sure? (Y/N) ")
	
if name_verify == 'yes' or name_verify == 'y':
	character_name
elif name_verify == 'no' or name_verify == 'n':
	while name_verify == 'no' or name_verify =='n':
		character_name = input("Enter new name. ")
		name_verify = input("Are you sure? (Y/N) ")
		
GENDER = input("What gender is this character? ")
EYE_COLOR = input("What is the character's eye color? ")
HAIR_COLOR = input("What color hair does the character have? ")
SKIN_COLOR = input("What is the character's skin color? ")

class_name = ''
character_lvl = 1
class_lvl = 0
age = input("What age is your character? ")

height , weight = stat_size()
	
basic_species = SPECIES.starter_species
print("\n".join(basic_species))
species = input("From the list above, what species is " + character_name + '? \n').capitalize()

##################################################################################

#SPECIES TRAITS BELOW
species_desc = ''
species_personality = ''
species_physicality = ''
species_homeworld = ''
species_language = ''
species_ex_names = ''
species_adventuring = ''
species_size = stat_size()
species_auto_language = ''

if species == SPECIES.starter_species[0]:
	species_desc = human.description
	species_personality = human.personality
	species_physicality = human.physicality
	species_homeworld = human.homeworld
	species_language = human.language
	species_ex_names = human.example_names
	species_adventuring = human.adventuring
	species_size = human.trait_size
	species_auto_language = human.auto_language
elif species == SPECIES.starter_species[1]:
	species_desc = bothan.description
	species_personality = bothan.personality
	species_physicality = bothan.physicality
	species_homeworld = bothan.homeworld
	species_language = bothan.language
	species_ex_names = bothan.example_names
	species_adventuring = bothan.adventuring
	species_size = bothan.trait_size
	species_auto_language = bothan.auto_language
elif species == SPECIES.starter_species[2]:
	species_desc = 'none'

#############################################################

#STAT ROLL MECHANICS
STR = STAT_ROLLS()
DEX = STAT_ROLLS()
CON = STAT_ROLLS()
INT = STAT_ROLLS()
WIS = STAT_ROLLS()
CHA = STAT_ROLLS()


stat_print()

re_roll = input("Keep these rolls? (Y/N) ")
re_roll = re_roll.lower()

if re_roll == 'yes' or re_roll == 'y':
	pass
elif re_roll == 'no' or re_roll == 'n':
	while re_roll == 'no' or re_roll == 'n':
		STR = STAT_ROLLS()
		DEX = STAT_ROLLS()
		CON = STAT_ROLLS()
		INT = STAT_ROLLS()
		WIS = STAT_ROLLS()
		CHA = STAT_ROLLS()

		stat_print()

		re_roll = input("Will these suffice? ")
		re_roll = re_roll.lower()
#######################################################################

### Sets up how the final print will end up in the terminal ###
print(

"\n \t Character Name: " + character_name + "\t Player Name: GM" \

+ "\t Class: " + class_name + "\t Species: " + species + "\t Character Level: " \

+ str(character_lvl) + "\t CLASS Level: " + str(class_lvl) + '\n' \

+ "\t Age: " + str(age) + "\t Gender: " + GENDER + "\t Height (m): " + str(height) \

+ "\t Weight (Kg): " + str(weight) + "\t Size: "  + species_size + "\t Eyes: " + EYE_COLOR + "\t Hair Color: " + HAIR_COLOR \
    
+ "\t Skin Color: " + SKIN_COLOR \

+ "\n \n" \

+ "\t Attribute \t Ability Score \t Ability Modifier \n" + '\t'  \

+   "   STR    \t \t" + str(STR) +  "\t \t" + str(modifier(STR)) + '\n' \

+ "\t   DEX    \t \t" + str(DEX) +  "\t \t" + str(modifier(DEX)) + '\n' \
        
+ "\t   CON    \t \t" + str(CON) +  "\t \t" + str(modifier(CON)) + '\n' \


+ "\t   INT    \t \t" + str(INT) +  "\t \t" + str(modifier(INT)) + '\n' \

+ "\t   WIS    \t \t" + str(WIS) +  "\t \t" + str(modifier(WIS)) + '\n' \

+ "\t   CHA    \t \t" + str(CHA) +  "\t \t" + str(modifier(CHA)) + '\n \n' \

+ species_desc + '\n \n' + species_personality + '\n \n'  \

+ species_physicality + '\n \n' + species_homeworld + '\n \n' \

+ species_language + '\n \n' + species_ex_names + '\n \n' \

+ species_adventuring + '\n \n' + species_auto_language + '\n \n' \
)
