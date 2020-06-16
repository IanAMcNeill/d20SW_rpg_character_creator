from Stat_rolls import STAT_ROLLS
from attribute_mods import modifier
import character_class

attribute = STAT_ROLLS()
attribute_mod = modifier(attribute)

starter_class = character_class.starting_classes
prestige_class = character_class.prestige_classes
droid_class = character_class.droid_classifications

def stat_print():
	print("Your starting stats are: " +
	 "\n" + 'STR: '+ str(STR) + ' ' + str(attribute_mod) \
         +"\n" + 'DEX: '+ str(DEX) + ' ' + str(attribute_mod) \
         +"\n" + 'CON: '+ str(CON) + ' ' + str(attribute_mod) \
         +"\n" + 'INT: '+ str(INT) + ' ' + str(attribute_mod) \
         +"\n" + 'WIS: '+ str(WIS) + ' ' + str(attribute_mod) \
         +"\n" + 'CHA: '+ str(CHA) + ' ' + str(attribute_mod))


character_name = input("What is the name of this character? ")

name_verify = input("Are you sure? (Y/N) ")
if name_verify == 'yes' or name_verify == 'y':
	character_name
elif name_verify == 'no' or name_verify == 'n':
	character_name = input("Enter new name. ")

species_list = ['Human']

print (species_list)
species = input("From the list above, what species is " + character_name + '? ')

STR = attribute
DEX = attribute
CON = attribute
INT = attribute
WIS = attribute
CHA = attribute

stat_print()

re_roll = input("Keep these rolls? (Y/N) ")
re_roll = re_roll.lower()

if re_roll == 'yes' or re_roll == 'y':
	pass
elif re_roll == 'no' or re_roll == 'n':
	while re_roll == 'no' or re_roll == 'n':
		STR = attribute
		DEX = attribute
		CON = attribute
		INT = attribute
		WIS = attribute
		CHA = attribute

		stat_print()

		re_roll = input("Will these suffice? ")
		re_roll = re_roll.lower()
		
