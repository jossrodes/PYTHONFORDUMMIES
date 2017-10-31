import random
def roll(d=6):
	return random.randint(1, d)
roll() # rolls a 6-sided die
roll(20) # rolls a 20-sided die