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

SFSTAT_BUTTON = 201

class sfstat(wxPanel):
    def __init__(self,parent,ID,label,orient = wxHORIZONTAL,buttons = 5,alternate = False):
        wxPanel.__init__(self,parent,ID,wxDefaultPosition,wxDefaultSize)

	self.value = 0
	self.alternate = alternate

	root = wxBoxSizer(orient)

	self.label = wxStaticText(self,-1,label)

	root.Add(self.label,1,wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL)

	self.buttons = []
	self.dummy = []

	for i in range(buttons):
	    if alternate:
	        self.buttons.append(wxCheckBox(self,(SFSTAT_BUTTON + i),""))
	        self.Connect((SFSTAT_BUTTON + i),-1,wxEVT_COMMAND_CHECKBOX_CLICKED,self.onclick)
	    else:
	        self.buttons.append(wxRadioButton(self,(SFSTAT_BUTTON + i),"",wxDefaultPosition,wxDefaultSize,wxRB_GROUP))
		self.dummy.append(wxRadioButton(self,-1,""))
		self.dummy[i].Show(false)
	        self.Connect((SFSTAT_BUTTON + i),-1,wxEVT_COMMAND_RADIOBUTTON_SELECTED,self.onclick)
	    root.Add(self.buttons[i],0,wxALIGN_CENTER_VERTICAL)

	self.recalc()

	self.SetSizer(root)

    def onclick(self,event):
        n = event.GetId() - SFSTAT_BUTTON
	if (n+1) == self.value:
	    self.value -= 1
	else:
	    self.value = n+1
	self.recalc()

    def recalc(self):
        for i in range(self.value):
	    self.buttons[i].SetValue(true)
	for i in range(self.value,len(self.buttons)):
	    self.buttons[i].SetValue(false)
	    if not self.alternate:
	        self.dummy[i].SetValue(true)
	    
    def setvalue(self,v):
        self.value = v
	self.recalc()
