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
import sfuniverses

SFUNIVERSECHOOSER_OK = 601
SFUNIVERSECHOOSER_CANCEL = 602

class sfuniversechooser(wxDialog):
    def __init__(self,parent,ID,title="Select universe"):
        wxDialog.__init__(self,parent,ID,title)

	self.universe = None
	
	root = wxBoxSizer(wxVERTICAL)
	self.uchooser = wxChoice(self,-1,wxDefaultPosition,wxDefaultSize,sfuniverses.universes)
	root.Add(self.uchooser,1,wxEXPAND)

	bbox = wxBoxSizer(wxHORIZONTAL)
	bbox.Add(wxButton(self,SFUNIVERSECHOOSER_OK,u"Ok"),1,wxEXPAND)
	bbox.Add(wxButton(self,SFUNIVERSECHOOSER_CANCEL,u"Cancel"),1,wxEXPAND)
	root.Add(bbox,0,wxEXPAND)

	self.SetSizerAndFit(root)
	self.Centre(wxBOTH)

	EVT_BUTTON(self,SFUNIVERSECHOOSER_OK,self.onok)
	EVT_BUTTON(self,SFUNIVERSECHOOSER_CANCEL,self.oncancel)

    def onok(self,event):
        self.universe = self.uchooser.GetStringSelection()
	self.EndModal(wxID_OK)

    def oncancel(self,event):
        self.EndModal(wxID_CANCEL)
