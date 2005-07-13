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

from soulforge.libsoulforge import headerdata
from soulforge.soulforgemain.sheets import vampire_the_masquerade,vampire_the_masquerade_data

def _(message): return message

universes = [ _('Vampire: The Masquerade') ]

universe_sheets = {
	'Vampire: The Masquerade': vampire_the_masquerade.vampire_the_masquerade
}

universe_sheet2xml = {
	'Vampire: The Masquerade': vampire_the_masquerade_data.sheet2xml
}

universe_xml2sheet = {
	'Vampire: The Masquerade': vampire_the_masquerade_data.xml2sheet
}

del _
