#!/usr/bin/env python

from wxPython.wx import *
from soulforgemain.sfrootframe import sfrootframe

class Soulforge(wxApp):
    def OnInit(self):
        sframe = sfrootframe(NULL, -1, u"Soulforge")
	sframe.Show(true)
	self.SetTopWindow(sframe)
	return true

sf = Soulforge(0)
sf.MainLoop()
