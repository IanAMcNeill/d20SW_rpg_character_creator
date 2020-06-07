import random

def d6_roll():
	die_roll = random.randint(1 , 6)
	
	return die_roll
	
	
def STAT_ROLLS():
	die_1 = d6_roll()
	die_2 = d6_roll()
	die_3 = d6_roll()
	die_4 = d6_roll()

	if die_1 == die_2:
		if die_2 == die_3:
			if die_3 == die_4:
				stat_roll = die_1 + die_2 + die_3
			elif die_3 > die_4:
				stat_roll = die_1 + die_2 + die_3
			elif die_3 < die_4:
				stat_roll = die_1 + die_2 + die_4
		elif die_2 > die_3:
			if die_3 == die_4:
				stat_roll = die_1 + die_2 + die_3
			elif die_3 > die_4:
				stat_roll = die_1 + die_2 + die_3
			elif die_3 < die_4:
				stat_roll = die_1 + die_2 + die_4
		elif die_2 < die_3:
			if die_3 == die_4:
				stat_roll = die_1 + die_3 + die_4
			elif die_3 > die_4:
				if die_2 == die_4:
					stat_roll = die_1 + die_2 + die_3
				elif die_2 > die_4:
					stat_roll = die_1 + die_3 + die_4
				elif die_2 < die_4:
					stat_roll = die_1 + die_3 + die_4
			elif die_3 < die_4:
				if die_2 == die_4:
					stat_roll = die_1 + die_2 + die_3	
				elif die_2 > die_4:
					stat_roll = die_1 + die_3 + die_4 
				elif die_2 < die_4:
					stat_roll = die_1 + die_3 + die_4

					
	elif die_1 > die_2:
		if die_2 == die_3:
			if die_3 == die_4:
				stat_roll = die_1 + die_2 + die_3
			elif die_3 > die_4:
				stat_roll = die_1 + die_2 + die_3
			elif die_3 < die_4:
				stat_roll = die_1 + die_2 + die_4
		elif die_2 > die_3:
			if die_3 == die_4:
				stat_roll =  die_1 + die_2 + die_3
			elif die_3 > die_4:
				stat_roll = die_2 + die_3 + die_4
			elif die_3 < die_4:
				stat_roll = die_1 + die_2 + die_4
		elif die_2 < die_3:
			if die_3 == die_4:
				stat_roll = die_1 + die_2 + die_3
			elif die_3 > die_4:
				stat_roll = die_1 + die_3 + die_4
			elif die_3 < die_4:
				stat_roll = die_1 + die_3 + die_4
	
	elif die_1 < die_2:
		if die_2 == die_3:
			if die_3 == die_4:
				stat_roll = die_2 + die_3 + die_4
			elif die_3 > die_4:
				stat_roll = die_2 + die_3 + die_4
			elif die_3 < die_4:
				stat_roll = die_2 + die_3 + die_4
		elif die_2 > die_3:
			if die_3 == die_4:
				stat_roll = die_2 + die_3 + die_4
			elif die_3 > die_4:
				if die_1 == die_4:
					stat_roll = die_1 + die_2 + die_3
				elif die_1 > die_4:
					stat_roll = die_1 + die_2 + die_3
				elif die_1 < die_4:
					stat_roll = die_2 + die_3 + die_4
			elif die_3 < die_4:
					stat_roll = die_1 + die_2 + die_4
		elif die_2 < die_3:
			if die_3 == die_4:
				stat_roll = die_1 + die_2 + die_3
			elif die_3 > die_4:
				if die_1 == die_4:
					stat_roll = die_1 + die_2 + die_3
				elif die_1 > die_4:
					stat_roll = die_1 + die_2 + die_3
				elif die_1 < die_4:
					stat_roll = die_2 + die_3 + die_4
			elif die_3 < die_4:
				stat_roll = die_2 + die_3 + die_4
	
	return stat_roll


def mods(ATTRIBUTE):

       
	if ATTRIBUTE <= 1:
		 mod = -5
	elif ATTRIBUTE >= 2 and ATTRIBUTE <= 3:
		mod = -4
	elif ATTRIBUTE >= 4 and ATTRIBUTE <= 5:
		mod = -3
	elif ATTRIBUTE >= 6 and ATTRIBUTE <= 7:
		mod = -2
	elif ATTRIBUTE >= 8 and ATTRIBUTE <= 9:
		mod = -1
	elif ATTRIBUTE >= 10 and ATTRIBUTE <= 11:
		mod = 0
	elif ATTRIBUTE >= 12 and ATTRIBUTE <= 13:
		mod = 1
	elif ATTRIBUTE >= 14 and ATTRIBUTE <= 15:
		mod = 2
	elif ATTRIBUTE >= 16 and ATTRIBUTE <= 17:
		mod = 3
	elif ATTRIBUTE >= 18 and ATTRIBUTE <= 19:
		mod = 4
	elif ATTRIBUTE >= 20 and ATTRIBUTE <= 21:
		mod = 5
	elif ATTRIBUTE >= 22:
		mod = ((ATTRIBUTE - 21) / 2 ) + 5
		
	return mod
	
def stat_print():
	print("Your starting stats are: \n" + 'STR: '+ str(STR) + ' ' + str(mods(STR)) \
         +"\n" + 'DEX: '+ str(DEX) + ' ' + str(mods(DEX)) \
         +"\n" + 'CON: '+ str(CON) + ' ' + str(mods(CON)) \
         +"\n" + 'INT: '+ str(INT) + ' ' + str(mods(INT)) \
         +"\n" + 'WIS: '+ str(WIS) + ' ' + str(mods(WIS)) \
         +"\n" + 'CHA: '+ str(CHA) + ' ' + str(mods(CHA)))


character_name = input("What is the name of this character? ")

name_verify = input("Are you sure? (Y/N) ")
if name_verify == 'yes' or name_verify == 'y':
	character_name
elif name_verify == 'no' or name_verify == 'n':
	character_name = input("Enter new name. ")

species_list = ['Human']

print (species_list)
species = input("From the list above, what species is " + character_name + '? ')

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
