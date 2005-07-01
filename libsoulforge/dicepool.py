#
# Soulforge
# Copyright (C) 2005 Christopher Han <xiphux@gmail.com>
#
# This file is part of Soulforge.
#
# Soulforge is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Soulforge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Soulforge; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

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
	self.final = 0
	self.dice = []
	
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
	self.final = 0
	del self.dice
	self.dice = []
        for i in range(self.pool):
	    v = self.rngfunc(1,self.faces)
	    if self.tabulate:
	        if v >= self.difficulty:
		    self.successes += 1
		elif self.botch and v == 1:
		    self.botches += 1
		else:
		    self.failures += 1
            self.dice.append(v)
	if self.tabulate:
	    self.final = self.successes - self.botches
