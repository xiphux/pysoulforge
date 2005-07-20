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
import cStringIO
from xml.dom.ext import PrettyPrint
from xml.dom.ext.reader import Sax2
from soulforge.lib import headerdata

def getnodetext(node):
    string = ""
    for nod in node.childNodes:
        if nod.nodeType == nod.TEXT_NODE:
            string = string + nod.data
    return re.sub('[^A-Za-z\ _\-0-9]*', '', string).strip()

def load(filename):
    data = None
    try:
        dat = bz2.BZ2File(filename, "r")
	data = dat.read()
	if headerdata.options.verbose:
	    print "BZ2-compressed Soulforge data file loaded"
    except:
        try:
	    dat = gzip.GzipFile(filename, "r")
	    data = dat.read()
	    if headerdata.options.verbose:
	        print "Gzip-compressed Soulforge data file loaded"
	except:
	    try:
                dat = open(filename, "r")
		data = dat.read()
		if headerdata.options.verbose:
		    print "Plaintext data file loaded"
	    except:
	        raise IOError, 'Could not read file data'
		return
    dat.close()
    return data

def loaddata(filename):
    try:
        fd = load(filename)
    except:
	raise IOError, 'Could not read file data'
        return None
    reader = Sax2.Reader()
    doc = reader.fromString(fd)
    return doc

def save(filename, compress):
    filedescriptor = None
    if filename.lower().endswith(headerdata.SF_COMPRESSED_EXT):
        if compress == "bzip2":
            filedescriptor = bz2.BZ2File(filename, "w")
	    if headerdata.options.verbose:
	        print "Saving to BZ2-compressed Soulforge data file"
	elif compress == "gzip":
	    filedescriptor = gzip.GzipFile(filename, "w")
	    if headerdata.options.verbose:
	        print "Saving to Gzip-compressed Soulforge data file"
	else:
	    filedescriptor = open(filename, "w")
	    if headerdata.options.verbose:
	        print "Saving to plaintext Soulforge data file"
    else:
        filedescriptor = open(filename, "w")
	if headerdata.options.verbose:
	    print "Saving to legacy XML document"
    return filedescriptor

def insert_dtd(filename, compress, dtd):
    data = cStringIO.StringIO(load(filename))
    prolog = data.readline()
    stringdata = data.readlines()
    data.close()
    fd = save(filename, compress)
    fd.write(prolog)
    fd.write("<!DOCTYPE soulforge_character [\n")
    fd.write(dtd)
    fd.write("]>\n")
    fd.writelines(stringdata)
    fd.close()

def savedata(dom, filename, compress, dtd = ''):
    filedescriptor = save(filename, compress)
    PrettyPrint(dom,filedescriptor)
    filedescriptor.close()
    if dtd:
        insert_dtd(filename, compress, dtd)
