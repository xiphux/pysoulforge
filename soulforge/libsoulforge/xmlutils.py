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

import re
import bz2
from xml.dom import minidom
from soulforge.libsoulforge import headerdata

def getnodetext(node):
    string = ""
    for nod in node.childNodes:
        if nod.nodeType == nod.TEXT_NODE:
            string = string + nod.data
    return re.sub('[^A-Za-z\ _\-0-9]*', '', string).strip()

def loaddata(filename):
    data = None
    try:
        bzd = bz2.BZ2File(filename, "r")
	data = minidom.parseString(bzd.read())
    except:
        data = minidom.parse(filename)
    return data

def savedata(dom, filename, compress):
    filedescriptor = None
    if filename.lower().endswith(headerdata.SF_COMPRESSED_EXT) and compress:
        filedescriptor = bz2.BZ2File(filename, "w")
    else:
        filedescriptor = open(filename, "w")
    dom.writexml(filedescriptor, "    ", "    ", "\n")
    filedescriptor.close()
