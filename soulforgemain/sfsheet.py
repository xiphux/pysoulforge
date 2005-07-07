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

import sfcontrols
from wxPython.wx import *
from wxPython.xrc import *
from sheets import vampire_the_masquerade

SFSHEET_OK = 401
SFSHEET_CANCEL = 402

class sfsheet(wxFrame):
    def __init__(self,parent,ID,title,resource):
        wxFrame.__init__(self, parent, ID, title, wxDefaultPosition, wxDefaultSize)

	root = wxBoxSizer(wxVERTICAL)

	sheet = vampire_the_masquerade.vampire_the_masquerade(self,-1)

	root.Add(sheet,0,wxEXPAND)

	controls = wxBoxSizer(wxHORIZONTAL)
	self.okbutton = wxButton(self,SFSHEET_OK,u"Ok")
	controls.Add(self.okbutton,1,wxEXPAND)

	controls.Add(wxButton(self,SFSHEET_CANCEL,u"Cancel"),1,wxEXPAND)

	root.Add(controls,0,wxEXPAND)

	self.SetSizerAndFit(root)
	self.Centre(wxBOTH)

	EVT_BUTTON(self,SFSHEET_OK,self.onok)
	EVT_BUTTON(self,SFSHEET_CANCEL,self.oncancel)

    def oncancel(self,event):
        self.Destroy()

    def onok(self,event):
        pass
