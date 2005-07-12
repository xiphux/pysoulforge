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

from wxPython.wx import wxDialog,wxBoxSizer,wxVERTICAL,wxHORIZONTAL,wxButton,wxCheckBox,wxConfig,EVT_BUTTON,EVT_CHECKBOX,wxEXPAND,wxBOTH,wxID_OK,wxID_CANCEL
from libsoulforge import headerdata

SFCONFIG_OK = 701
SFCONFIG_CANCEL = 702
SFCONFIG_APPLY = 703
SFCONFIG_COMPRESS = 704

class sfconfig(wxDialog):
    def __init__(self,parent,ID,title=_("Soulforge config")):
        wxDialog.__init__(self, parent, ID, title)

	self.modified = False
	self.config = wxConfig.Get()

        root = wxBoxSizer(wxVERTICAL)
	str = _("Transparently compress") + " *" + headerdata.SF_COMPRESSED_EXT + " " + _("files")
	self.compress = wxCheckBox(self,SFCONFIG_COMPRESS,str)
	self.compress.SetValue(self.config.ReadInt(headerdata.SF_CONFIGKEY_COMPRESS,headerdata.SF_CONFIGDEFAULT_COMPRESS))
	root.Add(self.compress,0,wxEXPAND)

	bbox = wxBoxSizer(wxHORIZONTAL)
	self.apply = wxButton(self,SFCONFIG_APPLY,_("Apply"))
	bbox.Add(self.apply,1,wxEXPAND)
	bbox.Add(wxButton(self,SFCONFIG_CANCEL,_("Cancel")),1,wxEXPAND)
	self.ok = wxButton(self,SFCONFIG_OK,_("Ok"))
	bbox.Add(self.ok,1,wxEXPAND)
	root.Add(bbox,0,wxEXPAND)

	self.SetSizerAndFit(root)
	self.Centre(wxBOTH)

	self.updategui()

	EVT_BUTTON(self,SFCONFIG_OK,self.onok)
	EVT_BUTTON(self,SFCONFIG_CANCEL,self.oncancel)
	EVT_BUTTON(self,SFCONFIG_APPLY,self.onapply)
	EVT_CHECKBOX(self,SFCONFIG_COMPRESS,self.onchange)

    def onchange(self,event):
        self.modified = True
	self.updategui()

    def writesettings(self):
        if self.compress.GetValue():
	    self.config.WriteInt(headerdata.SF_CONFIGKEY_COMPRESS,1)
	else:
	    self.config.WriteInt(headerdata.SF_CONFIGKEY_COMPRESS,0)
	self.config.Flush(True)

    def onok(self,event):
        self.writesettings()
	self.EndModal(wxID_OK)

    def oncancel(self,event):
        self.EndModal(wxID_CANCEL)

    def onapply(self,event):
        self.writesettings()
	self.modified = False
	self.updategui()

    def updategui(self):
        self.apply.Enable(self.modified)
