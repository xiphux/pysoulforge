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
from soulforge.libsoulforge import headerdata
from soulforge.soulforgemain import sfcontrols,sfuniverses

SFSHEET_OK = 401
SFSHEET_CANCEL = 402

class sfsheet(wx.Frame):
    def __init__(self,parent,ID,univ):
        wx.Frame.__init__(self, parent, ID, univ, wx.DefaultPosition, wx.DefaultSize)

	self.universe = univ

	pan = wx.Panel(self,-1)
	ts = wx.BoxSizer(wx.VERTICAL)
	ts.Add(pan,1,wx.EXPAND|wx.ALL)
	self.SetSizer(ts)

	root = wx.BoxSizer(wx.VERTICAL)

	sh = sfuniverses.universe_sheets[univ]
	self.sheet = sh(pan,-1)

	root.Add(self.sheet,0,wx.EXPAND)

	controls = wx.BoxSizer(wx.HORIZONTAL)
	self.okbutton = wx.Button(pan,SFSHEET_OK, _("Ok"))
	controls.Add(self.okbutton,1,wx.EXPAND)

	controls.Add(wx.Button(pan,SFSHEET_CANCEL, _("Cancel")),1,wx.EXPAND)

	root.Add(controls,0,wx.EXPAND)

	pan.SetSizer(root)
	self.Fit()
	self.Centre(wx.BOTH)

	wx.EVT_BUTTON(self,SFSHEET_OK,self.onok)
	wx.EVT_BUTTON(self,SFSHEET_CANCEL,self.oncancel)

    def oncancel(self,event):
        self.Destroy()

    def onok(self,event):
        event.Skip()
