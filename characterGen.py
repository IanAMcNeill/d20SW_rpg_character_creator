import sys , os.path
from DICE_MECHANICS.Stat_rolls import STAT_ROLLS, specificStats  #imports the "dice roll" function for stats
from DICE_MECHANICS.attribute_mods import modifier  #imports the attribute modifiers for each stat
from CLASSES import character_class, Fringer            #imports the individual classes from 'class' list
from SPECIESFILES import SPECIES , human , bothan , cerean , duro , ewok , gammorean , gungan , ithorian , kelDor , monCalamari , quarren , rodian , sullustan , trandoshan , twiLek , wookie , zabrak	 #imports individual species from the 'species' list

#-------------Defines each specific 'Class' based on a separate list within the file 'character_class.py' ------------#
STARTER_CLASS = character_class.starting_classes
PRESTIGE_CLASS = character_class.prestige_classes
DROID_CLASS = character_class.droid_classifications

#######################################################################

#--------- function dictating creature size in metric units (height/weight)-------#
def stat_size():                                    

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
		height = 1.8
		weight = 12
		
	return height , weight
		
################################################################################


###---------- Questions for user to answer about character ----------#
playerName = ''
whoAmI = input("Are you the GM or a Player? \n\n").upper()
if whoAmI == "GM":
	playerName = "GM"
	print("Welcome back Game Master!\n")
	
elif whoAmI == "PLAYER":
	playerName = input("What is your name? \n")
	print("Hello " + playerName + "! \n")
else:
	playerName = "Player"
	

#---------------------- SPECIES LIST -------------------#
basic_species = SPECIES.starter_species

print("\n".join(basic_species))

species = input("\n\nFrom the list above, what species is your character?\n\n").capitalize()

#-----------------Name----------------#
if species == SPECIES.starter_species[0]:
	print('\n' + "--------------------------------------------------")
	print('\n' +human.example_names + '\n')
	print(human.description + '\n')
	print(human.physicality + '\n')
	print(human.homeworld + '\n')
	print(human.language + '\n')
	print(human.adventuring + '\n')
	print('\n' + "--------------------------------------------------")	
