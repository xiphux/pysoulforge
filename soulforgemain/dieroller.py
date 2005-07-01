from wxPython.wx import *

DIEROLLER_CLOSE = 104
DIEROLLER_ROLL = 105
DIEROLLER_POOL = 106
DIEROLLER_FACES = 107

class dieroller(wxFrame):
    def __init__(self,parent,ID,title):
        wxFrame.__init__(self,parent,ID,title,wxDefaultPosition,wxDefaultSize)

	root = wxBoxSizer(wxHORIZONTAL)

	controls = wxBoxSizer(wxVERTICAL)

	self.poolctl = wxSpinCtrl(self,DIEROLLER_POOL,u"Dice pool: ",wxDefaultPosition,wxDefaultSize,0,1,99,1)
	controls.Add(self.poolctl,1,wxEXPAND)

	self.facectl = wxSpinCtrl(self,DIEROLLER_FACES,u"Die faces: ",wxDefaultPosition,wxDefaultSize,0,2,99,10)
	controls.Add(self.facectl,1,wxEXPAND)

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

    def onclose(self,event):
        self.Destroy()

    def onroll(self,event):
        pass
