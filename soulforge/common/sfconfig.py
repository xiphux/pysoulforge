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

import wx
from soulforge.lib import headerdata

SFCONFIG_OK = 701
SFCONFIG_CANCEL = 702
SFCONFIG_APPLY = 703
SFCONFIG_COMPRESS = 704
SFCONFIG_RNG = 705

class sfconfig(wx.Dialog):
    def __init__(self,parent,ID,title=_("Soulforge config")):
        wx.Dialog.__init__(self, parent, ID, title)

	self.modified = False
	self.config = wx.Config.Get()

	pan = wx.Panel(self,-1)
	ts = wx.BoxSizer(wx.VERTICAL)
	ts.Add(pan,1,wx.EXPAND|wx.ALL)
	self.SetSizer(ts)

        root = wx.BoxSizer(wx.VERTICAL)

	zipbox = wx.BoxSizer(wx.VERTICAL)
	str = _("Algorithm for transparently compressing") + " *" + headerdata.SF_COMPRESSED_EXT + " " + _("files:")
	zipbox.Add(wx.StaticText(pan,-1,str),0,wx.ALIGN_LEFT)
	self.compress = wx.Choice(pan,SFCONFIG_COMPRESS,wx.DefaultPosition,wx.DefaultSize,headerdata.SF_COMPRESSION_STRINGS)
	self.compress.SetStringSelection(self.config.Read(headerdata.SF_CONFIGKEY_COMPRESS,headerdata.SF_CONFIGDEFAULT_COMPRESS))
	zipbox.Add(self.compress,1,wx.EXPAND)
	root.Add(zipbox,0,wx.EXPAND)

	rngbox = wx.BoxSizer(wx.VERTICAL)
	rngl = wx.StaticText(pan,-1,"Preferred pseudo-random number generator:")
	rngbox.Add(rngl,0,wx.ALIGN_LEFT)
	self.rng = wx.Choice(pan,SFCONFIG_RNG,wx.DefaultPosition,wx.DefaultSize,headerdata.SF_DIEROLLER_RNGSTRINGS)
	self.rng.SetStringSelection(self.config.Read(headerdata.SF_CONFIGKEY_RNG,headerdata.SF_CONFIGDEFAULT_RNG))
	rngbox.Add(self.rng,1,wx.EXPAND)
	root.Add(rngbox,0,wx.EXPAND)

	bbox = wx.BoxSizer(wx.HORIZONTAL)
	self.apply = wx.Button(pan,SFCONFIG_APPLY,_("Apply"))
	bbox.Add(self.apply,1,wx.EXPAND)
	bbox.Add(wx.Button(pan,SFCONFIG_CANCEL,_("Cancel")),1,wx.EXPAND)
	self.ok = wx.Button(pan,SFCONFIG_OK,_("Ok"))
	bbox.Add(self.ok,1,wx.EXPAND)
	root.Add(bbox,0,wx.EXPAND)

	pan.SetSizer(root)
	self.Fit()
	self.Centre(wx.BOTH)

	self.updategui()

	wx.EVT_BUTTON(self,SFCONFIG_OK,self.onok)
	wx.EVT_BUTTON(self,SFCONFIG_CANCEL,self.oncancel)
	wx.EVT_BUTTON(self,SFCONFIG_APPLY,self.onapply)
	wx.EVT_CHOICE(self,SFCONFIG_COMPRESS,self.onchange)
	wx.EVT_CHOICE(self,SFCONFIG_RNG,self.onchange)

    def onchange(self,event):
        self.modified = True
	self.updategui()

    def writesettings(self):
	self.config.Write(headerdata.SF_CONFIGKEY_COMPRESS,self.compress.GetStringSelection())
	self.config.Write(headerdata.SF_CONFIGKEY_RNG,self.rng.GetStringSelection())
	self.config.Flush(True)

    def onok(self,event):
        self.writesettings()
	self.EndModal(wx.ID_OK)

    def oncancel(self,event):
        self.EndModal(wx.ID_CANCEL)

    def onapply(self,event):
        self.writesettings()
	self.modified = False
	self.updategui()

    def updategui(self):
        self.apply.Enable(self.modified)
