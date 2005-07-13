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
from libsoulforge import dicepool, headerdata

DIEROLLER_CLOSE = 104
DIEROLLER_ROLL = 105
DIEROLLER_POOL = 106
DIEROLLER_FACES = 107
DIEROLLER_RNG = 108
DIEROLLER_BOTCH = 109
DIEROLLER_TAB = 110
DIEROLLER_DIFF = 111

class dieroller(wx.Frame):
    def __init__(self,parent,ID,title):
        wx.Frame.__init__(self,parent,ID,title,wx.DefaultPosition,wx.DefaultSize)

	self.dicepool = dicepool.dicepool()

	root = wx.BoxSizer(wx.HORIZONTAL)

	controls = wx.BoxSizer(wx.VERTICAL)

	poolbox = wx.BoxSizer(wx.HORIZONTAL)
	poolbox.Add(wx.StaticText(self,-1,_("Dice pool:")),0,wx.ALIGN_CENTER_VERTICAL)
	self.poolctl = wx.SpinCtrl(self,DIEROLLER_POOL,u"",wx.DefaultPosition,wx.DefaultSize,0,1,99,self.dicepool.pool)
	poolbox.Add(self.poolctl,1,wx.ALIGN_CENTER_VERTICAL)
	controls.Add(poolbox,1,wx.EXPAND)

	facebox = wx.BoxSizer(wx.HORIZONTAL)
	facebox.Add(wx.StaticText(self,-1,_("Die faces:")),0,wx.ALIGN_CENTER_VERTICAL)
	self.facectl = wx.SpinCtrl(self,DIEROLLER_FACES,u"",wx.DefaultPosition,wx.DefaultSize,0,2,99,self.dicepool.faces)
	facebox.Add(self.facectl,1,wx.ALIGN_CENTER_VERTICAL)
	controls.Add(facebox,1,wx.EXPAND)

	rngbox = wx.BoxSizer(wx.VERTICAL)
	rngbox.Add(wx.StaticText(self,-1,_("Pseudo-random number generator:")),0)
	rngstrings = [ _("Mersenne Twister"), _("Wichmann-Hill"), _("urandom()") ]
	self.rngctl = wx.Choice(self,DIEROLLER_RNG,wx.DefaultPosition,wx.DefaultSize,rngstrings)
	rngbox.Add(self.rngctl,1,wx.EXPAND)
	controls.Add(rngbox,0,wx.EXPAND)
	
	self.botchctl = wx.CheckBox(self,DIEROLLER_BOTCH, _("Botches"))
	self.botchctl.SetValue(self.dicepool.botch)
	controls.Add(self.botchctl,0,wx.EXPAND)

	self.tabctl = wx.CheckBox(self,DIEROLLER_TAB, _("Tabulate"))
	self.tabctl.SetValue(self.dicepool.tabulate)
	controls.Add(self.tabctl,0,wx.EXPAND)

	diffbox = wx.BoxSizer(wx.HORIZONTAL)
	self.difflabel = wx.StaticText(self,-1, _("Difficulty:"))
	diffbox.Add(self.difflabel,0,wx.ALIGN_CENTER_VERTICAL)
	self.diffctl = wx.SpinCtrl(self,DIEROLLER_DIFF,u"",wx.DefaultPosition,wx.DefaultSize,0,1,self.dicepool.faces,6)
	diffbox.Add(self.diffctl,1,wx.ALIGN_CENTER_VERTICAL)
	controls.Add(diffbox,1,wx.EXPAND)
	self.difflabel.Enable(self.dicepool.tabulate)
	self.diffctl.Enable(self.dicepool.tabulate)

	roll = wx.Button(self,DIEROLLER_ROLL, _("Roll"))
	controls.Add(roll,0,wx.EXPAND)

	root.Add(controls,1,wx.EXPAND)

	results = wx.BoxSizer(wx.VERTICAL)

	self.resultbox = wx.TextCtrl(self,-1,u"",wx.DefaultPosition,wx.DefaultSize,wx.TE_MULTILINE|wx.TE_READONLY)
	results.Add(self.resultbox,2,wx.EXPAND)

	finalbox = wx.BoxSizer(wx.HORIZONTAL)
	self.finallabel = wx.StaticText(self,-1, _("Final score:"))
	finalbox.Add(self.finallabel,1,wx.ALIGN_CENTER_VERTICAL)
	self.finalscore = wx.StaticText(self,-1,u"")
	finalbox.Add(self.finalscore,1)
	results.Add(finalbox,0,wx.EXPAND)
	self.finallabel.Enable(self.dicepool.tabulate)
	self.finallabel.Enable(self.dicepool.tabulate)

	successbox = wx.BoxSizer(wx.VERTICAL)
	successlabelbox = wx.BoxSizer(wx.HORIZONTAL)
	self.successtag = wx.StaticText(self,-1, _("Successes:"))
	successlabelbox.Add(self.successtag,1,wx.ALIGN_LEFT)
	self.successlabel = wx.StaticText(self,-1, "0/" + str(self.dicepool.pool))
	successlabelbox.Add(self.successlabel,0,wx.ALIGN_RIGHT)
	successbox.Add(successlabelbox,0,wx.EXPAND)
	self.successgauge = wx.Gauge(self,-1,self.dicepool.pool)
	successbox.Add(self.successgauge,0,wx.EXPAND)
	self.successtag.Enable(self.dicepool.tabulate)
	self.successlabel.Enable(self.dicepool.tabulate)
	self.successgauge.Enable(self.dicepool.tabulate)
	results.Add(successbox,0,wx.EXPAND)

	failurebox = wx.BoxSizer(wx.VERTICAL)
	failurelabelbox = wx.BoxSizer(wx.HORIZONTAL)
	self.failuretag = wx.StaticText(self,-1, _("Failures:"))
	failurelabelbox.Add(self.failuretag,1,wx.ALIGN_LEFT)
	self.failurelabel = wx.StaticText(self,-1,"0/" + str(self.dicepool.pool))
	failurelabelbox.Add(self.failurelabel,0,wx.ALIGN_RIGHT)
	failurebox.Add(failurelabelbox,0,wx.EXPAND)
	self.failuregauge = wx.Gauge(self,-1,self.dicepool.pool)
	failurebox.Add(self.failuregauge,0,wx.EXPAND)
	self.failuretag.Enable(self.dicepool.tabulate)
	self.failurelabel.Enable(self.dicepool.tabulate)
	self.successgauge.Enable(self.dicepool.tabulate)
	results.Add(failurebox,0,wx.EXPAND)

	botchbox = wx.BoxSizer(wx.VERTICAL)
	botchlabelbox = wx.BoxSizer(wx.HORIZONTAL)
	self.botchtag = wx.StaticText(self,-1, _("Botches:"))
	botchlabelbox.Add(self.botchtag,1,wx.ALIGN_LEFT)
	self.botchlabel = wx.StaticText(self,-1,"0/" + str(self.dicepool.pool))
	botchlabelbox.Add(self.botchlabel,0,wx.ALIGN_RIGHT)
	botchbox.Add(botchlabelbox,0,wx.EXPAND)
	self.botchgauge = wx.Gauge(self,-1,self.dicepool.pool)
	botchbox.Add(self.botchgauge,0,wx.EXPAND)
	self.botchtag.Enable(self.dicepool.tabulate and self.dicepool.botch)
	self.botchlabel.Enable(self.dicepool.tabulate and self.dicepool.botch)
	self.botchgauge.Enable(self.dicepool.tabulate and self.dicepool.botch)
	results.Add(botchbox,0,wx.EXPAND)

	close = wx.Button(self,DIEROLLER_CLOSE,u"Close")
	results.Add(close,0,wx.EXPAND)

	root.Add(results,1,wx.EXPAND)

	self.SetSizerAndFit(root)
	self.Centre(wx.BOTH)

	wx.EVT_BUTTON(self,DIEROLLER_CLOSE,self.onclose)
	wx.EVT_BUTTON(self,DIEROLLER_ROLL,self.onroll)
	wx.EVT_SPINCTRL(self,DIEROLLER_POOL,self.onpool)
	wx.EVT_SPINCTRL(self,DIEROLLER_FACES,self.onfaces)
	wx.EVT_CHOICE(self,DIEROLLER_RNG,self.onrng)
	wx.EVT_SPINCTRL(self,DIEROLLER_DIFF,self.ondiff)
	wx.EVT_CHECKBOX(self,DIEROLLER_BOTCH,self.onbotch)
	wx.EVT_CHECKBOX(self,DIEROLLER_TAB,self.ontab)

    def onclose(self,event):
        self.Destroy()

    def onroll(self,event):
        self.resultbox.Clear()
	self.dicepool.roll()
	for i in range(self.dicepool.pool):
	    self.resultbox.AppendText(str(self.dicepool.dice[i]))
	    self.resultbox.AppendText('\n')
	if self.dicepool.tabulate:
	    self.successlabel.SetLabel(str(self.dicepool.successes) + "/" + str(self.dicepool.pool))
	    self.successgauge.SetValue(self.dicepool.successes)
	    self.failurelabel.SetLabel(str(self.dicepool.failures) + "/" + str(self.dicepool.pool))
	    self.failuregauge.SetValue(self.dicepool.failures)
	    self.botchlabel.SetLabel(str(self.dicepool.botches) + "/" + str(self.dicepool.pool))
	    self.botchgauge.SetValue(self.dicepool.botches)
	    scr = self.dicepool.final
	    score = str(scr) + " : "
	    if scr > 0:
	    	score += _("Success!")
	    elif scr < 0:
	        score += _("Botch!")
	    else:
	        score += _("Failure!")
	    self.finalscore.SetLabel(score)
	self.Layout()
	    

    def onpool(self,event):
        self.dicepool.pool = self.poolctl.GetValue()
	self.freshen()
	self.Layout()

    def onfaces(self,event):
        self.dicepool.faces = self.facectl.GetValue()
	self.diffctl.SetRange(1,self.dicepool.faces)

    def onrng(self,event):
        self.dicepool.setrng(self.rngctl.GetStringSelection())

    def ondiff(self,event):
        self.dicepool.difficulty = self.diffctl.GetValue()

    def onbotch(self,event):
        self.dicepool.botch = self.botchctl.GetValue()
	self.freshen()

    def ontab(self,event):
        self.dicepool.tabulate = self.tabctl.GetValue()
	self.freshen()

    def freshen(self):
	self.difflabel.Enable(self.dicepool.tabulate)
	self.diffctl.Enable(self.dicepool.tabulate)
	self.successtag.Enable(self.dicepool.tabulate)
	self.successlabel.Enable(self.dicepool.tabulate)
	self.successgauge.Enable(self.dicepool.tabulate)
	self.failuretag.Enable(self.dicepool.tabulate)
	self.failurelabel.Enable(self.dicepool.tabulate)
	self.failuregauge.Enable(self.dicepool.tabulate)
	self.botchtag.Enable(self.dicepool.tabulate and self.dicepool.botch)
	self.botchlabel.Enable(self.dicepool.tabulate and self.dicepool.botch)
	self.botchgauge.Enable(self.dicepool.tabulate and self.dicepool.botch)
	self.successlabel.SetLabel("0/" + str(self.dicepool.pool))
	self.successgauge.SetRange(self.dicepool.pool)
	self.successgauge.SetValue(0)
	self.failurelabel.SetLabel("0/" + str(self.dicepool.pool))
	self.failuregauge.SetRange(self.dicepool.pool)
	self.failuregauge.SetValue(0)
	self.botchlabel.SetLabel("0/" + str(self.dicepool.pool))
	self.botchgauge.SetRange(self.dicepool.pool)
	self.botchgauge.SetValue(0)
	self.finallabel.Enable(self.dicepool.tabulate)
	self.finalscore.Enable(self.dicepool.tabulate)
	self.finalscore.SetLabel(u"")
