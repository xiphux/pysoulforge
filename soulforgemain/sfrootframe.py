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

from wxPython.wx import *
import dieroller,sfcontrols,sfsheet
from sheets import vampire_the_masquerade_data
from xml.dom import minidom

SFROOTFRAME_ABOUT = 101
SFROOTFRAME_QUIT = 102
SFROOTFRAME_DIEROLLER = 103
SFROOTFRAME_LOAD = 104
SFROOTFRAME_SAVE = 105
SFROOTFRAME_NEW = 106
SFSHEET_OK = 401

class sfrootframe(wxFrame):
    def __init__(self, parent, ID, title):
        wxFrame.__init__(self, parent, ID, title, wxDefaultPosition, wxDefaultSize)

	self.dom = None
	self.file = None
	self.sh = None
	
	filemenu = wxMenu()
	filemenu.Append(SFROOTFRAME_NEW, u"&New", u"New character")
	filemenu.Append(SFROOTFRAME_LOAD, u"&Load", u"Load character")
	filemenu.Append(SFROOTFRAME_SAVE, u"&Save", u"Save character")
	filemenu.AppendSeparator()
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

	root = wxFlexGridSizer(5,2,0,0)
	root.AddGrowableCol(1,1)
	root.Add(wxStaticText(self,-1,u"Name:"),0,wxALIGN_CENTER_VERTICAL)
	self.name = wxTextCtrl(self,-1,u"",wxDefaultPosition,wxDefaultSize,wxTE_READONLY)
	root.Add(self.name,1,wxEXPAND)
	root.Add(wxStaticText(self,-1,u"Player:"),0,wxALIGN_CENTER_VERTICAL)
	self.player = wxTextCtrl(self,-1,u"",wxDefaultPosition,wxDefaultSize,wxTE_READONLY)
	root.Add(self.player,1,wxEXPAND)
	root.Add(wxStaticText(self,-1,u"Clan:"),0,wxALIGN_CENTER_VERTICAL)
	self.clan = wxTextCtrl(self,-1,u"",wxDefaultPosition,wxDefaultSize,wxTE_READONLY)
	root.Add(self.clan,1,wxEXPAND)
	root.Add(wxStaticText(self,-1,u"Universe:"),0,wxALIGN_CENTER_VERTICAL)
	self.universe = wxTextCtrl(self,-1,u"",wxDefaultPosition,wxDefaultSize,wxTE_READONLY)
	root.Add(self.universe,1,wxEXPAND)
	root.Add(wxStaticText(self,-1,u"Filename:"),0,wxALIGN_CENTER_VERTICAL)
	self.filename = wxTextCtrl(self,-1,u"",wxDefaultPosition,wxDefaultSize,wxTE_READONLY)
	root.Add(self.filename,1,wxEXPAND)

	self.SetSizer(root)
	self.Centre(wxBOTH)

	EVT_MENU(self,SFROOTFRAME_QUIT,self.onquit)
	EVT_MENU(self,SFROOTFRAME_ABOUT,self.onabout)
	EVT_MENU(self,SFROOTFRAME_DIEROLLER,self.ondieroller)
	EVT_MENU(self,SFROOTFRAME_LOAD,self.onload)
	EVT_MENU(self,SFROOTFRAME_SAVE,self.onsave)
	EVT_MENU(self,SFROOTFRAME_NEW,self.onnew)
	EVT_BUTTON(self,SFSHEET_OK,self.onsheetok)

    def onquit(self,event):
        self.Close(true)

    def onabout(self,event):
        abt = wxMessageDialog(self,u"Soulforge by Christopher Han <xiphux@gmail.com>\nCopyright (C) 2005\nLicensed under the GNU GPL",u"About Soulforge",wxOK)
	abt.ShowModal()
	abt.Destroy()

    def ondieroller(self,event):
        dr = dieroller.dieroller(self,-1,u"Dieroller")
	dr.Show(true)

    def onload(self,event):
        loaddlg = wxFileDialog(self,u"Load character","","",u"Soulforge Data (*.sfd)|*.sfd|XML (*.xml)|*.xml|All files (*.*)|*.*",wxOPEN|wxFILE_MUST_EXIST)
	if loaddlg.ShowModal() == wxID_OK:
	    self.file = loaddlg.GetPath()
	    self.dom = minidom.parse(self.file)
	    self.populatefields()

    def onsave(self,event):
        if not self.dom:
	    err = wxMessageDialog(self,u"Error: No character data to save",u"Error!",wxOK)
	    err.Centre(wxBOTH)
	    err.ShowModal()
	    return
        if not self.file:
	    savedlg = wxFileDialog(self,u"Save character","","",u"Soulforge Data (*.sfd)|*.sfd|XML (*.xml)|*.xml|All files (*.*)|*.*",wxSAVE|wxOVERWRITE_PROMPT)
	    if savedlg.ShowModal() == wxID_OK:
	        self.file = savedlg.GetPath()
	if self.file:
	    fd = open(self.file,"w")
	    self.dom.writexml(fd,"    ","    ","\n")
	    fd.close()

    def onnew(self,event):
        self.sh = sfsheet.sfsheet(self,-1,u"Vampire: The Masquerade")
	self.sh.Show()

    def onsheetok(self,event):
        if self.dom:
	    self.dom.unlink()
	self.dom = minidom.getDOMImplementation().createDocument(None,"soulforge_character",None)
	vtmp = vampire_the_masquerade_data.vampire_the_masquerade_parser()
	vtmp.sheet2xml(self.sh.sheet,self.dom)
	self.sh.Destroy()
	self.populatefields()

    def populatefields(self):
        if self.sh:
	    self.name.SetValue(self.sh.sheet.name.GetValue())
	    self.player.SetValue(self.sh.sheet.player.GetValue())
	    self.chronicle.SetValue(self.sh.sheet.chronicle.GetValue())
	    self.universe.SetValue(vampire_the_masquerade_data.universe)
	    self.clan.SetValue(self.sh.sheet.clan.GetValue())
	elif self.dom:
	    self.name.SetValue(self.dom.getElementsByTagName("name")[0])
	    self.player.SetValue(self.dom.getElementsByTagName("player")[0])
	    self.chronicle.SetValue(self.dom.getElementsByTagName("chronicle")[0])
	    self.clan.SetValue(self.dom.getElementsByTagName("clan")[0])
	    self.universe.SetValue(self.dom.getAttribute("universe"))
	if self.file:
	    self.filename.SetValue(self.file)
