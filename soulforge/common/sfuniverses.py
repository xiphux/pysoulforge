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
# $Id: sfuniverses.py 110 2005-07-22 10:24:48Z xiphux $
#

from soulforge.lib import headerdata
from soulforge.common.sheets import vampire_the_masquerade,vampire_the_masquerade_data

universes = [ 'Vampire: The Masquerade' ]

class universe:
    def __init__(self):
        pass

    def name(self):
        return ''

    def dtdfile(self):
        return ''

    def dtd(self):
        return ''

    def sheet(self, *args, **kwargs):
        raise NotImplementedError("This method must be implemented!")

    def sheet2xml(self, *args, **kwargs):
        raise NotImplementedError("This method must be implemented!")

    def xml2sheet(self, *args, **kwargs):
        raise NotImplementedError("This method must be implemented!")


class vampire_the_masquerade_universe(universe):
    def __init__(self):
        pass

    def name(self):
        return 'Vampire: The Masquerade'

    def dtdfile(self):
        return 'vampire_the_masquerade.dtd'

    def dtd(self):
        return vampire_the_masquerade_data.dtd()

    def sheet(self, *args, **kwargs):
        return vampire_the_masquerade.vampire_the_masquerade(*args, **kwargs)

    def sheet2xml(self, *args, **kwargs):
        return vampire_the_masquerade_data.sheet2xml(*args, **kwargs)

    def xml2sheet(self, *args, **kwargs):
        return vampire_the_masquerade_data.xml2sheet(*args, **kwargs)

def getuniverse(univ):
    if univ == 'Vampire: The Masquerade':
        return vampire_the_masquerade_universe
    else:
        return None
