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
from soulforge.lib import headerdata

class dicepool:
    def __init__(self):
        self.faces = headerdata.SF_DIEROLLER_FACES
        self.pool = headerdata.SF_DIEROLLER_POOL
        self.botch = headerdata.SF_DIEROLLER_BOTCH
        self.difficulty = headerdata.SF_DIEROLLER_DIFFICULTY
        self.tabulate = headerdata.SF_DIEROLLER_TABULATE
        self.successes = 0
        self.failures = 0
        self.botches = 0
        self.final = 0
        self.dice = []

    def setrng(self, rngname):
        if rngname == headerdata.SF_DIEROLLER_RNGSTRINGS[0]:
            self.rng = random.Random()
            self.rngfunc = self.rng.randint
        elif rngname == headerdata.SF_DIEROLLER_RNGSTRINGS[1]:
            self.rng = random.WichmannHill()
            self.rngfunc = self.rng.randint
        elif rngname == headerdata.SF_DIEROLLER_RNGSTRINGS[2]:
            self.rng = random.SystemRandom()
            self.rngfunc = self.rng.randint
        else:
            return False
        if headerdata.options.verbose:
            print "Using RNG: " + rngname

    def roll(self):
        self.successes = 0
        self.failures = 0
        self.botches = 0
        self.final = 0
        del self.dice
        self.dice = []
        for i in range(self.pool):
            val = self.rngfunc(1, self.faces)
            if self.tabulate:
                if val >= self.difficulty:
                    self.successes += 1
                elif self.botch and val == 1:
                    self.botches += 1
                else:
                    self.failures += 1
            self.dice.append(val)
        if self.tabulate:
            self.final = self.successes - self.botches
