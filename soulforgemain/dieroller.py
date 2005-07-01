from wxPython.wx import *
from libsoulforge import dicepool

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
	poolbox.Add(wxStaticText(self,-1,u"Dice pool:"),0,wxALIGN_CENTER_VERTICAL)
	self.poolctl = wxSpinCtrl(self,DIEROLLER_POOL,u"",wxDefaultPosition,wxDefaultSize,0,1,99,self.dicepool.pool)
	poolbox.Add(self.poolctl,1)
	controls.Add(poolbox,1,wxEXPAND)

	facebox = wxBoxSizer(wxHORIZONTAL)
	facebox.Add(wxStaticText(self,-1,u"Die faces:"),0,wxALIGN_CENTER_VERTICAL)
	self.facectl = wxSpinCtrl(self,DIEROLLER_FACES,u"",wxDefaultPosition,wxDefaultSize,0,2,99,self.dicepool.faces)
	facebox.Add(self.facectl,1)
	controls.Add(facebox,1,wxEXPAND)

	rngbox = wxBoxSizer(wxVERTICAL)
	rngbox.Add(wxStaticText(self,-1,u"Pseudo-random number generator:"),0)
	rngstrings = [ u"Mersenne Twister", u"Wichmann-Hill", u"urandom()" ]
	self.rngctl = wxChoice(self,DIEROLLER_RNG,wxDefaultPosition,wxDefaultSize,rngstrings)
	rngbox.Add(self.rngctl,1,wxEXPAND)
	controls.Add(rngbox,0,wxEXPAND)
	
	self.botchctl = wxCheckBox(self,DIEROLLER_BOTCH,u"Botches")
	self.botchctl.SetValue(self.dicepool.botch)
	controls.Add(self.botchctl,0,wxEXPAND)

	self.tabctl = wxCheckBox(self,DIEROLLER_TAB,u"Tabulate")
	self.tabctl.SetValue(self.dicepool.tabulate)
	controls.Add(self.tabctl,0,wxEXPAND)

	diffbox = wxBoxSizer(wxHORIZONTAL)
	self.difflabel = wxStaticText(self,-1,u"Difficulty:")
	diffbox.Add(self.difflabel,0,wxALIGN_CENTER_VERTICAL)
	self.diffctl = wxSpinCtrl(self,DIEROLLER_DIFF,u"",wxDefaultPosition,wxDefaultSize,0,1,self.dicepool.faces,6)
	diffbox.Add(self.diffctl,1)
	controls.Add(diffbox,1,wxEXPAND)
	self.difflabel.Enable(self.dicepool.tabulate)
	self.diffctl.Enable(self.dicepool.tabulate)

	roll = wxButton(self,DIEROLLER_ROLL,u"Roll")
	controls.Add(roll,0,wxEXPAND)

	root.Add(controls,1,wxEXPAND)

	results = wxBoxSizer(wxVERTICAL)

	self.resultbox = wxTextCtrl(self,-1,u"",wxDefaultPosition,wxSize(100,60),wxTE_MULTILINE|wxTE_READONLY)
	results.Add(self.resultbox,1,wxEXPAND)

	close = wxButton(self,DIEROLLER_CLOSE,u"Close")
	results.Add(close,0,wxEXPAND)

	root.Add(results,1,wxEXPAND)

	self.SetSizerAndFit(root)

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

    def onpool(self,event):
        self.dicepool.pool = self.poolctl.GetValue()

    def onfaces(self,event):
        self.dicepool.faces = self.facectl.GetValue()

    def onrng(self,event):
        self.dicepool.setrng(self.rngctl.GetStringSelection())

    def ondiff(self,event):
        self.dicepool.difficulty = self.diffctl.GetValue()

    def onbotch(self,event):
        self.dicepool.botch = self.botchctl.GetValue()

    def ontab(self,event):
        self.dicepool.tabulate = self.tabctl.GetValue()
	self.difflabel.Enable(self.dicepool.tabulate)
	self.diffctl.Enable(self.dicepool.tabulate)
