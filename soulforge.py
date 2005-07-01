#!/usr/bin/env python

from wxPython.wx import *
from soulforgemain import sfrootframe

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

sf = Soulforge(0)
sf.MainLoop()
