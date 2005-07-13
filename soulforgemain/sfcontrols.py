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
from wx.lib import buttons
from libsoulforge import headerdata

SFSTAT_BUTTON = 201
SFPOOL_BUTTON = 301

class sfdot(buttons.GenToggleButton):
    def __init__(self, parent, ID, label,
                 pos = wx.DefaultPosition, size = wx.DefaultSize,
                 style = 0, validator = wx.DefaultValidator,
                 name = "genbutton"):
        cstyle = style
        if cstyle == 0:
            cstyle = wx.NO_BORDER
        wx.PyControl.__init__(self, parent, ID, pos, size, cstyle, validator, name)

        self.up = True
        self.hasFocus = False
        self.bezelWidth = 0
        self.useFocusInd = False

        self.InheritAttributes()
        self.SetBestFittingSize(size)
        self.InitColours()

        self.Bind(wx.EVT_LEFT_DOWN,        self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP,          self.OnLeftUp)
        if wx.Platform == '__WXMSW__':
            self.Bind(wx.EVT_LEFT_DCLICK,  self.OnLeftDown)
        self.Bind(wx.EVT_MOTION,           self.OnMotion)
        self.Bind(wx.EVT_SET_FOCUS,        self.OnGainFocus)
        self.Bind(wx.EVT_KILL_FOCUS,       self.OnLoseFocus)
        self.Bind(wx.EVT_KEY_DOWN,         self.OnKeyDown)
        self.Bind(wx.EVT_KEY_UP,           self.OnKeyUp)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_PAINT,            self.OnPaint)

    def OnPoint(self, event):
        (width, height) = self.GetClientSizeTuple()
	x = width - 1
	y = height - 1
	df = wx.BufferedPaintDC(self)
	dc.Clear()
	self.DrawBezel(dc, 0, 0, x, y)

    def DrawBezel(self, dc, x1, y1, x2, y2):
	dc.SetPen(wx.BLACK_PEN)
	if self.up:
	    dc.SetBrush(wx.Brush(self.GetBackgroundColour(), wx.SOLID))
	else:
	    dc.SetBrush(wx.Brush(wx.BLACK, wx.SOLID))
	dc.DrawEllipseRect(wx.Rect(self.bezelWidth+2,self.bezelWidth+2,x2-self.bezelWidth*2-4,y2-self.bezelWidth*2-4))

    def DoGetBestSize(self):
        width = 15
	height = 15
	return (width, height)

    def DrawFocusIndicator(self, dc, w, h):
        pass

    def OnLeftDown(self, event):
        if not self.IsEnabled():
            return
        self.saveUp = self.up
        self.up = not self.up
        self.CaptureMouse()
        self.SetFocus()


class sfstat(wx.Panel):
    def __init__(self,parent,ID,label="",orient = wx.HORIZONTAL,buttons = headerdata.SF_SFSTAT_BUTTONS,alternate = False):
        wx.Panel.__init__(self,parent,ID,wx.DefaultPosition,wx.DefaultSize)

	self.btns = buttons
	self.value = 0
	self.alternate = alternate

	root = wx.BoxSizer(orient)

	if label != "":
	    self.label = wx.StaticText(self,-1,label)
	    root.Add(self.label,1,wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL)

	self.buttons = []

	for i in range(self.btns):
	    if alternate:
	        pass
	    else:
	        self.buttons.append(sfdot(self,(SFSTAT_BUTTON + i),""))
		wx.EVT_BUTTON(self,(SFSTAT_BUTTON+i),self.onclick)
	    root.Add(self.buttons[i],0,wx.ALIGN_CENTER_VERTICAL)

	self.recalc()

	self.SetSizer(root)

    def onclick(self,event):
        n = event.GetId() - SFSTAT_BUTTON + 1
	if n == self.value:
	    self.value = self.value - 1
	else:
	    self.value = n
	self.recalc()

    def recalc(self):
        for i in range(self.value):
	    self.buttons[i].SetValue(1)
	for i in range(self.value,len(self.buttons)):
	    self.buttons[i].SetValue(0)
	    
    def setvalue(self,v):
        self.value = v
	self.recalc()

class sfpool(wx.Panel):
    def __init__(self,parent,ID,rows = headerdata.SF_SFPOOL_ROWS,cols = headerdata.SF_SFPOOL_COLS,alternate = False):
        wx.Panel.__init__(self,parent,ID,wx.DefaultPosition,wx.DefaultSize)

	self.value = 0
	self.alternate = alternate
	self.rows = rows
	self.cols = cols
	self.total = rows*cols

	root = wx.GridSizer(rows,cols,1,1)

	self.buttons = []
	self.dummy = []
	self.state = []

	for i in range(self.total):
	    if alternate:
	        self.buttons.append(wx.RadioButton(self,(SFPOOL_BUTTON + i),"",wx.DefaultPosition,wx.DefaultSize,wx.RB_GROUP))
		self.dummy.append(wx.RadioButton(self,-1,"",wx.DefaultPosition,wx.DefaultSize,wx.RB_SINGLE))
		self.dummy[i].Show(False)
		self.dummy[i].SetValue(True)
		self.state.append(False)
		wx.EVT_RADIOBUTTON(self,(SFPOOL_BUTTON + i),self.onclick)
	    else:
	        self.buttons.append(wx.CheckBox(self,(SFPOOL_BUTTON + i),""))
		wx.EVT_CHECKBOX(self,(SFPOOL_BUTTON + i),self.onclick)
	    root.Add(self.buttons[i],0,wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL)
	
	self.SetSizer(root)

    def onclick(self,event):
        n = event.GetId() - SFPOOL_BUTTON
        if self.alternate:
	    if self.state[n]:
	        self.dummy[n].SetValue(True)
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
	    self.buttons[i].SetValue(True)
	for i in range(self.value,len(self.buttons)):
	    self.buttons[i].SetValue(False)
	    if self.alternate:
	        self.dummy[i].SetValue(True)
