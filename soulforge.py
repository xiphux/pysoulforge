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

import sys
from optparse import OptionParser
from compileall import compile_dir
import wx
from soulforge.lib import headerdata
from soulforge.common import sfrootframe

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
    parser.add_option("-d", "--debug", action="store_true",
      dest="debug", help="print debugging info")
    parser.add_option("-p", "--profile", action="store", type="string",
      dest="profile", help="gather performance profiling info", metavar="PROFILE")
    parser.add_option("-s", "--pstats", action="store", type="string",
      dest="stats", help="parse profiling output", metavar="PROFILE")
    parser.set_defaults(verbose=False)
    parser.set_defaults(force=False)
    parser.set_defaults(compile=False)
    parser.set_defaults(debug=False)
    parser.set_defaults(parser=False)
    parser.set_defaults(profile='')
    parser.set_defaults(stats='')
    (options, args) = parser.parse_args()

    headerdata.options = options

    if options.compile:
        if not options.verbose:
            q = True
        else:
            q = False
        compile_dir(".", force=options.force, quiet=q)

    if options.debug:
        print "Debugging output enabled"
        print "If the debugging output shows any suspicious errors,"
        print "please email the output to the author."
        print "Verbose output automatically enabled"
        options.verbose = 1

    if options.verbose:
        print "Verbose execution enabled"

    if options.stats:
        import pstats
	p = pstats.Stats(options.stats)
	p.sort_stats('cumulative').print_stats(10)
	p.sort_stats('time').print_stats(10)
	sys.exit()

try:
    import psyco
    psyco.full()
except ImportError:
    if options.verbose:
        print "Could not import psyco, ignoring..."

    sf = Soulforge(0)

    if options.profile:
        print "Program execution will be profiled."
	print "Expect it to run a lot slower."
	import profile
	profile.run('sf.MainLoop()', options.profile)
    else:	
        sf.MainLoop()
