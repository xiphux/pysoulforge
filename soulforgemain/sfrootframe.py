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
import dieroller,sfcontrols,sfsheet,sfuniverses,sfuniversechooser
from xml.dom import minidom
from libsoulforge import xmlutils

SFROOTFRAME_ABOUT = 101
SFROOTFRAME_QUIT = 102
SFROOTFRAME_DIEROLLER = 103
SFROOTFRAME_LOAD = 104
SFROOTFRAME_SAVE = 105
SFROOTFRAME_NEW = 106
SFROOTFRAME_EDIT = 107
SFROOTFRAME_CLOSE = 108
SFSHEET_OK = 401

class sfrootframe(wxFrame):
    def __init__(self, parent, ID, title):
        wxFrame.__init__(self, parent, ID, title, wxDefaultPosition, wxDefaultSize)

	self.dom = None
	self.file = None
	self.sh = None
	self.modified = False
	
	filemenu = wxMenu()
	filemenu.Append(SFROOTFRAME_NEW, u"&New", u"New character")
	filemenu.Append(SFROOTFRAME_LOAD, u"&Load", u"Load character")
	self.save = wxMenuItem(filemenu,SFROOTFRAME_SAVE,u"&Save",u"Save character")
	filemenu.AppendItem(self.save)
	self.close = wxMenuItem(filemenu,SFROOTFRAME_CLOSE,u"&Close",u"Close character")
	filemenu.AppendItem(self.close)
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

	root = wxFlexGridSizer(6,2,0,0)
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
	root.Add(wxPanel(self,-1))
	self.edit = wxButton(self,SFROOTFRAME_EDIT,u"Edit")
	root.Add(self.edit,1,wxEXPAND)

	self.SetSizer(root)
	self.Centre(wxBOTH)

	self.updategui()

	EVT_MENU(self,SFROOTFRAME_QUIT,self.onquit)
	EVT_MENU(self,SFROOTFRAME_ABOUT,self.onabout)
	EVT_MENU(self,SFROOTFRAME_DIEROLLER,self.ondieroller)
	EVT_MENU(self,SFROOTFRAME_LOAD,self.onload)
	EVT_MENU(self,SFROOTFRAME_SAVE,self.onsave)
	EVT_MENU(self,SFROOTFRAME_CLOSE,self.onclose)
	EVT_MENU(self,SFROOTFRAME_NEW,self.onnew)
	EVT_BUTTON(self,SFSHEET_OK,self.onsheetok)
	EVT_BUTTON(self,SFROOTFRAME_EDIT,self.onedit)

    def onquit(self,event):
        if self.modified:
	    err = wxMessageDialog(self,u"Character is still unsaved.  Quit anyway?",u"Are you sure?",wxOK|wxCANCEL)
	    err.Centre(wxBOTH)
	    ret = err.ShowModal()
	    err.Destroy()
	    if ret == wxID_CANCEL:
	        return
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
	    if self.dom:
	        err = wxMessageDialog(self,u"If you load this character sheet, current character data will be cleared.  Are you sure?",u"Are you sure?",wxOK|wxCANCEL)
		err.Centre(wxBOTH)
		ret = err.ShowModal()
		err.Destroy()
		if ret == wxID_CANCEL:
		    return
	    self.file = loaddlg.GetPath()
	    self.dom = xmlutils.loaddata(self.file)
	    self.populatefields()
	    self.updategui()
	loaddlg.Destroy()

    def onsave(self,event):
        if not self.dom:
	    err = wxMessageDialog(self,u"Error: No character data to save",u"Error!",wxOK)
	    err.Centre(wxBOTH)
	    err.ShowModal()
	    err.Destroy()
	    return
        if not self.file:
	    savedlg = wxFileDialog(self,u"Save character","","",u"Soulforge Data (*.sfd)|*.sfd|XML (*.xml)|*.xml|All files (*.*)|*.*",wxSAVE|wxOVERWRITE_PROMPT)
	    if savedlg.ShowModal() == wxID_OK:
	        self.file = savedlg.GetPath()
	    savedlg.Destroy()
	if self.file:
	    xmlutils.savedata(self.dom, self.file)
	    self.modified = False
	self.populatefields()
	self.updategui()

    def onnew(self,event):
        if self.dom:
	    err = wxMessageDialog(self,u"If you start a new sheet, previous character data will be cleared.  Are you sure?","Are you sure?",wxOK|wxCANCEL)
	    err.Centre(wxBOTH)
	    ret = err.ShowModal()
	    err.Destroy()
	    if ret == wxID_OK:
	        self.dom.unlink()
		self.dom = None
		self.file = None
		self.populatefields()
		self.updategui()
	    else:
	        return
	uni = sfuniversechooser.sfuniversechooser(self,-1)
	ret = uni.ShowModal()
	if ret == wxID_OK:
            self.sh = sfsheet.sfsheet(self,-1,uni.universe)
	    self.sh.Show()
	uni.Destroy()

    def onsheetok(self,event):
        if self.dom:
	    self.dom.unlink()
	self.dom = minidom.getDOMImplementation().createDocument(None,"soulforge_character",None)
	sfuniverses.universe_sheet2xml[self.sh.universe](self.sh.sheet,self.dom)
	self.sh.Destroy()
	self.populatefields()
	self.modified = True
	self.updategui()

    def onedit(self,event):
        uni = self.dom.documentElement.getAttribute("universe")
        self.sh = sfsheet.sfsheet(self,-1,uni)
	sfuniverses.universe_xml2sheet[uni](self.dom,self.sh.sheet)
	self.sh.Show()

    def populatefields(self):
        if self.sh:
	    self.name.SetValue(self.sh.sheet.name.GetValue())
	    self.player.SetValue(self.sh.sheet.player.GetValue())
	    self.universe.SetValue(self.sh.universe)
	    self.clan.SetValue(self.sh.sheet.clan.GetValue())
	elif self.dom:
	    self.name.SetValue(xmlutils.getnodetext(self.dom.getElementsByTagName("name")[0]))
	    self.player.SetValue(xmlutils.getnodetext(self.dom.getElementsByTagName("player")[0]))
	    self.clan.SetValue(xmlutils.getnodetext(self.dom.getElementsByTagName("clan")[0]))
	    self.universe.SetValue(self.dom.documentElement.getAttribute("universe"))
	else:
	    self.name.SetValue(u"")
	    self.player.SetValue(u"")
	    self.clan.SetValue(u"")
	    self.universe.SetValue(u"")
	if self.file:
	    self.filename.SetValue(self.file)
	else:
	    self.filename.SetValue(u"")

    def updategui(self):
        self.save.Enable(self.modified)
	if self.dom:
	    self.edit.Enable(True)
	else:
	    self.edit.Enable(False)
	if self.file or self.modified:
	    self.close.Enable(True)
	else:
	    self.close.Enable(False)

    def onclose(self,event):
        if self.modified:
	    err = wxMessageDialog(self,u"Character is still unsaved.  Close anyway?",u"Are you sure?",wxOK|wxCANCEL)
	    err.Centre(wxBOTH)
	    ret = err.ShowModal()
	    err.Destroy()
	    if ret == wxID_CANCEL:
	        return
	self.file = None
	if self.dom:
	    self.dom.unlink()
	    self.dom = None
	if self.sh:
	    self.sh.Destroy()
	    self.sh = None
	self.modified = False
	self.populatefields()
	self.updategui()
