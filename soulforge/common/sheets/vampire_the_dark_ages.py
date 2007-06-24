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
from soulforge.common.sfcontrols import sfstat, sfpool, sfhealth
from soulforge.common.sheets import vampire_the_dark_ages_data

class vampire_the_dark_ages(wx.ScrolledWindow):
    def __init__(self, *args, **kwds):
        # begin wxGlade: vampire_the_dark_ages.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.ScrolledWindow.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, -1, _("Name:"))
        self.name = wx.TextCtrl(self, -1, "")
        self.label_2 = wx.StaticText(self, -1, _("Nature:"))
        self.nature = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.label_3 = wx.StaticText(self, -1, _("Generation:"))
        self.generation = wx.SpinCtrl(self, -1, "13", min=1, max=15)
        self.label_4 = wx.StaticText(self, -1, _("Player:"))
        self.player = wx.TextCtrl(self, -1, "")
        self.label_5 = wx.StaticText(self, -1, _("Demeanor:"))
        self.demeanor = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.label_6 = wx.StaticText(self, -1, _("Haven:"))
        self.haven = wx.TextCtrl(self, -1, "")
        self.label_7 = wx.StaticText(self, -1, _("Chronicle:"))
        self.chronicle = wx.TextCtrl(self, -1, "")
        self.label_9 = wx.StaticText(self, -1, _("Clan:"))
        self.clan = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.label_8 = wx.StaticText(self, -1, _("Concept:"))
        self.concept = wx.TextCtrl(self, -1, "")
        self.static_line_1 = wx.StaticLine(self, -1)
        self.label_10 = wx.StaticText(self, -1, _("Attributes"))
        self.static_line_2 = wx.StaticLine(self, -1)
        self.label_11 = wx.StaticText(self, -1, _("Physical"))
        self.label_12 = wx.StaticText(self, -1, _("Social"))
        self.label_13 = wx.StaticText(self, -1, _("Mental"))
        self.strength = sfstat(self, -1, label=_("Strength"))
        self.charisma = sfstat(self, -1, label=_("Charisma"))
        self.perception = sfstat(self, -1, label=_("Perception"))
        self.dexterity = sfstat(self, -1, label=_("Dexterity"))
        self.manipulation = sfstat(self, -1, label=_("Manipulation"))
        self.intelligence = sfstat(self, -1, label=_("Intelligence"))
        self.stamina = sfstat(self, -1, label=_("Stamina"))
        self.appearance = sfstat(self, -1, label=_("Appearance"))
        self.wits = sfstat(self, -1, label=_("Wits"))
        self.static_line_3 = wx.StaticLine(self, -1)
        self.label_14 = wx.StaticText(self, -1, _("Abilities"))
        self.static_line_4 = wx.StaticLine(self, -1)
        self.label_15 = wx.StaticText(self, -1, _("Talents"))
        self.label_16 = wx.StaticText(self, -1, _("Skills"))
        self.label_17 = wx.StaticText(self, -1, _("Knowledges"))
	self.acting = sfstat(self, -1, label=_("Acting"))
        self.alertness = sfstat(self, -1, label=_("Alertness"))
        self.animalken = sfstat(self, -1, label=_("Animal Ken"))
        self.academics = sfstat(self, -1, label=_("Academics"))
        self.athletics = sfstat(self, -1, label=_("Athletics"))
	self.archery = sfstat(self, -1, label=_("Archery"))
        self.crafts = sfstat(self, -1, label=_("Crafts"))
        self.hearth_wisdom = sfstat(self, -1, label=_("Hearth Wisdom"))
        self.brawl = sfstat(self, -1, label=_("Brawl"))
        self.dodge = sfstat(self, -1, label=_("Dodge"))
        self.etiquette = sfstat(self, -1, label=_("Etiquette"))
        self.investigation = sfstat(self, -1, label=_("Investigation"))
        self.empathy = sfstat(self, -1, label=_("Empathy"))
        self.herbalism = sfstat(self, -1, label=_("Herbalism"))
        self.law = sfstat(self, -1, label=_("Law"))
        self.melee = sfstat(self, -1, label=_("Melee"))
        self.linguistics = sfstat(self, -1, label=_("Linguistics"))
        self.intimidation = sfstat(self, -1, label=_("Intimidation"))
	self.larceny = sfstat(self, -1, label=_("Larceny"))
        self.music = sfstat(self, -1, label=_("Music"))
        self.medicine = sfstat(self, -1, label=_("Medicine"))
        self.leadership = sfstat(self, -1, label=_("Leadership"))
        self.ride = sfstat(self, -1, label=_("Ride"))
        self.occult = sfstat(self, -1, label=_("Occult"))
        self.stealth = sfstat(self, -1, label=_("Stealth"))
        self.politics = sfstat(self, -1, label=_("Politics"))
        self.subterfuge = sfstat(self, -1, label=_("Subterfuge"))
        self.survival = sfstat(self, -1, label=_("Survival"))
        self.science = sfstat(self, -1, label=_("Science"))
	self.seneschal = sfstat(self, -1, label=_("Seneschal"))
        self.static_line_5 = wx.StaticLine(self, -1)
        self.label_18 = wx.StaticText(self, -1, _("Advantages"))
        self.static_line_6 = wx.StaticLine(self, -1)
        self.label_19 = wx.StaticText(self, -1, _("Backgrounds"))
        self.label_20 = wx.StaticText(self, -1, _("Disciplines"))
        self.label_21 = wx.StaticText(self, -1, _("Virtues"))
        self.background_1_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.background_1_level = sfstat(self, -1)
        self.discipline_1_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.discipline_1_level = sfstat(self, -1)
        self.conscience_conviction_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.conscience_conviction_level = sfstat(self, -1)
        self.background_2_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.background_2_level = sfstat(self, -1)
        self.discipline_2_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.discipline_2_level = sfstat(self, -1)
        self.panel_1 = wx.Panel(self, -1)
        self.background_3_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.background_3_level = sfstat(self, -1)
        self.discipline_3_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.discipline_3_level = sfstat(self, -1)
        self.panel_2 = wx.Panel(self, -1)
        self.background_4_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.background_4_level = sfstat(self, -1)
        self.discipline_4_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.discipline_4_level = sfstat(self, -1)
        self.selfcontrol_instinct_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.selfcontrol_instinct_level = sfstat(self, -1)
        self.background_5_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.background_5_level = sfstat(self, -1)
        self.discipline_5_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.discipline_5_level = sfstat(self, -1)
        self.panel_3 = wx.Panel(self, -1)
        self.background_6_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.background_6_level = sfstat(self, -1)
        self.discipline_6_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.discipline_6_level = sfstat(self, -1)
        self.panel_4 = wx.Panel(self, -1)
        self.background_7_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.background_7_level = sfstat(self, -1)
        self.discipline_7_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.discipline_7_level = sfstat(self, -1)
        self.courage_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.courage_level = sfstat(self, -1)
        self.static_line_7 = wx.StaticLine(self, -1)
        self.static_line_8 = wx.StaticLine(self, -1)
        self.label_22 = wx.StaticText(self, -1, _("Merits"))
        self.static_line_9 = wx.StaticLine(self, -1)
        self.merit_1 = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_SORT)
        self.merit_2 = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_SORT)
        self.merit_3 = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_SORT)
        self.static_line_8a = wx.StaticLine(self, -1)
        self.label_22a = wx.StaticText(self, -1, _("Flaws"))
        self.static_line_9a = wx.StaticLine(self, -1)
        self.flaw_1 = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_SORT)
        self.flaw_2 = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_SORT)
        self.flaw_3 = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_SORT)
        self.static_line_10 = wx.StaticLine(self, -1)
        self.label_23 = wx.StaticText(self, -1, _("Road"))
        self.static_line_11 = wx.StaticLine(self, -1)
        self.road_name = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.road_level = sfstat(self, -1, buttons=10)
        self.static_line_12 = wx.StaticLine(self, -1)
        self.label_24 = wx.StaticText(self, -1, _("Willpower"))
        self.static_line_13 = wx.StaticLine(self, -1)
        self.willpower_max = sfstat(self, -1, buttons=10)
        self.willpower_current = sfpool(self, -1, rows=1, cols=10)
        self.static_line_14 = wx.StaticLine(self, -1)
        self.label_25 = wx.StaticText(self, -1, _("Blood Pool"))
        self.static_line_15 = wx.StaticLine(self, -1)
        self.blood_pool = sfpool(self, -1)
        self.static_line_18 = wx.StaticLine(self, -1)
        self.label_27 = wx.StaticText(self, -1, _("Health"))
        self.static_line_19 = wx.StaticLine(self, -1)
        self.label_28 = wx.StaticText(self, -1, _("Bruised"))
        self.panel_5 = wx.Panel(self, -1)
        self.label_29 = wx.StaticText(self, -1, _("Hurt"))
        self.label_35 = wx.StaticText(self, -1, _("-1"))
        self.label_30 = wx.StaticText(self, -1, _("Injured"))
        self.label_36 = wx.StaticText(self, -1, _("-1"))
        self.label_31 = wx.StaticText(self, -1, _("Wounded"))
        self.label_37 = wx.StaticText(self, -1, _("-2"))
        self.label_32 = wx.StaticText(self, -1, _("Mauled"))
        self.label_38 = wx.StaticText(self, -1, _("-2"))
        self.label_33 = wx.StaticText(self, -1, _("Crippled"))
        self.label_39 = wx.StaticText(self, -1, _("-5"))
        self.label_34 = wx.StaticText(self, -1, _("Incapacitated"))
        self.panel_6 = wx.Panel(self, -1)
        self.health = sfhealth(self, -1, buttons=7)
        self.static_line_16 = wx.StaticLine(self, -1)
        self.label_26 = wx.StaticText(self, -1, _("Experience"))
        self.static_line_17 = wx.StaticLine(self, -1)
        self.experience = wx.SpinCtrl(self, -1, "", min=0, max=100)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
	self.initfields()

    def initfields(self):
	for i in vampire_the_dark_ages_data.archetypes:
	    self.nature.Append(i,None)
	    self.demeanor.Append(i,None)
	for i in vampire_the_dark_ages_data.clans:
	    self.clan.Append(i,None)
	for i in vampire_the_dark_ages_data.backgrounds:
	    self.background_1_name.Append(i,None)
	    self.background_2_name.Append(i,None)
	    self.background_3_name.Append(i,None)
	    self.background_4_name.Append(i,None)
	    self.background_5_name.Append(i,None)
	    self.background_6_name.Append(i,None)
	    self.background_7_name.Append(i,None)
	for i in vampire_the_dark_ages_data.disciplines:
	    self.discipline_1_name.Append(i,None)
	    self.discipline_2_name.Append(i,None)
	    self.discipline_3_name.Append(i,None)
	    self.discipline_4_name.Append(i,None)
	    self.discipline_5_name.Append(i,None)
	    self.discipline_6_name.Append(i,None)
	    self.discipline_7_name.Append(i,None)
	for i in vampire_the_dark_ages_data.conscience_conviction:
	    self.conscience_conviction_name.Append(i,None)
	for i in vampire_the_dark_ages_data.selfcontrol_instinct:
	    self.selfcontrol_instinct_name.Append(i,None)
	for i in vampire_the_dark_ages_data.courage:
	    self.courage_name.Append(i,None)
	for i in vampire_the_dark_ages_data.roads:
	    self.road_name.Append(i,None)
	self.merit_1.Append('',None)
	self.merit_2.Append('',None)
	self.merit_3.Append('',None)
	self.flaw_1.Append('',None)
	self.flaw_2.Append('',None)
	self.flaw_3.Append('',None)
	for i,j in vampire_the_dark_ages_data.merits.iteritems():
	    for k in j.tolist():
	        st = i + " (" + str(k) + "-pt. Merit)"
		self.merit_1.Append(st,(i,k,))
		self.merit_2.Append(st,(i,k,))
		self.merit_3.Append(st,(i,k,))
        for i,j in vampire_the_dark_ages_data.flaws.iteritems():
	    for k in j.tolist():
	        st = i + " (" + str(k) + "-pt. Flaw)"
		self.flaw_1.Append(st,(i,k,))
		self.flaw_2.Append(st,(i,k,))
		self.flaw_3.Append(st,(i,k,))

    def __set_properties(self):
        # begin wxGlade: vampire_the_dark_ages.__set_properties
        self.SetScrollRate(10, 10)
        self.nature.SetSelection(0)
        self.demeanor.SetSelection(0)
        self.clan.SetSelection(0)
        self.background_1_name.SetSelection(0)
        self.discipline_1_name.SetSelection(-1)
        self.conscience_conviction_name.SetSelection(-1)
        self.background_2_name.SetSelection(-1)
        self.discipline_2_name.SetSelection(-1)
        self.background_3_name.SetSelection(-1)
        self.discipline_3_name.SetSelection(-1)
        self.background_4_name.SetSelection(-1)
        self.discipline_4_name.SetSelection(-1)
        self.selfcontrol_instinct_name.SetSelection(-1)
        self.background_5_name.SetSelection(-1)
        self.discipline_5_name.SetSelection(-1)
        self.background_6_name.SetSelection(-1)
        self.discipline_6_name.SetSelection(-1)
        self.background_7_name.SetSelection(-1)
        self.discipline_7_name.SetSelection(-1)
        self.courage_name.SetSelection(-1)
        self.merit_1.SetSelection(-1)
        self.merit_2.SetSelection(-1)
        self.merit_3.SetSelection(-1)
        self.flaw_1.SetSelection(-1)
        self.flaw_2.SetSelection(-1)
        self.flaw_3.SetSelection(-1)
        self.road_name.SetSelection(-1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: vampire_the_dark_ages.__do_layout
        sizer_1 = wx.FlexGridSizer(6, 1, 0, 0)
        sizer_28 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_38 = wx.BoxSizer(wx.VERTICAL)
        sizer_39 = wx.BoxSizer(wx.VERTICAL)
        sizer_40 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_41 = wx.BoxSizer(wx.VERTICAL)
        sizer_43 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_5 = wx.FlexGridSizer(7, 2, 0, 0)
        sizer_42 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_31 = wx.BoxSizer(wx.VERTICAL)
        sizer_36 = wx.BoxSizer(wx.VERTICAL)
        sizer_37 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_34 = wx.BoxSizer(wx.VERTICAL)
        sizer_35 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_32 = wx.BoxSizer(wx.VERTICAL)
        sizer_33 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_29 = wx.BoxSizer(wx.VERTICAL)
        sizer_30a = wx.BoxSizer(wx.HORIZONTAL)
        sizer_30 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_4 = wx.GridSizer(9, 3, 0, 0)
        sizer_27 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_26 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_25 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_24 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_22 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_21 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_19 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_3 = wx.GridSizer(12, 3, 0, 0)
        grid_sizer_2 = wx.GridSizer(5, 3, 0, 0)
        grid_sizer_1 = wx.GridSizer(3, 3, 0, 0)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.label_1, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_2.Add(self.name, 1, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_3.Add(self.label_2, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_3.Add(self.nature, 1, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_4.Add(self.label_3, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_4.Add(self.generation, 1, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_1.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_5.Add(self.label_4, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_5.Add(self.player, 1, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_1.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_6.Add(self.label_5, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_6.Add(self.demeanor, 1, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_1.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_7.Add(self.label_6, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_7.Add(self.haven, 1, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_1.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_8.Add(self.label_7, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_8.Add(self.chronicle, 1, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_1.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_10.Add(self.label_9, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_10.Add(self.clan, 1, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_1.Add(sizer_10, 1, wx.EXPAND, 0)
        sizer_9.Add(self.label_8, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_9.Add(self.concept, 1, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_1.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_1.Add(grid_sizer_1, 0, wx.EXPAND, 2)
        grid_sizer_2.Add(self.static_line_1, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.label_10, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_2.Add(self.static_line_2, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.label_11, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_2.Add(self.label_12, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_2.Add(self.label_13, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_2.Add(self.strength, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.charisma, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.perception, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.dexterity, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.manipulation, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.intelligence, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.stamina, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.appearance, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.wits, 1, wx.EXPAND, 0)
        sizer_1.Add(grid_sizer_2, 0, wx.EXPAND, 0)
        grid_sizer_3.Add(self.static_line_3, 0, wx.EXPAND, 0)
        grid_sizer_3.Add(self.label_14, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_3.Add(self.static_line_4, 0, wx.EXPAND, 0)
        grid_sizer_3.Add(self.label_15, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_3.Add(self.label_16, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_3.Add(self.label_17, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
	grid_sizer_3.Add(self.acting, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.animalken, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.academics, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.alertness, 1, wx.EXPAND, 0)
	grid_sizer_3.Add(self.archery, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.hearth_wisdom, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.athletics, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.crafts, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.investigation, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.brawl, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.etiquette, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.law, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.dodge, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.herbalism, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.linguistics, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.empathy, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.melee, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.medicine, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.intimidation, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.music, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.occult, 1, wx.EXPAND, 0)
	grid_sizer_3.Add(self.larceny, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.ride, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.politics, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.leadership, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.stealth, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.science, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.subterfuge, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.survival, 1, wx.EXPAND, 0)
	grid_sizer_3.Add(self.seneschal, 1, wx.EXPAND, 0)
        sizer_1.Add(grid_sizer_3, 0, wx.EXPAND, 0)
        grid_sizer_4.Add(self.static_line_5, 0, wx.EXPAND, 0)
        grid_sizer_4.Add(self.label_18, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_4.Add(self.static_line_6, 0, wx.EXPAND, 0)
        grid_sizer_4.Add(self.label_19, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_4.Add(self.label_20, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        grid_sizer_4.Add(self.label_21, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_11.Add(self.background_1_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_11.Add(self.background_1_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_11, 1, wx.EXPAND, 0)
        sizer_12.Add(self.discipline_1_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_12.Add(self.discipline_1_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_13.Add(self.conscience_conviction_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_13.Add(self.conscience_conviction_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_13, 1, wx.EXPAND, 0)
        sizer_14.Add(self.background_2_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_14.Add(self.background_2_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_14, 1, wx.EXPAND, 0)
        sizer_15.Add(self.discipline_2_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_15.Add(self.discipline_2_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_15, 1, wx.EXPAND, 0)
        grid_sizer_4.Add(self.panel_1, 1, wx.EXPAND, 0)
        sizer_16.Add(self.background_3_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_16.Add(self.background_3_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_16, 1, wx.EXPAND, 0)
        sizer_17.Add(self.discipline_3_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_17.Add(self.discipline_3_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_17, 1, wx.EXPAND, 0)
        grid_sizer_4.Add(self.panel_2, 1, wx.EXPAND, 0)
        sizer_18.Add(self.background_4_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_18.Add(self.background_4_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_18, 1, wx.EXPAND, 0)
        sizer_19.Add(self.discipline_4_name, 1, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        sizer_19.Add(self.discipline_4_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_19, 1, wx.EXPAND, 0)
        sizer_20.Add(self.selfcontrol_instinct_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_20.Add(self.selfcontrol_instinct_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_20, 1, wx.EXPAND, 0)
        sizer_21.Add(self.background_5_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_21.Add(self.background_5_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_21, 1, wx.EXPAND, 0)
        sizer_22.Add(self.discipline_5_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_22.Add(self.discipline_5_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_22, 1, wx.EXPAND, 0)
        grid_sizer_4.Add(self.panel_3, 1, wx.EXPAND, 0)
        sizer_23.Add(self.background_6_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_23.Add(self.background_6_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_23, 1, wx.EXPAND, 0)
        sizer_24.Add(self.discipline_6_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_24.Add(self.discipline_6_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_24, 1, wx.EXPAND, 0)
        grid_sizer_4.Add(self.panel_4, 1, wx.EXPAND, 0)
        sizer_25.Add(self.background_7_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_25.Add(self.background_7_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_25, 1, wx.EXPAND, 0)
        sizer_26.Add(self.discipline_7_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_26.Add(self.discipline_7_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_26, 1, wx.EXPAND, 0)
        sizer_27.Add(self.courage_name, 1, wx.FIXED_MINSIZE, 0)
        sizer_27.Add(self.courage_level, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(sizer_27, 1, wx.EXPAND, 0)
        sizer_1.Add(grid_sizer_4, 0, wx.EXPAND, 0)
        sizer_1.Add(self.static_line_7, 0, wx.EXPAND, 0)
        sizer_30.Add(self.static_line_8, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_30.Add(self.label_22, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_30.Add(self.static_line_9, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_29.Add(sizer_30, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_29.Add(self.merit_1, 0, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        sizer_29.Add(self.merit_2, 0, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        sizer_29.Add(self.merit_3, 0, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        sizer_30a.Add(self.static_line_8a, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_30a.Add(self.label_22a, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_30a.Add(self.static_line_9a, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_29.Add(sizer_30a, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_29.Add(self.flaw_1, 0, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        sizer_29.Add(self.flaw_2, 0, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        sizer_29.Add(self.flaw_3, 0, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        sizer_28.Add(sizer_29, 1, 0, 0)
        sizer_33.Add(self.static_line_10, 1, wx.EXPAND, 0)
        sizer_33.Add(self.label_23, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_33.Add(self.static_line_11, 1, wx.EXPAND, 0)
        sizer_32.Add(sizer_33, 0, wx.EXPAND, 0)
        sizer_32.Add(self.road_name, 0, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        sizer_32.Add(self.road_level, 0, wx.EXPAND, 0)
        sizer_31.Add(sizer_32, 1, wx.EXPAND, 0)
        sizer_35.Add(self.static_line_12, 1, wx.EXPAND, 0)
        sizer_35.Add(self.label_24, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_35.Add(self.static_line_13, 1, wx.EXPAND, 0)
        sizer_34.Add(sizer_35, 0, wx.EXPAND, 0)
        sizer_34.Add(self.willpower_max, 0, wx.EXPAND, 0)
        sizer_34.Add(self.willpower_current, 0, wx.EXPAND, 0)
        sizer_31.Add(sizer_34, 1, wx.EXPAND, 0)
        sizer_37.Add(self.static_line_14, 1, wx.EXPAND, 0)
        sizer_37.Add(self.label_25, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_37.Add(self.static_line_15, 1, wx.EXPAND, 0)
        sizer_36.Add(sizer_37, 0, wx.EXPAND, 0)
        sizer_36.Add(self.blood_pool, 0, wx.EXPAND, 0)
        sizer_31.Add(sizer_36, 1, wx.EXPAND, 0)
        sizer_28.Add(sizer_31, 1, 0, 0)
        sizer_42.Add(self.static_line_18, 1, wx.EXPAND, 0)
        sizer_42.Add(self.label_27, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_42.Add(self.static_line_19, 1, wx.EXPAND, 0)
        sizer_41.Add(sizer_42, 0, wx.EXPAND, 0)
        grid_sizer_5.Add(self.label_28, 0, wx.FIXED_MINSIZE, 0)
        grid_sizer_5.Add(self.panel_5, 1, wx.EXPAND, 0)
        grid_sizer_5.Add(self.label_29, 0, wx.FIXED_MINSIZE, 0)
        grid_sizer_5.Add(self.label_35, 0, wx.ALIGN_RIGHT|wx.FIXED_MINSIZE, 0)
        grid_sizer_5.Add(self.label_30, 0, wx.FIXED_MINSIZE, 0)
        grid_sizer_5.Add(self.label_36, 0, wx.ALIGN_RIGHT|wx.FIXED_MINSIZE, 0)
        grid_sizer_5.Add(self.label_31, 0, wx.FIXED_MINSIZE, 0)
        grid_sizer_5.Add(self.label_37, 0, wx.ALIGN_RIGHT|wx.FIXED_MINSIZE, 0)
        grid_sizer_5.Add(self.label_32, 0, wx.FIXED_MINSIZE, 0)
        grid_sizer_5.Add(self.label_38, 0, wx.ALIGN_RIGHT|wx.FIXED_MINSIZE, 0)
        grid_sizer_5.Add(self.label_33, 0, wx.FIXED_MINSIZE, 0)
        grid_sizer_5.Add(self.label_39, 0, wx.ALIGN_RIGHT|wx.FIXED_MINSIZE, 0)
        grid_sizer_5.Add(self.label_34, 0, wx.FIXED_MINSIZE, 0)
        grid_sizer_5.Add(self.panel_6, 1, wx.EXPAND, 0)
        sizer_43.Add(grid_sizer_5, 1, wx.EXPAND, 0)
        sizer_43.Add(self.health, 1, wx.EXPAND, 0)
        sizer_41.Add(sizer_43, 1, wx.EXPAND, 0)
        sizer_38.Add(sizer_41, 0, wx.EXPAND, 0)
        sizer_40.Add(self.static_line_16, 1, wx.EXPAND, 0)
        sizer_40.Add(self.label_26, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_40.Add(self.static_line_17, 1, wx.EXPAND, 0)
        sizer_39.Add(sizer_40, 0, wx.EXPAND, 0)
        sizer_39.Add(self.experience, 0, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        sizer_38.Add(sizer_39, 0, wx.EXPAND, 0)
        sizer_28.Add(sizer_38, 1, 0, 0)
        sizer_1.Add(sizer_28, 0, 0, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        # end wxGlade

# end of class vampire_the_dark_ages

