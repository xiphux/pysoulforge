from wxPython.wx import *
from libsoulforge import dicepool

DIEROLLER_CLOSE = 104
DIEROLLER_ROLL = 105
DIEROLLER_POOL = 106
DIEROLLER_FACES = 107
DIEROLLER_RNG = 108

class dieroller(wxFrame):
    def __init__(self,parent,ID,title):
        wxFrame.__init__(self,parent,ID,title,wxDefaultPosition,wxDefaultSize)

	self.dicepool = dicepool.dicepool()

	root = wxBoxSizer(wxHORIZONTAL)

	controls = wxBoxSizer(wxVERTICAL)

	poolbox = wxBoxSizer(wxHORIZONTAL)
	poolbox.Add(wxStaticText(self,-1,u"Dice pool:"),0)
	self.poolctl = wxSpinCtrl(self,DIEROLLER_POOL,u"",wxDefaultPosition,wxDefaultSize,0,1,99,self.dicepool.pool)
	poolbox.Add(self.poolctl,1)
	controls.Add(poolbox,1,wxEXPAND)

	facebox = wxBoxSizer(wxHORIZONTAL)
	facebox.Add(wxStaticText(self,-1,u"Die faces:"),0)
	self.facectl = wxSpinCtrl(self,DIEROLLER_FACES,u"",wxDefaultPosition,wxDefaultSize,0,2,99,self.dicepool.faces)
	facebox.Add(self.facectl,1)
	controls.Add(facebox,1,wxEXPAND)

	rngbox = wxBoxSizer(wxVERTICAL)
	rngbox.Add(wxStaticText(self,-1,u"Pseudo-random number generator:"),0)
	rngstrings = [ u"Mersenne Twister", u"Wichmann-Hill", u"urandom()" ]
	self.rngcontrol = wxChoice(self,DIEROLLER_RNG,wxDefaultPosition,wxDefaultSize,rngstrings)
	rngbox.Add(self.rngcontrol,1,wxEXPAND)
	controls.Add(rngbox,0,wxEXPAND)

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

    def onclose(self,event):
        self.Destroy()

    def onroll(self,event):
        pass

    def onpool(self,event):
        pass

    def onfaces(self,event):
        pass

    def onrng(self,event):
        pass
