#!/usr/bin/env python
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
import wx
from soulforge.libsoulforge import headerdata
from soulforge.soulforgemain import sfrootframe

class Soulforge(wx.App):
    def OnInit(self):
        self.SetAppName("soulforge")
        config = wx.Config.Get()
        sframe = sfrootframe.sfrootframe(None, -1, u"Soulforge")
        sframe.Show(True)
        self.SetTopWindow(sframe)
        return True

    def OnExit(self):
        config = wx.Config.Get()
	del config

if __name__ == "__main__":
    parser = OptionParser(version=headerdata.SF_VERSION)
    parser.add_option("-v", "--verbose", action="store_true",
      dest="verbose", help="verbose output")
    parser.add_option("-f", "--force", action="store_true",
      dest="force", help="force operation")
    parser.add_option("-c", "--compile", action="store_true",
      dest="compile", help="byte-compile")
    parser.set_defaults(verbose=False)
    parser.set_defaults(force=False)
    parser.set_defaults(compile=False)
    (options, args) = parser.parse_args()

    headerdata.options = options

    if options.compile:
        if not options.verbose:
            q = True
        else:
            q = False
        compile_dir(".", force=options.force, quiet=q)
    
try:
    import psyco
    psyco.full()
except ImportError:
    if options.verbose:
        print "Could not import psyco, ignoring..."

    sf = Soulforge(0)
    sf.MainLoop()
