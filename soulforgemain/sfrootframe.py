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

from wxPython.wx import *
import dieroller

SFROOTFRAME_ABOUT = 101
SFROOTFRAME_QUIT = 102
SFROOTFRAME_DIEROLLER = 103

class sfrootframe(wxFrame):
    def __init__(self, parent, ID, title):
        wxFrame.__init__(self, parent, ID, title, wxDefaultPosition, wxDefaultSize)

	filemenu = wxMenu()
	filemenu.Append(SFROOTFRAME_QUIT, u"E&xit", u"Quit Soulforge")

	toolsmenu = wxMenu()
	toolsmenu.Append(SFROOTFRAME_DIEROLLER, u"&Dieroller", u"Dieroller")

	helpmenu = wxMenu()
	helpmenu.Append(SFROOTFRAME_ABOUT, u"&About", u"About Soulforge")

	menubar = wxMenuBar()
	menubar.Append(filemenu, u"&File")
	menubar.Append(toolsmenu, u"&Tools")
	menubar.Append(helpmenu, u"&Help")
	
	self.SetMenuBar(menubar)
	self.Centre(wxBOTH)

	EVT_MENU(self,SFROOTFRAME_QUIT,self.onquit)
	EVT_MENU(self,SFROOTFRAME_ABOUT,self.onabout)
	EVT_MENU(self,SFROOTFRAME_DIEROLLER,self.ondieroller)

    def onquit(self,event):
        self.Close(true)

    def onabout(self,event):
        abt = wxMessageDialog(self,u"Soulforge by Christopher Han\nCopyright (C) 2005\nLicensed under the GNU GPL",u"About Soulforge",wxOK)
	abt.ShowModal()
	abt.Destroy()

    def ondieroller(self,event):
        dr = dieroller.dieroller(self,-1,u"Dieroller")
	dr.Show(true)
