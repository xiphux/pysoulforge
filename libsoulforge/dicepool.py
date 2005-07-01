import random

class dicepool(object):
    def __init__(self):
        self.faces = 10
	self.pool = 1
	self.botch = True
	self.difficulty = 6
	self.tabulate = False
	self.rng = random.Random()
	self.rngfunc = self.rng.randint
	self.successes = 0
	self.failures = 0
	self.botches = 0
	
    def setrng(self,rngname):
        if rngname == "Mersenne Twister":
	    self.rng = random.Random()
	    self.rngfunc = self.rng.randint
	elif rngname == "Wichmann-Hill":
	    self.rng = random.WichmannHill()
	    self.rngfunc = self.rng.randint
	elif rngname == "urandom()":
	    self.rng = random.SystemRandom()
	    self.rngfunc = self.rng.randint

    def roll(self):
        self.successes = 0
	self.failures = 0
	self.botches = 0
        for i in range(self.pool):
	    v = self.rngfunc(1,self.faces)
	    if self.tabulate:
	        if v >= self.difficulty:
		    self.successes += 1
		elif self.botch and v == 1:
		    self.botches += 1
		else:
		    self.failures += 1
            self.dice[i] = v
