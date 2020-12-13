import math
def modifier(ATTRIBUTE):

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
		mod = '+' + str(1)
	elif ATTRIBUTE >= 14 and ATTRIBUTE <= 15:
		mod = '+' + str(2)
	elif ATTRIBUTE >= 16 and ATTRIBUTE <= 17:
		mod = '+' + str(3)
	elif ATTRIBUTE >= 18 and ATTRIBUTE <= 19:
		mod = '+' + str(4)
	elif ATTRIBUTE >= 20 and ATTRIBUTE <= 21:
		mod = '+' + str(5)
	elif ATTRIBUTE >= 22:
		mod = '+' + str(math.ceil(((ATTRIBUTE - 21) / 2 ) + 5))
		
	return mod
	

