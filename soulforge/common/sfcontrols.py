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
from soulforge.lib import headerdata

SFSTAT_BUTTON = 201
SFPOOL_BUTTON = 301
SFHEALTH_BUTTON = 801

class sfdot(buttons.GenToggleButton):
    def __init__(self, parent, ID, label,
                 pos = wx.DefaultPosition, size = wx.DefaultSize,
                 style = 0, validator = wx.DefaultValidator,
                 name = "sfdot"):
        cstyle = style
        if cstyle == 0:
            cstyle = wx.NO_BORDER
        wx.PyControl.__init__(self, parent, ID, pos, size, cstyle, validator, name)

        self.up = True
        self.hasFocus = False
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
        self.Bind(wx.EVT_PAINT,            self.OnPaint)

    def OnPaint(self, event):
        (width, height) = self.GetClientSizeTuple()
	x = width - 1
	y = height - 1
	dc = wx.BufferedPaintDC(self)
	dc.SetBackground(wx.Brush(self.GetBackgroundColour(), wx.SOLID))
	dc.Clear()
	self.DrawBezel(dc, 0, 0, x, y)

    def DrawBezel(self, dc, x1, y1, x2, y2):
	dc.SetPen(self.shadowPen)
        if self.up:
	    dc.SetBrush(wx.Brush(self.GetBackgroundColour(), wx.SOLID))
	    dc.DrawEllipseRect(wx.Rect(3,3,y2-4,y2-4))
	    dc.SetPen(wx.BLACK_PEN)
	    dc.SetBrush(wx.Brush(self.GetBackgroundColour(), wx.TRANSPARENT))
	    dc.DrawEllipseRect(wx.Rect(2,2,y2-4,y2-4))
	else:
	    dc.SetBrush(wx.Brush(self.shadowPen.GetColour(), wx.SOLID))
	    dc.DrawEllipseRect(wx.Rect(2,2,y2-4,y2-4))
	    dc.SetPen(wx.BLACK_PEN)
	    dc.SetBrush(wx.Brush(wx.BLACK, wx.SOLID))
	    dc.DrawEllipseRect(wx.Rect(3,3,y2-4,y2-4))

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

    def OnMotion(self, event):
        pass


class sfbox(buttons.GenToggleButton):
    def __init__(self, parent, ID, label,
                 pos = wx.DefaultPosition, size = wx.DefaultSize,
                 style = 0, validator = wx.DefaultValidator,
                 name = "sfbox"):
        cstyle = style
        if cstyle == 0:
            cstyle = wx.NO_BORDER
        wx.PyControl.__init__(self, parent, ID, pos, size, cstyle, validator, name)

        self.up = True
        self.hasFocus = False
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
        self.Bind(wx.EVT_PAINT,            self.OnPaint)

    def OnPaint(self, event):
        (width, height) = self.GetClientSizeTuple()
	x = width - 1
	y = height - 1
	dc = wx.BufferedPaintDC(self)
	dc.SetBackground(wx.Brush(self.GetBackgroundColour(), wx.SOLID))
	dc.Clear()
	self.DrawBezel(dc, 0, 0, x, y)
	self.DrawMarker(dc, 0, 0, x, y)

    def DrawMarker(self, dc, x1, y1, x2, y2):
	if not self.up:
            dc.SetPen(wx.BLACK_PEN)
	    dc.DrawLine(x2-2, 3, 3, y2-2)

    def DrawBezel(self, dc, x1, y1, x2, y2):
	dc.SetBrush(wx.Brush(self.GetBackgroundColour(), wx.TRANSPARENT))
	dc.SetPen(self.shadowPen)
	if self.up:
	    dc.DrawRectangle(3,3,y2-4,y2-4)
	    dc.SetPen(wx.BLACK_PEN)
	    dc.DrawRectangle(2,2,y2-4,y2-4)
	else:
	    dc.DrawRectangle(2,2,y2-4,y2-4)
	    dc.SetPen(wx.BLACK_PEN)
	    dc.DrawRectangle(3,3,y2-4,y2-4)

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

    def OnMotion(self, event):
        pass

class sftristate(buttons.GenToggleButton):
    def __init__(self, parent, ID, label,
                 pos = wx.DefaultPosition, size = wx.DefaultSize,
                 style = 0, validator = wx.DefaultValidator,
                 name = "sftristate"):
        cstyle = style
        if cstyle == 0:
            cstyle = wx.NO_BORDER
        wx.PyControl.__init__(self, parent, ID, pos, size, cstyle, validator, name)

        self.state = 0
	self.up = True
	self.saveUp = False
        self.hasFocus = False
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
        self.Bind(wx.EVT_PAINT,            self.OnPaint)

    def setvalue(self, value):
        if value > 2 or value < 0:
	    return
        self.state = value
	self.SetFocus()

    def OnPaint(self, event):
        (width, height) = self.GetClientSizeTuple()
	x = width - 1
	y = height - 1
	dc = wx.BufferedPaintDC(self)
	dc.SetBackground(wx.Brush(self.GetBackgroundColour(), wx.SOLID))
	dc.Clear()
	self.DrawBezel(dc, 0, 0, x, y)
	self.DrawMarker(dc, 0, 0, x, y)

    def DrawMarker(self, dc, x1, y1, x2, y2):
	if self.state > 0:
            dc.SetPen(wx.BLACK_PEN)
	    dc.DrawLine(x2-1, 3, 3, y2-2)
	    if self.state > 1:
	        dc.DrawLine(3, 3, x2, y2-1)

    def DrawBezel(self, dc, x1, y1, x2, y2):
	dc.SetBrush(wx.Brush(self.GetBackgroundColour(), wx.TRANSPARENT))
	dc.SetPen(self.shadowPen)
	if self.state > 0:
	    dc.DrawRectangle(2,2,y2-4,y2-4)
	    dc.SetPen(wx.BLACK_PEN)
	    dc.DrawRectangle(3,3,y2-4,y2-4)
	else:
	    dc.DrawRectangle(3,3,y2-4,y2-4)
	    dc.SetPen(wx.BLACK_PEN)
	    dc.DrawRectangle(2,2,y2-4,y2-4)

    def DoGetBestSize(self):
        width = 15
	height = 15
	return (width, height)

    def DrawFocusIndicator(self, dc, w, h):
        pass

    def OnLeftDown(self, event):
        if not self.IsEnabled():
            return
        self.state += 1
	if self.state > 2:
	    self.state = 0
        self.CaptureMouse()
        self.SetFocus()

    def OnMotion(self, event):
        pass

    def GetValue(self):
        return self.state


