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

from wxPython.wx import wxFrame,wxDefaultPosition,wxDefaultSize,wxMenu,wxMenuItem,wxMenuBar,wxFlexGridSizer,wxALIGN_CENTER_VERTICAL,wxTE_READONLY,EVT_MENU,EVT_MENU_RANGE,EVT_BUTTON,wxEXPAND,wxMessageDialog,wxFileDialog,wxStaticText,wxTextCtrl,wxPanel,wxButton,wxBOTH,wxID_OK,wxID_CANCEL,wxOPEN,wxOK,wxCANCEL,wxFILE_MUST_EXIST,wxSAVE,wxOVERWRITE_PROMPT,wxSingleChoiceDialog,wxConfig,wxFileHistory,wxID_FILE1,wxID_FILE2,wxID_FILE3,wxID_FILE4,wxID_FILE5,wxID_FILE6,wxID_FILE7,wxID_FILE8,wxID_FILE9
import dieroller,sfcontrols,sfsheet,sfuniverses,sfconfig
from xml.dom import minidom
from libsoulforge import xmlutils,headerdata
from os import path

SFROOTFRAME_ABOUT = 101
SFROOTFRAME_QUIT = 102
SFROOTFRAME_DIEROLLER = 103
SFROOTFRAME_LOAD = 104
SFROOTFRAME_SAVE = 105
SFROOTFRAME_NEW = 106
SFROOTFRAME_EDIT = 107
SFROOTFRAME_CLOSE = 108
SFROOTFRAME_OPTIONS = 109
SFSHEET_OK = 401

