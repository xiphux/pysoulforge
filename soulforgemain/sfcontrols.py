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
SFPOOL_BUTTON = 301

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

class sfpool(wxPanel):
    def __init__(self,parent,ID,rows = 2,cols = 10,alternate = False):
        wxPanel.__init__(self,parent,ID,wxDefaultPosition,wxDefaultSize)

	self.value = 0
	self.alternate = alternate
	self.rows = rows
	self.cols = cols
	self.total = rows*cols

	root = wxGridSizer(rows,cols,1,1)

	self.buttons = []
	self.dummy = []
	self.state = []

	for i in range(self.total):
	    if alternate:
	        self.buttons.append(wxRadioButton(self,(SFPOOL_BUTTON + i),"",wxDefaultPosition,wxDefaultSize,wxRB_GROUP))
		self.dummy.append(wxRadioButton(self,-1,""))
		self.dummy[i].Show(false)
		self.dummy[i].SetValue(true)
		self.state.append(False)
		self.Connect((SFPOOL_BUTTON + i),-1,wxEVT_COMMAND_RADIOBUTTON_SELECTED,self.onclick)
	    else:
	        self.buttons.append(wxCheckBox(self,(SFPOOL_BUTTON + i),""))
		self.Connect((SFPOOL_BUTTON + i),-1,wxEVT_COMMAND_CHECKBOX_CLICKED,self.onclick)
	    root.Add(self.buttons[i],0,wxALIGN_CENTER_VERTICAL|wxALIGN_CENTER_HORIZONTAL)
	
	self.SetSizer(root)

    def onclick(self,event):
        n = event.GetId() - SFPOOL_BUTTON
        if self.alternate:
	    if self.state[n]:
	        self.dummy[n].SetValue(true)
	    self.state[n] = self.buttons[n].GetValue()
        self.recalc()

    def recalc(self):
        n = 0
	for i in range(self.total):
	    if self.buttons[i].GetValue():
	        n += 1
            if self.alternate:
	        self.state[i] = self.buttons[i].GetValue()
        self.value = n

    def setvalue(self,v):
        self.value = v
	for i in range(self.value):
	    self.buttons[i].SetValue(true)
	for i in range(self.value,len(self.buttons)):
	    self.buttons[i].SetValue(false)
	    if self.alternate:
	        self.dummy[i].SetValue(true)