class sfstat(wx.Panel):
    def __init__(self,parent,ID,label="",orient = wx.HORIZONTAL,buttons = headerdata.SF_SFSTAT_BUTTONS,alternate = False):
        wx.Panel.__init__(self,parent,ID,wx.DefaultPosition,wx.DefaultSize)

	self.btns = buttons
	self.value = 0
	self.alternate = alternate

	root = wx.BoxSizer(orient)

	if label != "":
	    self.label = wx.StaticText(self,-1,label)
	    root.Add(self.label,self.btns,wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL)

	self.buttons = []

	for i in range(self.btns):
	    if alternate:
	        self.buttons.append(sfbox(self,(SFSTAT_BUTTON + i),""))
	    else:
	        self.buttons.append(sfdot(self,(SFSTAT_BUTTON + i),""))
            wx.EVT_BUTTON(self,(SFSTAT_BUTTON+i),self.onclick)
	    root.Add(self.buttons[i],1,wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL)

	self.recalc()

	self.SetSizer(root)

    def onclick(self,event):
        n = event.GetId() - SFSTAT_BUTTON + 1
	if n == self.value:
	    self.value = self.value - 1
	else:
	    self.value = n
	if headerdata.options.debug:
	    print self.value
	self.recalc()

    def recalc(self):
        for i in range(self.value):
	    self.buttons[i].SetValue(1)
	for i in range(self.value,len(self.buttons)):
	    self.buttons[i].SetValue(0)
	    
    def setvalue(self,v):
        self.value = v
	self.recalc()

class sfhealth(wx.Panel):
    def __init__(self,parent,ID,label="",orient = wx.VERTICAL,buttons = headerdata.SF_SFHEALTH_LEVELS):
        wx.Panel.__init__(self,parent,ID,wx.DefaultPosition,wx.DefaultSize)

	self.btns = buttons
	self.normal = 0
	self.aggravated = 0

	root = wx.BoxSizer(orient)

	if label != "":
	    self.label = wx.StaticText(self,-1,label)
	    root.Add(self.label,self.btns,wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL)

	self.buttons = []

	for i in range(self.btns):
	    self.buttons.append(sftristate(self,(SFHEALTH_BUTTON + i),""))
	    wx.EVT_BUTTON(self,(SFHEALTH_BUTTON+i),self.onclick)
	    root.Add(self.buttons[i],1,wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL)

	self.SetSizer(root)

    def onclick(self,event):
        self.recalc()

    def recalc(self):
        n = 0
	a = 0
	for i in range(self.btns):
	    s = self.buttons[i].GetValue()
	    if headerdata.options.debug:
	        print s
	    if s == 2:
	        a += 1
	    elif s == 1:
	        n += 1
	self.normal = n
	self.aggravated = a
	if headerdata.options.debug:
	    print "N: " + str(self.normal)
	    print "A: " + str(self.aggravated)

    def setnormal(self,norm):
        self.normal = norm
	self.fillboxes()

    def setaggravated(self,agg):
        self.aggravated = agg
	self.fillboxes()

    def fillboxes(self):
        for i in range(self.aggravated):
	    if i >= self.btns:
	        return
	    self.buttons[i].setvalue(2)
	sum = self.aggravated + self.normal
	for i in range(self.aggravated,sum):
	    if i >= self.btns:
	        return
	    self.buttons[i].setvalue(1)
	if sum < self.btns:
	    for i in range(sum,self.btns):
	        if i >= self.btns:
		    return
	        self.buttons[i].setvalue(0)

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

	for i in range(self.total):
	    if alternate:
	        self.buttons.append(sfdot(self,(SFPOOL_BUTTON + i),""))
	    else:
	        self.buttons.append(sfbox(self,(SFPOOL_BUTTON + i),""))
	    wx.EVT_BUTTON(self,(SFPOOL_BUTTON + i),self.onclick)
	    root.Add(self.buttons[i],0,wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL)
	
	self.SetSizer(root)

    def onclick(self,event):
        self.recalc()

    def recalc(self):
        n = 0
	for i in range(self.total):
	    if self.buttons[i].GetValue():
	        n += 1
        self.value = n
	if headerdata.options.debug:
	    print self.value

    def setvalue(self,v):
        self.value = v
	for i in range(self.value):
	    self.buttons[i].SetValue(True)
	for i in range(self.value,len(self.buttons)):
	    self.buttons[i].SetValue(False)