class sfrootframe(wxFrame):
    def __init__(self, parent, ID, title):
        wxFrame.__init__(self, parent, ID, title, wxDefaultPosition, wxDefaultSize)

	self.dom = None
	self.file = None
	self.sh = None
	self.modified = False
	self.config = wxConfig.Get()
	self.history = wxFileHistory()
	self.config.SetPath("/lastrun")
	self.history.Load(self.config)
	self.config.SetPath("/")
	
	filemenu = wxMenu()
	filemenu.Append(SFROOTFRAME_NEW, _("&New"), _("New character"))
	filemenu.Append(SFROOTFRAME_LOAD, _("&Load"), _("Load character"))
	self.save = wxMenuItem(filemenu,SFROOTFRAME_SAVE, _("&Save"), _("Save character"))
	filemenu.AppendItem(self.save)
	self.close = wxMenuItem(filemenu,SFROOTFRAME_CLOSE, _("&Close"), _("Close character"))
	filemenu.AppendItem(self.close)
	filemenu.AppendSeparator()
	self.recent = wxMenu()
	self.history.UseMenu(self.recent)
	self.history.AddFilesToMenu()
	filemenu.AppendMenu(-1, _("&Recent files"), self.recent, _("Recently opened files"))
	filemenu.AppendSeparator()
	filemenu.Append(SFROOTFRAME_QUIT, _("E&xit"), _("Quit Soulforge"))

	toolsmenu = wxMenu()
	toolsmenu.Append(SFROOTFRAME_DIEROLLER, _("&Dieroller"), _("Dieroller"))
	toolsmenu.AppendSeparator()
	toolsmenu.Append(SFROOTFRAME_OPTIONS, _("&Options"), _("Options"))

	helpmenu = wxMenu()
	helpmenu.Append(SFROOTFRAME_ABOUT, _("&About"), _("About Soulforge"))

	menubar = wxMenuBar()
	menubar.Append(filemenu, _("&File"))
	menubar.Append(toolsmenu, _("&Tools"))
	menubar.Append(helpmenu, _("&Help"))
	
	self.SetMenuBar(menubar)

	pan = wxPanel(self,-1,wxDefaultPosition,wxDefaultSize)

	root = wxFlexGridSizer(6,2,0,0)
	root.AddGrowableCol(1,1)
	root.Add(wxStaticText(self,-1, _("Name:")),0,wxALIGN_CENTER_VERTICAL)
	self.name = wxTextCtrl(self,-1,u"",wxDefaultPosition,wxDefaultSize,wxTE_READONLY)
	root.Add(self.name,1,wxEXPAND)
	root.Add(wxStaticText(self,-1, _("Player:")),0,wxALIGN_CENTER_VERTICAL)
	self.player = wxTextCtrl(self,-1,u"",wxDefaultPosition,wxDefaultSize,wxTE_READONLY)
	root.Add(self.player,1,wxEXPAND)
	root.Add(wxStaticText(self,-1, _("Universe:")),0,wxALIGN_CENTER_VERTICAL)
	self.universe = wxTextCtrl(self,-1,u"",wxDefaultPosition,wxDefaultSize,wxTE_READONLY)
	root.Add(self.universe,1,wxEXPAND)
	root.Add(wxStaticText(self,-1, _("Filename:")),0,wxALIGN_CENTER_VERTICAL)
	self.filename = wxTextCtrl(self,-1,u"",wxDefaultPosition,wxDefaultSize,wxTE_READONLY)
	root.Add(self.filename,1,wxEXPAND)
	root.Add(wxPanel(self,-1))
	self.edit = wxButton(self,SFROOTFRAME_EDIT, _("Edit"))
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
	EVT_MENU(self,SFROOTFRAME_OPTIONS,self.onoptions)
	EVT_MENU_RANGE(self,wxID_FILE1,wxID_FILE9,self.onrecent)
	EVT_BUTTON(self,SFSHEET_OK,self.onsheetok)
	EVT_BUTTON(self,SFROOTFRAME_EDIT,self.onedit)

    def onquit(self,event):
        if self.modified:
	    err = wxMessageDialog(self, _("Character is still unsaved.  Quit anyway?"), _("Are you sure?"),wxOK|wxCANCEL)
	    err.Centre(wxBOTH)
	    ret = err.ShowModal()
	    err.Destroy()
	    if ret == wxID_CANCEL:
	        return
        self.config.SetPath("/lastrun")
	self.history.Save(self.config)
	self.config.SetPath("/")
        self.Close(True)

    def onabout(self,event):
        abt = wxMessageDialog(self, _("Soulforge by Christopher Han <xiphux@gmail.com>\nCopyright (C) 2005\nLicensed under the GNU GPL"), _("About Soulforge"),wxOK)
	abt.ShowModal()
	abt.Destroy()

    def ondieroller(self,event):
        dr = dieroller.dieroller(self,-1, _("Dieroller"))
	dr.Show(True)

    def parsefile(self):
	self.dom = xmlutils.loaddata(self.file)
	self.populatefields()
	self.updategui()

    def onload(self,event):
        loaddlg = wxFileDialog(self, _("Load character"),self.config.Read(headerdata.SF_CONFIGKEY_LOADDIR),"", headerdata.SF_FILEMASK,wxOPEN|wxFILE_MUST_EXIST)
	if loaddlg.ShowModal() == wxID_OK:
	    if self.dom:
	        err = wxMessageDialog(self, _("If you load this character sheet, current character data will be cleared.  Are you sure?"), _("Are you sure?"),wxOK|wxCANCEL)
		err.Centre(wxBOTH)
		ret = err.ShowModal()
		err.Destroy()
		if ret == wxID_CANCEL:
		    return
	    self.file = loaddlg.GetPath()
	    self.history.AddFileToHistory(self.file)
	    self.config.Write(headerdata.SF_CONFIGKEY_LOADDIR, path.dirname(self.file))
	    self.config.Flush(True)
	    self.parsefile()
	loaddlg.Destroy()
    
    def onrecent(self,event):
        recentfile = self.history.GetHistoryFile(event.GetId() - wxID_FILE1)
	if recentfile:
	    if not path.exists(recentfile):
	        err = wxMessageDialog(self, _("Error: Selected file no longer exists"), _("Error!"),wxOK)
		err.Centre(wxBOTH)
		err.ShowModal()
		err.Destroy()
		return
	    self.file = recentfile
	    self.history.AddFileToHistory(recentfile)
	    self.parsefile()

    def onsave(self,event):
        if not self.dom:
	    err = wxMessageDialog(self, _("Error: No character data to save"), _("Error!"),wxOK)
	    err.Centre(wxBOTH)
	    err.ShowModal()
	    err.Destroy()
	    return
        if not self.file:
	    savedlg = wxFileDialog(self, _("Save character"),self.config.Read(headerdata.SF_CONFIGKEY_SAVEDIR),"", headerdata.SF_FILEMASK,wxSAVE|wxOVERWRITE_PROMPT)
	    if savedlg.ShowModal() == wxID_OK:
	        self.file = savedlg.GetPath()
		self.config.Write(headerdata.SF_CONFIGKEY_SAVEDIR, path.dirname(self.file))
		self.config.Flush(True)
	    savedlg.Destroy()
	if self.file:
	    xmlutils.savedata(self.dom, self.file, self.config.ReadInt(headerdata.SF_CONFIGKEY_COMPRESS,headerdata.SF_CONFIGDEFAULT_COMPRESS))
	    self.modified = False
	    self.history.AddFileToHistory(self.file)
	self.populatefields()
	self.updategui()

    def onnew(self,event):
        if self.dom:
	    err = wxMessageDialog(self, _("If you start a new sheet, previous character data will be cleared.  Are you sure?"), _("Are you sure?"),wxOK|wxCANCEL)
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
        un = []
	for i in sfuniverses.universes:
	    un.append(_(i))
	uni = wxSingleChoiceDialog(self, _("Choose a universe:"), _("Universe"),un)
	ret = uni.ShowModal()
	if ret == wxID_OK:
	    ch = uni.GetStringSelection()
	    if ch:
                self.sh = sfsheet.sfsheet(self,-1,ch)
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

    def onoptions(self,event):
        conf = sfconfig.sfconfig(self,-1)
	conf.ShowModal()

    def populatefields(self):
        if self.sh:
	    self.name.SetValue(self.sh.sheet.name.GetValue())
	    self.player.SetValue(self.sh.sheet.player.GetValue())
	    self.universe.SetValue(self.sh.universe)
	elif self.dom:
	    self.name.SetValue(xmlutils.getnodetext(self.dom.getElementsByTagName("name")[0]))
	    self.player.SetValue(xmlutils.getnodetext(self.dom.getElementsByTagName("player")[0]))
	    self.universe.SetValue(self.dom.documentElement.getAttribute("universe"))
	else:
	    self.name.SetValue(u"")
	    self.player.SetValue(u"")
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
	    err = wxMessageDialog(self, _("Character is still unsaved.  Close anyway?"), _("Are you sure?"),wxOK|wxCANCEL)
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