elif species == SPECIES.starter_species[1]:
	print('\n' + "--------------------------------------------------")
	print('\n' + bothan.example_names + '\n')
	print(bothan.description + '\n')
	print(bothan.physicality + '\n')
	print(bothan.homeworld + '\n')
	print(bothan.language + '\n')
	print(bothan.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[2]:
	print('\n' + "--------------------------------------------------")
	print('\n' + cerean.example_names + '\n')
	print(cerean.description + '\n')
	print(cerean.physicality + '\n')
	print(cerean.homeworld + '\n')
	print(cerean.language + '\n')
	print(cerean.adventuring + '\n')
	print(cerean.adjustments + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[3]:
	print('\n' + "--------------------------------------------------")
	print('\n' + duro.example_names + '\n')
	print(duro.description + '\n')
	print(duro.physicality + '\n')
	print(duro.homeworld + '\n')
	print(duro.language + '\n')
	print(duro.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[4]:
	print('\n' + "--------------------------------------------------")
	print('\n' +ewok.example_names + '\n')
	print(ewok.description + '\n')
	print(ewok.physicality + '\n')
	print(ewok.homeworld + '\n')
	print(ewok.language + '\n')
	print(ewok.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[5]:
	print('\n' + "--------------------------------------------------")
	print('\n' +gammorean.example_names + '\n')
	print(gammorean.description + '\n')
	print(gammorean.physicality + '\n')
	print(gammorean.homeworld + '\n')
	print(gammorean.language + '\n')
	print(gammorean.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[6]:
	print('\n' + "--------------------------------------------------")
	print('\n' +gungan.example_names + '\n')
	print(gungan.description + '\n')
	print(gungan.physicality + '\n')
	print(gungan.homeworld + '\n')
	print(gungan.language + '\n')
	print(gungan.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[7]:
	print('\n' + "--------------------------------------------------")
	print('\n' +ithorian.example_names + '\n')
	print(ithorian.description + '\n')
	print(ithorian.physicality + '\n')
	print(ithorian.homeworld + '\n')
	print(ithorian.language + '\n')
	print(ithorian.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[8]:
	print('\n' + "--------------------------------------------------")
	print('\n' +kelDor.example_names + '\n')
	print(kelDor.description + '\n')
	print(kelDor.physicality + '\n')
	print(kelDor.homeworld + '\n')
	print(kelDor.language + '\n')
	print(kelDor.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[9]:
	print('\n' + "--------------------------------------------------")
	print('\n' +monCalamari.example_names + '\n')
	print(monCalamari.description + '\n')
	print(monCalamari.physicality + '\n')
	print(monCalamari.homeworld + '\n')
	print(monCalamari.language + '\n')
	print(monCalamari.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[10]:
	print('\n' + "--------------------------------------------------")
	print('\n' +quarren.example_names + '\n')
	print(quarren.description + '\n')
	print(quarren.physicality + '\n')
	print(quarren.homeworld + '\n')
	print(quarren.language + '\n')
	print(quarren.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[11]:
	print('\n' + "--------------------------------------------------")
	print('\n' +rodian.example_names + '\n')
	print(rodian.description + '\n')
	print(rodian.physicality + '\n')
	print(rodian.homeworld + '\n')
	print(rodian.language + '\n')
	print(rodian.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[12]:
	print('\n' + "--------------------------------------------------")
	print('\n' +sullustan.example_names + '\n')
	print(sullustan.description + '\n')
	print(sullustan.physicality + '\n')
	print(sullustan.homeworld + '\n')
	print(sullustan.language + '\n')
	print(sullustan.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[13]:
	print('\n' + "--------------------------------------------------")
	print('\n' +trandoshan.example_names + '\n')
	print(trandoshan.description + '\n')
	print(trandoshan.physicality + '\n')
	print(trandoshan.homeworld + '\n')
	print(trandoshan.language + '\n')
	print(trandoshan.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[14]:
	print('\n' + "--------------------------------------------------")
	print('\n' +twiLek.example_names + '\n')
	print(twiLek.description + '\n')
	print(twiLek.physicality + '\n')
	print(twiLek.homeworld + '\n')
	print(twiLek.language + '\n')
	print(twiLek.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[15]:
	print('\n' + "--------------------------------------------------")
	print('\n' +wookie.example_names + '\n')
	print(wookie.description + '\n')
	print(wookie.physicality + '\n')
	print(wookie.homeworld + '\n')
	print(wookie.language + '\n')
	print(wookie.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
elif species == SPECIES.starter_species[16]:
	print('\n' + "--------------------------------------------------")
	print('\n' +zabrak.example_names + '\n')
	print(zabrak.description + '\n')
	print(zabrak.physicality + '\n')
	print(zabrak.homeworld + '\n')
	print(zabrak.language + '\n')
	print(zabrak.adventuring + '\n')
	print('\n' + "--------------------------------------------------")
else:
	species == 'human'
	
character_name = input("\nWhat is the name of this character? ")
name_verify = input("Are you sure? (Y/N) ")
	
if name_verify == 'yes' or name_verify == 'y':
	character_name
elif name_verify == 'no' or name_verify == 'n':
	while name_verify == 'no' or name_verify =='n':
		character_name = input("Enter new name. ")
		name_verify = input("Are you sure? (Y/N) ")
else:
	name_verify == 'yes'
	character_name


#--------------------CLASS ----------------# working ON THIS!
starter_classes = character_class.starting_classes
print("\n".join(starter_classes))
class_name = input("\nFrom the list above, what is your starting class? ").capitalize()

class_desc = ''
class_exploits = ''
class_characteristcs = ''
class_background = ''
class_examples = ''
class_impAbil = ''

if class_name == character_class.starting_classes[0]:
	class_desc = Fringer.description
	class_exploits = Fringer.exploits
	class_characteristcs = Fringer.characteristics
	class_background = Fringer.background
	class_examples = Fringer.examples
	class_impAbil = Fringer.importantAbil
elif class_name == CLASSES.character_class[1]:
	class_desc = 'none'
	
character_lvl = 1
class_lvl = 0

#---------------- PERSONAL TRAITS -------------------#
GENDER = input("What gender is this character? ")
EYE_COLOR = input("What is the character's eye color? ")
HAIR_COLOR = input("What color hair does the character have? ")
SKIN_COLOR = input("What is the character's skin color? ")
age = input("What age is your character? ")

height , weight = stat_size()



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
	species_adventuring = human.adventuring
	species_size = human.trait_size
	species_auto_language = human.auto_language
elif species == SPECIES.starter_species[1]:
	species_desc = bothan.description
	species_personality = bothan.personality
	species_physicality = bothan.physicality
	species_homeworld = bothan.homeworld
	species_language = bothan.language
	species_adventuring = bothan.adventuring
	species_size = bothan.trait_size
	species_auto_language = bothan.auto_language
elif species == SPECIES.starter_species[2]:
	species_desc = cerean.description
	species_personality = cerean.personality
	species_physicality = cerean.physicality
	species_homeworld = cerean.homeworld
	species_language = cerean.language
	species_adventuring = cerean.adventuring
	species_size = cerean.trait_size
	species_auto_language = cerean.auto_language
elif species == SPECIES.starter_species[3]:
	species_desc = duro.description
	species_personality = duro.personality
	species_physicality = duro.physicality
	species_homeworld = duro.homeworld
	species_language = duro.language
	species_adventuring = duro.adventuring
	species_size = duro.trait_size
	species_auto_language = duro.auto_language
elif species == SPECIES.starter_species[4]:
	species_desc = ewok.description
	species_personality = ewok.personality
	species_physicality = ewok.physicality
	species_homeworld = ewok.homeworld
	species_language = ewok.language
	species_adventuring = ewok.adventuring
	species_size = ewok.trait_size
	species_auto_language = ewok.auto_language
elif species == SPECIES.starter_species[5]:
	species_desc = gammorean.description
	species_personality = gammorean.personality
	species_physicality = gammorean.physicality
	species_homeworld = gammorean.homeworld
	species_language = gammorean.language
	species_adventuring = gammorean.adventuring
	species_size = gammorean.trait_size
	species_auto_language = gammorean.auto_language
elif species == SPECIES.starter_species[6]:
	species_desc = gungan.description
	species_personality = gungan.personality
	species_physicality = gungan.physicality
	species_homeworld = gungan.homeworld
	species_language = gungan.language
	species_adventuring = gungan.adventuring
	species_size = gungan.trait_size
	species_auto_language = gungan.auto_language
elif species == SPECIES.starter_species[7]:
	species_desc = ithorian.description
	species_personality = ithorian.personality
	species_physicality = ithorian.physicality
	species_homeworld = ithorian.homeworld
	species_language = ithorian.language
	species_adventuring = ithorian.adventuring
	species_size = ithorian.trait_size
	species_auto_language = ithorian.auto_language
elif species == SPECIES.starter_species[8]:
	species_desc = kelDor.description
	species_personality = kelDor.personality
	species_physicality = kelDor.physicality
	species_homeworld = kelDor.homeworld
	species_language = kelDor.language
	species_adventuring = kelDor.adventuring
	species_size = kelDor.trait_size
	species_auto_language = kelDor.auto_language
elif species == SPECIES.starter_species[9]:
	species_desc = monCalamari.description
	species_personality = monCalamari.personality
	species_physicality = monCalamari.physicality
	species_homeworld = monCalamari.homeworld
	species_language = monCalamari.language
	species_adventuring = monCalamari.adventuring
	species_size = monCalamari.trait_size
	species_auto_language = monCalamari.auto_language
elif species == SPECIES.starter_species[10]:
	species_desc = quarren.description
	species_personality = quarren.personality
	species_physicality = quarren.physicality
	species_homeworld = quarren.homeworld
	species_language = quarren.language
	species_adventuring = quarren.adventuring
	species_size = quarren.trait_size
	species_auto_language = quarren.auto_language
elif species == SPECIES.starter_species[11]:
	species_desc = rodian.description
	species_personality = rodian.personality
	species_physicality = rodian.physicality
	species_homeworld = rodian.homeworld
	species_language = rodian.language
	species_adventuring = rodian.adventuring
	species_size = rodian.trait_size
	species_auto_language = rodian.auto_language
elif species == SPECIES.starter_species[12]:
	species_desc = sullustan.description
	species_personality = sullustan.personality
	species_physicality = sullustan.physicality
	species_homeworld = sullustan.homeworld
	species_language = sullustan.language
	species_adventuring = sullustan.adventuring
	species_size = sullustan.trait_size
	species_auto_language = sullustan.auto_language
elif species == SPECIES.starter_species[13]:
	species_desc = trandoshan.description
	species_personality = trandoshan.personality
	species_physicality = trandoshan.physicality
	species_homeworld = trandoshan.homeworld
	species_language = trandoshan.language
	species_adventuring = trandoshan.adventuring
	species_size = trandoshan.trait_size
	species_auto_language = trandoshan.auto_language
elif species == SPECIES.starter_species[14]:
	species_desc = twiLek.description
	species_personality = twiLek.personality
	species_physicality = twiLek.physicality
	species_homeworld = twiLek.homeworld
	species_language = twiLek.language
	species_adventuring = twiLek.adventuring
	species_size = twiLek.trait_size
	species_auto_language = twiLek.auto_language
elif species == SPECIES.starter_species[15]:
	species_desc = wookie.description
	species_personality = wookie.personality
	species_physicality = wookie.physicality
	species_homeworld = wookie.homeworld
	species_language = wookie.language
	species_adventuring = wookie.adventuring
	species_size = wookie.trait_size
	species_auto_language = wookie.auto_language
elif species == SPECIES.starter_species[16]:
	species_desc = zabrak.description
	species_personality = zabrak.personality
	species_physicality = zabrak.physicality
	species_homeworld = zabrak.homeworld
	species_language = zabrak.language
	species_adventuring = zabrak.adventuring
	species_size = zabrak.trait_size
	species_auto_language = zabrak.auto_language

#############################################################

###---------------- PRINTS starting  ATTRIBUTE SCORES -----------------###
def stat_print():

	print("Your starting stats are: " +
	  "\n" + 'STR: ' + str(STR) + ' ' + str(modifier(STR)) \
         +"\n" + 'DEX: ' + str(DEX) + ' ' + str(modifier(DEX)) \
         +"\n" + 'CON: ' + str(CON) + ' ' + str(modifier(CON)) \
         +"\n" + 'INT: ' + str(INT) + ' ' + str(modifier(INT)) \
         +"\n" + 'WIS: ' + str(WIS) + ' ' + str(modifier(WIS)) \
         +"\n" + 'CHA: ' + str(CHA) + ' ' + str(modifier(CHA)))


#######################################################################
#STAT ROLL MECHANICS
userInput = input("Would you like randomized Stats? ")
if userInput.lower() == 'y' or userInput.lower() == 'yes':
	STR = STAT_ROLLS()
	DEX = STAT_ROLLS()
	CON = STAT_ROLLS()
	INT = STAT_ROLLS()
	WIS = STAT_ROLLS()
	CHA = STAT_ROLLS()
elif userInput.lower() == 'n' or userInput.lower() == 'no':
	STR = int(input("Strength Score: "))
	DEX = int(input("Dexterity Score: "))
	CON = int(input("Constitution Score: "))
	INT = int(input("Intelligence Score: "))
	WIS = int(input("Wisdom Score: "))
	CHA = int(input("Charisma Score: "))
else:
	STR = STAT_ROLLS()
	DEX = STAT_ROLLS()
	CON = STAT_ROLLS()
	INT = STAT_ROLLS()
	WIS = STAT_ROLLS()
	CHA = STAT_ROLLS()
	
	
#Stat adjustments based on Species 
if species == SPECIES.starter_species[1]:
	STR = STR + bothan.strAdj
	DEX = DEX + bothan.dexAdj
	CON = CON + bothan.conAdj
	INT = INT + bothan.intAdj
	WIS = WIS + bothan.wisAdj
	CHA = CHA + bothan.chaAdj
	
elif species == SPECIES.starter_species[2]:
	STR = STR + cerean.strAdj
	DEX = DEX + cerean.dexAdj
	CON = CON + cerean.conAdj
	INT = INT + cerean.intAdj
	WIS = WIS + cerean.wisAdj
	CHA = CHA + cerean.chaAdj
elif species == SPECIES.starter_species[3]:
	STR = STR + duro.strAdj
	DEX = DEX + duro.dexAdj
	CON = CON + duro.conAdj
	INT = INT + duro.intAdj
	WIS = WIS + duro.wisAdj
	CHA = CHA + duro.chaAdj	
elif species == SPECIES.starter_species[4]:
	STR = STR + ewok.strAdj
	DEX = DEX + ewok.dexAdj
	CON = CON + ewok.conAdj
	INT = INT + ewok.intAdj
	WIS = WIS + ewok.wisAdj
	CHA = CHA + ewok.chaAdj
elif species == SPECIES.starter_species[5]:
	STR = STR + gammorean.strAdj
	DEX = DEX + gammorean.dexAdj
	CON = CON + gammorean.conAdj
	INT = INT + gammorean.intAdj
	WIS = WIS + gammorean.wisAdj
	CHA = CHA + gammorean.chaAdj
elif species == SPECIES.starter_species[6]:
	STR = STR + gungan.strAdj
	DEX = DEX + gungan.dexAdj
	CON = CON + gungan.conAdj
	INT = INT + gungan.intAdj
	WIS = WIS + gungan.wisAdj
	CHA = CHA + gungan.chaAdj
elif species == SPECIES.starter_species[7]:
	STR = STR + ithorian.strAdj
	DEX = DEX + ithorian.dexAdj
	CON = CON + ithorian.conAdj
	INT = INT + ithorian.intAdj
	WIS = WIS + ithorian.wisAdj
	CHA = CHA + ithorian.chaAdj
elif species == SPECIES.starter_species[8]:
	STR = STR + kelDor.strAdj
	DEX = DEX + kelDor.dexAdj
	CON = CON + kelDor.conAdj
	INT = INT + kelDor.intAdj
	WIS = WIS + kelDor.wisAdj
	CHA = CHA + kelDor.chaAdj
elif species == SPECIES.starter_species[9]:
	STR = STR + monCalamari.strAdj
	DEX = DEX + monCalamari.dexAdj
	CON = CON + monCalamari.conAdj
	INT = INT + monCalamari.intAdj
	WIS = WIS + monCalamari.wisAdj
	CHA = CHA + monCalamari.chaAdj
elif species == SPECIES.starter_species[10]:
	STR = STR + quarren.strAdj
	DEX = DEX + quarren.dexAdj
	CON = CON + quarren.conAdj
	INT = INT + quarren.intAdj
	WIS = WIS + quarren.wisAdj
	CHA = CHA + quarren.chaAdj
elif species == SPECIES.starter_species[11]:
	STR = STR + rodian.strAdj
	DEX = DEX + rodian.dexAdj
	CON = CON + rodian.conAdj
	INT = INT + rodian.intAdj
	WIS = WIS + rodian.wisAdj
	CHA = CHA + rodian.chaAdj
elif species == SPECIES.starter_species[12]:
	STR = STR + sullustan.strAdj
	DEX = DEX + sullustan.dexAdj
	CON = CON + sullustan.conAdj
	INT = INT + sullustan.intAdj
	WIS = WIS + sullustan.wisAdj
	CHA = CHA + sullustan.chaAdj
elif species == SPECIES.starter_species[13]:
	STR = STR + trandoshan.strAdj
	DEX = DEX + trandoshan.dexAdj
	CON = CON + trandoshan.conAdj
	INT = INT + trandoshan.intAdj
	WIS = WIS + trandoshan.wisAdj
	CHA = CHA + trandoshan.chaAdj
elif species == SPECIES.starter_species[14]:
	STR = STR + twiLek.strAdj
	DEX = DEX + twiLek.dexAdj
	CON = CON + twiLek.conAdj
	INT = INT + twiLek.intAdj
	WIS = WIS + twiLek.wisAdj
	CHA = CHA + twiLek.chaAdj
elif species == SPECIES.starter_species[15]:
	STR = STR + wookie.strAdj
	DEX = DEX + wookie.dexAdj
	CON = CON + wookie.conAdj
	INT = INT + wookie.intAdj
	WIS = WIS + wookie.wisAdj
	CHA = CHA + wookie.chaAdj
elif species == SPECIES.starter_species[16]:
	STR = STR + zabrak.strAdj
	DEX = DEX + zabrak.dexAdj
	CON = CON + zabrak.conAdj
	INT = INT + zabrak.intAdj
	WIS = WIS + zabrak.wisAdj
	CHA = CHA + zabrak.chaAdj

stat_print()


re_roll = input("Keep these rolls? (Y/N) ")
re_roll = re_roll.lower()

if re_roll == 'yes' or re_roll == 'y':
	pass
elif re_roll == 'no' or re_roll == 'n':
	while re_roll == 'no' or re_roll == 'n':
		userInput = input("Want custom stats? ")
		if userInput.lower() == 'y' or userInput.lower() == 'yes':
			STR = int(input("Strength Score: "))
			DEX = int(input("Dexterity Score: "))
			CON = int(input("Constitution Score: "))
			INT = int(input("Intelligence Score: "))
			WIS = int(input("Wisdom Score: "))
			CHA = int(input("Charisma Score: "))
			
		elif userInput.lower() == 'n' or userInput.lower() =='no':
			STR = STAT_ROLLS()
			DEX = STAT_ROLLS()
			CON = STAT_ROLLS()
			INT = STAT_ROLLS()
			WIS = STAT_ROLLS()
			CHA = STAT_ROLLS()
		else:
			STR = STAT_ROLLS()
			DEX = STAT_ROLLS()
			CON = STAT_ROLLS()
			INT = STAT_ROLLS()
			WIS = STAT_ROLLS()
			CHA = STAT_ROLLS()
			
		stat_print()
		re_roll = input("Will these suffice? (Y/N) ")
		re_roll = re_roll.lower()
else:
	re_roll = 'no'
	while re_roll == 'no' or re_roll == 'n':
		userInput = input("Want custom stats? ")
		if userInput.lower() == 'y' or userInput.lower() == 'yes':
			STR = int(input("Strength Score: "))
			DEX = int(input("Dexterity Score: "))
			CON = int(input("Constitution Score: "))
			INT = int(input("Intelligence Score: "))
			WIS = int(input("Wisdom Score: "))
			CHA = int(input("Charisma Score: "))
		elif userInput.lower() == 'n' or userInput.lower() =='no':
		
			STR = STAT_ROLLS()
			DEX = STAT_ROLLS()
			CON = STAT_ROLLS()
			INT = STAT_ROLLS()
			WIS = STAT_ROLLS()
			CHA = STAT_ROLLS()
		else:
			print("\n Try again. \n")
			
		stat_print()
		re_roll = input("Will these suffice? (Y/N) ")
		re_roll = re_roll.lower()
		if re_roll != 'y' or re_roll != 'yes' or re_roll != 'n' or re_roll != 'no':
			re_roll = 'no'
		
###########################################################



### Sets up how the final print will end up in the terminal ###
txtFile = character_name + ".txt"
sys.stdout = open(txtFile, "w")

print(

"\n \t Character Name: " + character_name + "\t Player Name: " + playerName \

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

+ species_auto_language + '\n \n'  + "BACKSTORY: " + '\n \n'
)
sys.stdout.close()

print("New File Created in current directory")
