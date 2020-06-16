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
			#	- equates to no solution -
			
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
