from wxPython.wx import *
import dieroller

SFROOTFRAME_ABOUT = 101
SFROOTFRAME_QUIT = 102
SFROOTFRAME_DIEROLLER = 103

class sfrootframe(wxFrame):
    def __init__(self, parent, ID, title):
        wxFrame.__init__(self, parent, ID, title, wxDefaultPosition, wxSize(200,150))

	filemenu = wxMenu()
	filemenu.Append(SFROOTFRAME_QUIT, u"E&xit", u"Quit Soulforge")

	toolsmenu = wxMenu()
	toolsmenu.Append(SFROOTFRAME_DIEROLLER, u"&Dieroller", u"Dieroller")

	helpmenu = wxMenu()
	helpmenu.Append(SFROOTFRAME_ABOUT, u"&About", u"About Soulforge")

	menubar = wxMenuBar()
	menubar.Append(filemenu, u"&File")
	menubar.Append(toolsmenu, u"&Tools")
	menubar.Append(helpmenu, u"&Help")
	
	self.SetMenuBar(menubar)

	EVT_MENU(self,SFROOTFRAME_QUIT,self.onquit)
	EVT_MENU(self,SFROOTFRAME_ABOUT,self.onabout)
	EVT_MENU(self,SFROOTFRAME_DIEROLLER,self.ondieroller)

    def onquit(self,event):
        self.Close(true)

    def onabout(self,event):
        abt = wxMessageDialog(self,u"Soulforge by Christopher Han\nCopyright (C) 2005\nLicensed under the GNU GPL",u"About Soulforge",wxOK)
	abt.ShowModal()
	abt.Destroy()

    def ondieroller(self,event):
        dr = dieroller.dieroller(self,-1,u"Dieroller")
	dr.Show(true)
