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

import gettext
gettext.install('soulforge',unicode=1)

SF_VERSION = "%prog 0.0.1"

SF_COMPRESSED_EXT = ".sfd"

SF_SFSTAT_BUTTONS = 5

SF_SFPOOL_ROWS = 2
SF_SFPOOL_COLS = 10

SF_DIEROLLER_FACES = 10
SF_DIEROLLER_POOL = 1
SF_DIEROLLER_BOTCH = True
SF_DIEROLLER_DIFFICULTY = 6
SF_DIEROLLER_TABULATE = False
SF_DIEROLLER_RNGSTRINGS = [ "Mersenne Twister", "Wichmann-Hill", "urandom()" ]

SF_FILEMASK = _("Soulforge Data") + " (*.sfd)|*.sfd|XML (*.xml)|*.xml|" + _("All files") + " (*.*)|*.*"

SF_CONFIGKEY_LOADDIR = "/lastrun/loaddir"
SF_CONFIGKEY_SAVEDIR = "/lastrun/savedir"

SF_CONFIGKEY_COMPRESS = "/settings/compress"
SF_CONFIGDEFAULT_COMPRESS = 1

SF_CONFIGKEY_RNG = "/settings/rng"
SF_CONFIGDEFAULT_RNG = "Mersenne Twister"


options = None
