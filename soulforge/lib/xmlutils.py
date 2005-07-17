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

import sys
import re
import bz2
import gzip
from xml.dom import minidom
from soulforge.lib import headerdata

def getnodetext(node):
    string = ""
    for nod in node.childNodes:
        if nod.nodeType == nod.TEXT_NODE:
            string = string + nod.data
    return re.sub('[^A-Za-z\ _\-0-9]*', '', string).strip()

def loaddata(filename):
    try:
        bzd = bz2.BZ2File(filename, "r")
	data = minidom.parseString(bzd.read())
	if headerdata.options.verbose:
	    print "BZ2-compressed Soulforge data file loaded"
    except:
        try:
	    gzd = gzip.GzipFile(filename, "r")
	    data = minidom.parseString(gzd.read())
	    if headerdata.options.verbose:
	        print "Gzip-compressed Soulforge data file loaded"
	except:
	    try:
                data = minidom.parse(filename)
		if headerdata.options.verbose:
		    print "Plaintext data file loaded"
	    except:
	        raise IOError, 'Could not read file data'
		return
    return data

def savedata(dom, filename, compress, dtd = ''):
    filedescriptor = None
    dtdfile = None
    if dtd:
        try:
            dtdfile = open(dtd, "r")
	except:
	    if headerdata.options.verbose:
	        sys.stderr.write("Could not open DTD file, ignoring...")
    if filename.lower().endswith(headerdata.SF_COMPRESSED_EXT):
        if compress == "bzip2":
            filedescriptor = bz2.BZ2File(filename, "w")
	    print "Saving to BZ2-compressed Soulforge data file"
	elif compress == "gzip":
	    filedescriptor = gzip.GzipFile(filename, "w")
	        print "Saving to Gzip-compressed Soulforge data file"
	else:
	    filedescriptor = open(filename, "w")
	    if headerdata.options.verbose:
	        print "Saving to plaintext Soulforge data file"
    else:
        filedescriptor = open(filename, "w")
	if headerdata.options.verbose:
	    print "Saving to legacy XML document"
    if dtdfile:
        filedescriptor.write("<?xml version=\"1.0\" ?>\n\n")
        filedescriptor.write("<!DOCTYPE soulforge_character [\n")
        filedescriptor.write(dtdfile.read())
        filedescriptor.write("]>")
        filedescriptor.write("\n")
        filedescriptor.write(dom.toprettyxml()[22:])
    else:
        filedescriptor.write(dom.toprettyxml())
    filedescriptor.close()
