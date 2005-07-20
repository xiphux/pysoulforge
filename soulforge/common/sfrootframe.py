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

import sys
import os
import cStringIO
from codecs import getencoder,getdecoder
from xml import dom
from xml.parsers.xmlproc import xmlval, dtdparser, xmldtd
from xml.parsers.xmlproc.utils import validate_doc, ErrorRaiser
import wx
from soulforge.lib import xmlutils,headerdata
from soulforge.common import dieroller,sfcontrols,sfsheet,sfuniverses,sfconfig
from soulforge.common.sheets import universes

SFROOTFRAME_ABOUT = 101
SFROOTFRAME_QUIT = 102
SFROOTFRAME_DIEROLLER = 103
SFROOTFRAME_LOAD = 104
SFROOTFRAME_SAVE = 105
SFROOTFRAME_NEW = 106
SFROOTFRAME_EDIT = 107
SFROOTFRAME_CLOSE = 108
SFROOTFRAME_OPTIONS = 109
SFROOTFRAME_SAVEAS = 110
SFSHEET_OK = 401

class sfrootframe(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.DefaultSize)

	self.dom = None
	self.file = None
	self.sh = None
	self.modified = False
	self.config = wx.Config.Get()
	self.history = wx.FileHistory()
	self.config.SetPath("/lastrun")
	self.history.Load(self.config)
	self.config.SetPath("/")
	self.universe = None
	
	pan = wx.Panel(self,-1)
	ts = wx.BoxSizer(wx.VERTICAL)
	ts.Add(pan,1,wx.EXPAND|wx.ALL)
	self.SetSizer(ts)

	filemenu = wx.Menu()
	filemenu.Append(SFROOTFRAME_NEW, _("&New"), _("New character"))
	filemenu.Append(SFROOTFRAME_LOAD, _("&Load"), _("Load character"))
	self.save = wx.MenuItem(filemenu,SFROOTFRAME_SAVE, _("&Save"), _("Save character"))
	filemenu.AppendItem(self.save)
	self.saveas = wx.MenuItem(filemenu,SFROOTFRAME_SAVEAS, _("Save &As..."), _("Save character as..."))
	filemenu.AppendItem(self.saveas)
	self.close = wx.MenuItem(filemenu,SFROOTFRAME_CLOSE, _("&Close"), _("Close character"))
	filemenu.AppendItem(self.close)
	filemenu.AppendSeparator()
	self.recent = wx.Menu()
	self.history.UseMenu(self.recent)
	self.history.AddFilesToMenu()
	filemenu.AppendMenu(-1, _("&Recent files"), self.recent, _("Recently opened files"))
	filemenu.AppendSeparator()
	filemenu.Append(SFROOTFRAME_QUIT, _("E&xit"), _("Quit Soulforge"))

	toolsmenu = wx.Menu()
	toolsmenu.Append(SFROOTFRAME_DIEROLLER, _("&Dieroller"), _("Dieroller"))
	toolsmenu.AppendSeparator()
	toolsmenu.Append(SFROOTFRAME_OPTIONS, _("&Options"), _("Options"))

	helpmenu = wx.Menu()
	helpmenu.Append(SFROOTFRAME_ABOUT, _("&About"), _("About Soulforge"))

	menubar = wx.MenuBar()
	menubar.Append(filemenu, _("&File"))
	menubar.Append(toolsmenu, _("&Tools"))
	menubar.Append(helpmenu, _("&Help"))
	
	self.SetMenuBar(menubar)

	root = wx.FlexGridSizer(6,2,0,0)
	root.AddGrowableCol(1,1)
	root.Add(wx.StaticText(pan,-1, _("Name:")),0,wx.ALIGN_CENTER_VERTICAL)
	self.name = wx.TextCtrl(pan,-1,u"",wx.DefaultPosition,wx.DefaultSize,wx.TE_READONLY)
	root.Add(self.name,1,wx.EXPAND)
	root.Add(wx.StaticText(pan,-1, _("Player:")),0,wx.ALIGN_CENTER_VERTICAL)
	self.player = wx.TextCtrl(pan,-1,u"",wx.DefaultPosition,wx.DefaultSize,wx.TE_READONLY)
	root.Add(self.player,1,wx.EXPAND)
	root.Add(wx.StaticText(pan,-1, _("Universe:")),0,wx.ALIGN_CENTER_VERTICAL)
	self.univname = wx.TextCtrl(pan,-1,u"",wx.DefaultPosition,wx.DefaultSize,wx.TE_READONLY)
	root.Add(self.univname,1,wx.EXPAND)
	root.Add(wx.StaticText(pan,-1, _("Filename:")),0,wx.ALIGN_CENTER_VERTICAL)
	self.filename = wx.TextCtrl(pan,-1,u"",wx.DefaultPosition,wx.DefaultSize,wx.TE_READONLY)
	root.Add(self.filename,1,wx.EXPAND)
	root.Add(wx.Panel(pan,-1))
	self.edit = wx.Button(pan,SFROOTFRAME_EDIT, _("Edit"))
	root.Add(self.edit,1,wx.EXPAND)

	pan.SetSizer(root)
	pan.Fit()
	self.Centre(wx.BOTH)

	self.updategui()

	wx.EVT_MENU(self,SFROOTFRAME_QUIT,self.onquit)
	wx.EVT_MENU(self,SFROOTFRAME_ABOUT,self.onabout)
	wx.EVT_MENU(self,SFROOTFRAME_DIEROLLER,self.ondieroller)
	wx.EVT_MENU(self,SFROOTFRAME_LOAD,self.onload)
	wx.EVT_MENU(self,SFROOTFRAME_SAVE,self.onsave)
	wx.EVT_MENU(self,SFROOTFRAME_CLOSE,self.onclose)
	wx.EVT_MENU(self,SFROOTFRAME_NEW,self.onnew)
	wx.EVT_MENU(self,SFROOTFRAME_OPTIONS,self.onoptions)
	wx.EVT_MENU(self,SFROOTFRAME_SAVEAS,self.onsaveas)
	wx.EVT_MENU_RANGE(self,wx.ID_FILE1,wx.ID_FILE9,self.onrecent)
	wx.EVT_BUTTON(self,SFSHEET_OK,self.onsheetok)
	wx.EVT_BUTTON(self,SFROOTFRAME_EDIT,self.onedit)

    def onquit(self,event):
        if self.modified:
	    err = wx.MessageDialog(self, _("Character is still unsaved.  Quit anyway?"), _("Are you sure?"),wx.OK|wx.CANCEL)
	    err.Centre(wx.BOTH)
	    ret = err.ShowModal()
	    err.Destroy()
	    if ret == wx.ID_CANCEL:
	        return
        self.config.SetPath("/lastrun")
	self.history.Save(self.config)
	self.config.SetPath("/")
        self.Close(True)

    def onabout(self,event):
        abt = wx.MessageDialog(self, _("Soulforge by Christopher Han <xiphux@gmail.com>\nCopyright (C) 2005\nLicensed under the GNU GPL"), _("About Soulforge"),wx.OK)
	abt.ShowModal()
	abt.Destroy()

    def ondieroller(self,event):
        dr = dieroller.dieroller(self,-1, _("Dieroller"))
	dr.Show(True)

    def invalid(self):
	err = wx.MessageDialog(self, _("Error: Selected file is not a valid Soulforge character"), _("Error!"),wx.OK)
	err.Centre(wx.BOTH)
	err.ShowModal()
	err.Destroy()

    def parsefile(self, fp):
        try:
	    t = xmlutils.loaddata(fp)
	except:
	    self.invalid()
	    return False
	rt = t.documentElement
	if rt.nodeName != "soulforge_character":
	    self.invalid()
	    return False
        uni = rt.getAttribute("universe")
	if uni:
	    tmp = universes.getuniverse(uni)
	    if tmp:
	        self.universe = tmp()
	    dtd = self.universe.dtd()
	    if dtd:
	        if headerdata.options.debug:
		    print dtd
	        docstring = xmlutils.load(fp)
		dtddata = xmldtd.load_dtd_string(dtd)
	        if headerdata.options.debug:
                    from xml.parsers.xmlproc.utils import ErrorPrinter
		    docpointer = cStringIO.StringIO(docstring)
		    parser = xmlval.XMLValidator()
		    parser.dtd = dtddata
		    parser.set_error_handler(ErrorPrinter(parser,out=sys.stderr))
		    parser.read_from(docpointer)
		    parser.close()
		    docpointer.close()
		    del docpointer
		    del parser
		docpointer = cStringIO.StringIO(docstring)
	        parser = xmlval.XMLValidator()
		parser.dtd = dtddata
	        parser.set_error_handler(ErrorRaiser(parser))
	        try:
	            parser.read_from(docpointer)
		    parser.close()
		    docpointer.close()
	            del parser
	        except:
	            err = wx.MessageDialog(self, _("Error: Character data is malformed"), _("Error!"),wx.OK)
	            err.Centre(wx.BOTH)
	            err.ShowModal()
	            err.Destroy()
	            return False
		if headerdata.options.debug:
		    print "Character data is legitimate"
	    else:
	        if headerdata.options.debug:
		    print "Character has no DOCTYPE structure definition, proceed with caution..."
	else:
	    err = wx.MessageDialog(self, _("Error: Character has invalid or no universe"), _("Error!"),wx.OK)
	    err.Centre(wx.BOTH)
	    err.ShowModal()
	    err.Destroy()
	    return False
	return t
	
    def loadfile(self, fp):
        if self.file == fp:
	    return
	ret = self.parsefile(fp)
	if ret:
	    if self.dom and self.modified:
	        err = wx.MessageDialog(self, _("If you load this character sheet, current character's changes will be cleared.  Are you sure?"), _("Are you sure?"),wx.OK|wx.CANCEL)
		err.Centre(wx.BOTH)
		rc = err.ShowModal()
		err.Destroy()
		if rc == wx.ID_CANCEL:
		    return
	    self.dom = ret
	    self.file = fp
	else:
	    return
	self.modified = False
	self.populatefields()
	self.updategui()
	self.history.AddFileToHistory(self.file)
	self.config.Write(headerdata.SF_CONFIGKEY_LOADDIR, os.path.dirname(self.file))
	self.config.Flush(True)

    def onload(self,event):
        loaddlg = wx.FileDialog(self, _("Load character"),self.config.Read(headerdata.SF_CONFIGKEY_LOADDIR),"", headerdata.SF_FILEMASK,wx.OPEN|wx.FILE_MUST_EXIST)
	if loaddlg.ShowModal() == wx.ID_OK:
	    self.loadfile(loaddlg.GetPath())
	loaddlg.Destroy()
    
    def onrecent(self,event):
        recentfile = self.history.GetHistoryFile(event.GetId() - wx.ID_FILE1)
	if recentfile:
	    if not os.path.exists(recentfile):
	        err = wx.MessageDialog(self, _("Error: Selected file no longer exists"), _("Error!"),wx.OK)
		err.Centre(wx.BOTH)
		err.ShowModal()
		err.Destroy()
		return
	    self.loadfile(recentfile)

    def writefile(self):
	if self.file:
	    xmlutils.savedata(self.dom, self.file, self.config.Read(headerdata.SF_CONFIGKEY_COMPRESS,headerdata.SF_CONFIGDEFAULT_COMPRESS), self.universe.dtd())
	    self.modified = False
	    self.history.AddFileToHistory(self.file)
	self.populatefields()
	self.updategui()

    def onsaveas(self,event):
        if not self.dom:
	    err = wx.MessageDialog(self, _("Error: No character data to save"), _("Error!"),wx.OK)
	    err.Centre(wx.BOTH)
	    err.ShowModal()
	    err.Destroy()
	    return False
	savedlg = wx.FileDialog(self, _("Save character"),self.config.Read(headerdata.SF_CONFIGKEY_SAVEDIR),"", headerdata.SF_FILEMASK,wx.SAVE|wx.OVERWRITE_PROMPT)
	if savedlg.ShowModal() == wx.ID_OK:
	    self.file = savedlg.GetPath()
	    self.config.Write(headerdata.SF_CONFIGKEY_SAVEDIR, os.path.dirname(self.file))
	    self.config.Flush(True)
	savedlg.Destroy()
	self.writefile()
	return True

    def onsave(self,event):
        if not self.file:
	    ret = self.onsaveas(event)
	    if not ret:
	        return
	self.writefile()

    def onnew(self,event):
        if self.dom:
	    err = wx.MessageDialog(self, _("If you start a new sheet, previous character data will be cleared.  Are you sure?"), _("Are you sure?"),wx.OK|wx.CANCEL)
	    err.Centre(wx.BOTH)
	    ret = err.ShowModal()
	    err.Destroy()
	    if ret == wx.ID_OK:
	        del self.dom
		self.dom = None
		self.file = None
		self.populatefields()
		self.updategui()
	    else:
	        return
        un = []
	for i in sfuniverses.universes:
	    un.append(_(i))
	uni = wx.SingleChoiceDialog(self, _("Choose a universe:"), _("Universe"),un)
	ret = uni.ShowModal()
	if ret == wx.ID_OK:
	    self.universe = universes.getuniverse(uni.GetStringSelection())()
	    if self.universe:
                self.sh = sfsheet.sfsheet(self,-1,self.universe)
	        self.sh.Show()
	uni.Destroy()

    def onsheetok(self,event):
        del self.dom
	doctype = dom.getDOMImplementation().createDocumentType("soulforge_character", None, '')
	self.dom = dom.getDOMImplementation().createDocument(None,"soulforge_character",doctype)
	self.universe.sheet2xml(self.sh.sheet,self.dom)
	self.sh.Destroy()
	self.populatefields()
	self.modified = True
	self.updategui()

    def onedit(self,event):
        uni = self.dom.documentElement.getAttribute("universe")
	self.universe = universes.getuniverse(uni)()
	if self.universe:
            self.sh = sfsheet.sfsheet(self,-1,self.universe)
	    self.universe.xml2sheet(self.dom,self.sh.sheet)
	    self.sh.Show()

    def onoptions(self,event):
        conf = sfconfig.sfconfig(self,-1)
	conf.ShowModal()

    def populatefields(self):
        if self.sh:
	    self.name.SetValue(self.sh.sheet.name.GetValue())
	    self.player.SetValue(self.sh.sheet.player.GetValue())
	    self.univname.SetValue(self.sh.universe.name())
	elif self.dom:
	    self.name.SetValue(xmlutils.getnodetext(self.dom.getElementsByTagName("name")[0]))
	    self.player.SetValue(xmlutils.getnodetext(self.dom.getElementsByTagName("player")[0]))
	    self.univname.SetValue(self.dom.documentElement.getAttribute("universe"))
	else:
	    self.name.SetValue(u"")
	    self.player.SetValue(u"")
	    self.univname.SetValue(u"")
	if self.file:
	    self.filename.SetValue(self.file)
	else:
	    self.filename.SetValue(u"")

    def updategui(self):
        self.save.Enable(self.modified)
	if self.dom:
	    self.edit.Enable(True)
	    self.saveas.Enable(True)
	else:
	    self.edit.Enable(False)
	    self.saveas.Enable(False)
	if self.file or self.modified:
	    self.close.Enable(True)
	else:
	    self.close.Enable(False)

    def onclose(self,event):
        if self.modified:
	    err = wx.MessageDialog(self, _("Character is still unsaved.  Close anyway?"), _("Are you sure?"),wx.OK|wx.CANCEL)
	    err.Centre(wx.BOTH)
	    ret = err.ShowModal()
	    err.Destroy()
	    if ret == wx.ID_CANCEL:
	        return
	self.file = None
	del self.dom
	self.dom = None
	if self.sh:
	    self.sh.Destroy()
	    self.sh = None
	self.modified = False
	self.populatefields()
	self.updategui()
