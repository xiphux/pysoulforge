#!/usr/bin/python -OO
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

from optparse import OptionParser
from compileall import compile_dir
from wxPython.wx import *
from soulforgemain import sfrootframe

SF_VERSION = "%prog 0.0.1"

class Soulforge(wxApp):
    def OnInit(self):
        sframe = sfrootframe.sfrootframe(NULL, -1, u"Soulforge")
	sframe.Show(true)
	self.SetTopWindow(sframe)
	return true

try:
    import psyco
    psyco.full()
except ImportError:
    pass

if __name__ == "__main__":
    parser = OptionParser(version=SF_VERSION)
    parser.add_option("-v","--verbose",action="store_true",dest="verbose",help="verbose output")
    parser.add_option("-f","--force",action="store_true",dest="force",help="force operation")
    parser.add_option("-c","--compile",action="store_true",dest="compile",help="byte-compile")
    parser.set_defaults(verbose=False)
    parser.set_defaults(force=False)
    parser.set_defaults(compile=False)
    (options, args) = parser.parse_args()

    if options.compile:
        if not options.verbose:
	    q = True
	else:
	    q = False
        compile_dir(".",force=options.force,quiet=q)
    
    sf = Soulforge(0)
    sf.MainLoop()
