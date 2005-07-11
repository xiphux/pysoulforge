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

from wxPython.wx import wxFrame,wxBoxSizer,wxStaticText,wxSpinCtrl,wxTextCtrl,wxGauge,wxDefaultPosition,wxDefaultSize,wxHORIZONTAL,wxVERTICAL,wxALIGN_CENTER_VERTICAL,wxEXPAND,wxChoice,wxCheckBox,wxButton,wxTE_MULTILINE,wxTE_READONLY,wxALIGN_LEFT,wxALIGN_RIGHT,wxBOTH,EVT_BUTTON,EVT_SPINCTRL,EVT_CHOICE,EVT_CHECKBOX
from libsoulforge import dicepool, headerdata

DIEROLLER_CLOSE = 104
DIEROLLER_ROLL = 105
DIEROLLER_POOL = 106
DIEROLLER_FACES = 107
DIEROLLER_RNG = 108
DIEROLLER_BOTCH = 109
DIEROLLER_TAB = 110
DIEROLLER_DIFF = 111

class dieroller(wxFrame):
    def __init__(self,parent,ID,title):
        wxFrame.__init__(self,parent,ID,title,wxDefaultPosition,wxDefaultSize)

	self.dicepool = dicepool.dicepool()

	root = wxBoxSizer(wxHORIZONTAL)

	controls = wxBoxSizer(wxVERTICAL)

	poolbox = wxBoxSizer(wxHORIZONTAL)
	poolbox.Add(wxStaticText(self,-1,_("Dice pool:")),0,wxALIGN_CENTER_VERTICAL)
	self.poolctl = wxSpinCtrl(self,DIEROLLER_POOL,u"",wxDefaultPosition,wxDefaultSize,0,1,99,self.dicepool.pool)
	poolbox.Add(self.poolctl,1,wxALIGN_CENTER_VERTICAL)
	controls.Add(poolbox,1,wxEXPAND)

	facebox = wxBoxSizer(wxHORIZONTAL)
	facebox.Add(wxStaticText(self,-1,_("Die faces:")),0,wxALIGN_CENTER_VERTICAL)
	self.facectl = wxSpinCtrl(self,DIEROLLER_FACES,u"",wxDefaultPosition,wxDefaultSize,0,2,99,self.dicepool.faces)
	facebox.Add(self.facectl,1,wxALIGN_CENTER_VERTICAL)
	controls.Add(facebox,1,wxEXPAND)

	rngbox = wxBoxSizer(wxVERTICAL)
	rngbox.Add(wxStaticText(self,-1,_("Pseudo-random number generator:")),0)
	rngstrings = [ _("Mersenne Twister"), _("Wichmann-Hill"), _("urandom()") ]
	self.rngctl = wxChoice(self,DIEROLLER_RNG,wxDefaultPosition,wxDefaultSize,rngstrings)
	rngbox.Add(self.rngctl,1,wxEXPAND)
	controls.Add(rngbox,0,wxEXPAND)
	
	self.botchctl = wxCheckBox(self,DIEROLLER_BOTCH, _("Botches"))
	self.botchctl.SetValue(self.dicepool.botch)
	controls.Add(self.botchctl,0,wxEXPAND)

	self.tabctl = wxCheckBox(self,DIEROLLER_TAB, _("Tabulate"))
	self.tabctl.SetValue(self.dicepool.tabulate)
	controls.Add(self.tabctl,0,wxEXPAND)

	diffbox = wxBoxSizer(wxHORIZONTAL)
	self.difflabel = wxStaticText(self,-1, _("Difficulty:"))
	diffbox.Add(self.difflabel,0,wxALIGN_CENTER_VERTICAL)
	self.diffctl = wxSpinCtrl(self,DIEROLLER_DIFF,u"",wxDefaultPosition,wxDefaultSize,0,1,self.dicepool.faces,6)
	diffbox.Add(self.diffctl,1,wxALIGN_CENTER_VERTICAL)
	controls.Add(diffbox,1,wxEXPAND)
	self.difflabel.Enable(self.dicepool.tabulate)
	self.diffctl.Enable(self.dicepool.tabulate)

	roll = wxButton(self,DIEROLLER_ROLL, _("Roll"))
	controls.Add(roll,0,wxEXPAND)

	root.Add(controls,1,wxEXPAND)

	results = wxBoxSizer(wxVERTICAL)

	self.resultbox = wxTextCtrl(self,-1,u"",wxDefaultPosition,wxDefaultSize,wxTE_MULTILINE|wxTE_READONLY)
	results.Add(self.resultbox,2,wxEXPAND)

	finalbox = wxBoxSizer(wxHORIZONTAL)
	self.finallabel = wxStaticText(self,-1, _("Final score:"))
	finalbox.Add(self.finallabel,1,wxALIGN_CENTER_VERTICAL)
	self.finalscore = wxStaticText(self,-1,u"")
	finalbox.Add(self.finalscore,1)
	results.Add(finalbox,0,wxEXPAND)
	self.finallabel.Enable(self.dicepool.tabulate)
	self.finallabel.Enable(self.dicepool.tabulate)

	successbox = wxBoxSizer(wxVERTICAL)
	successlabelbox = wxBoxSizer(wxHORIZONTAL)
	self.successtag = wxStaticText(self,-1, _("Successes:"))
	successlabelbox.Add(self.successtag,1,wxALIGN_LEFT)
	self.successlabel = wxStaticText(self,-1, "0/" + str(self.dicepool.pool))
	successlabelbox.Add(self.successlabel,0,wxALIGN_RIGHT)
	successbox.Add(successlabelbox,0,wxEXPAND)
	self.successgauge = wxGauge(self,-1,self.dicepool.pool)
	successbox.Add(self.successgauge,0,wxEXPAND)
	self.successtag.Enable(self.dicepool.tabulate)
	self.successlabel.Enable(self.dicepool.tabulate)
	self.successgauge.Enable(self.dicepool.tabulate)
	results.Add(successbox,0,wxEXPAND)

	failurebox = wxBoxSizer(wxVERTICAL)
	failurelabelbox = wxBoxSizer(wxHORIZONTAL)
	self.failuretag = wxStaticText(self,-1, _("Failures:"))
	failurelabelbox.Add(self.failuretag,1,wxALIGN_LEFT)
	self.failurelabel = wxStaticText(self,-1,"0/" + str(self.dicepool.pool))
	failurelabelbox.Add(self.failurelabel,0,wxALIGN_RIGHT)
	failurebox.Add(failurelabelbox,0,wxEXPAND)
	self.failuregauge = wxGauge(self,-1,self.dicepool.pool)
	failurebox.Add(self.failuregauge,0,wxEXPAND)
	self.failuretag.Enable(self.dicepool.tabulate)
	self.failurelabel.Enable(self.dicepool.tabulate)
	self.successgauge.Enable(self.dicepool.tabulate)
	results.Add(failurebox,0,wxEXPAND)

	botchbox = wxBoxSizer(wxVERTICAL)
	botchlabelbox = wxBoxSizer(wxHORIZONTAL)
	self.botchtag = wxStaticText(self,-1, _("Botches:"))
	botchlabelbox.Add(self.botchtag,1,wxALIGN_LEFT)
	self.botchlabel = wxStaticText(self,-1,"0/" + str(self.dicepool.pool))
	botchlabelbox.Add(self.botchlabel,0,wxALIGN_RIGHT)
	botchbox.Add(botchlabelbox,0,wxEXPAND)
	self.botchgauge = wxGauge(self,-1,self.dicepool.pool)
	botchbox.Add(self.botchgauge,0,wxEXPAND)
	self.botchtag.Enable(self.dicepool.tabulate and self.dicepool.botch)
	self.botchlabel.Enable(self.dicepool.tabulate and self.dicepool.botch)
	self.botchgauge.Enable(self.dicepool.tabulate and self.dicepool.botch)
	results.Add(botchbox,0,wxEXPAND)

	close = wxButton(self,DIEROLLER_CLOSE,u"Close")
	results.Add(close,0,wxEXPAND)

	root.Add(results,1,wxEXPAND)

	self.SetSizerAndFit(root)
	self.Centre(wxBOTH)

	EVT_BUTTON(self,DIEROLLER_CLOSE,self.onclose)
	EVT_BUTTON(self,DIEROLLER_ROLL,self.onroll)
	EVT_SPINCTRL(self,DIEROLLER_POOL,self.onpool)
	EVT_SPINCTRL(self,DIEROLLER_FACES,self.onfaces)
	EVT_CHOICE(self,DIEROLLER_RNG,self.onrng)
	EVT_SPINCTRL(self,DIEROLLER_DIFF,self.ondiff)
	EVT_CHECKBOX(self,DIEROLLER_BOTCH,self.onbotch)
	EVT_CHECKBOX(self,DIEROLLER_TAB,self.ontab)

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
