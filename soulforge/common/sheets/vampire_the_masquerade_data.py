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

from array import array
import wx
from soulforge.lib import xmlutils, headerdata

universe = 'Vampire: The Masquerade'

archetypes = ['', _('Architect'), _('Autocrat'), _('Bon Vivant'), _('Bravo'), _('Caregiver'), _('Celebrant'), _('Child'), _('Competitor'), _('Conformist'), _('Conniver'), _('Curmudgeon'), _('Deviant'), _('Director'), _('Fanatic'), _('Gallant'), _('Judge'), _('Loner'), _('Martyr'), _('Masochist'), _('Monster'), _('Pedagogue'), _('Penitent'), _('Perfectionist'), _('Rebel'), _('Rogue'), _('Survivor'), _('Thrill-Seeker'), _('Traditionalist'), _('Trickster'), _('Visionary')]

clans = ['', _('Brujah'), _('Gangrel'), _('Malkavian'), _('Nosferatu'), _('Toreador'), _('Tremere'), _('Ventrue'), _('Lasombra'), _('Tzimisce'), _('Assamite'), _('Followers of Set'), _('Giovanni'), _('Ravnos')]

backgrounds = ['', _('Allies'), _('Contacts'), _('Fame'), _('Generation'), _('Herd'), _('Influence'), _('Mentor'), _('Resources'), _('Retainers'), _('Status')]

disciplines = ['', _('Animalism'), _('Auspex'), _('Celerity'), _('Chimerstry'), _('Dementation'), _('Dominate'), _('Fortitude'), _('Necromancy'), _('Obfuscate'), _('Obtenebration'), _('Potence'), _('Presence'), _('Protean'), _('Quietus'), _('Serpentis'), _('Thaumaturgy'), _('Vicissitude')]

conscience_conviction = ['', _('Conscience'), _('Conviction')]

selfcontrol_instinct = ['', _('Self-Control'), _('Instinct')]

courage = ['', _('Courage')]

humanity_path = ['', _('Humanity'), _('Path of Blood'), _('Path of Bones'), _('Path of Night'), _('Path of Metamorphosis'), _('Path of Paradox'), _('Path of Typhon')]

merits = {
	'Acute Sense': array('i', [1]),
	'Ambidextrous': array('i', [1]),
	'Eat Food': array('i', [1]),
	'Catlike Balance': array('i', [1]),
	'Blush of Health': array('i', [2]),
	'Enchanting Voice': array('i', [2]),
	'Daredevil': array('i', [3]),
	'Efficient Digestion': array('i', [3]),
	'Huge Size': array('i', [4]),
	'Common Sense': array('i', [1]),
	'Concentration': array('i', [1]),
	'Time Sense': array('i', [1]),
	'Code of Honor': array('i', [2]),
	'Eidetic Memory': array('i', [2]),
	'Light Sleeper': array('i', [2]),
	'Natural Linguist': array('i', [2]),
	'Calm Heart': array('i', [3]),
	'Iron Will': array('i', [3]),
	'Prestigious Sire': array('i', [1]),
	'Natural Leader': array('i', [1]),
	'Debt of Gratitude': array('i', [1, 2, 3]),
	'Medium': array('i', [2]),
	'Magic Resistance': array('i', [2]),
	'Oracular Ability': array('i', [3]),
	'Spirit Mentor': array('i', [3]),
	'Unbondable': array('i', [3]),
	'Lucky': array('i', [3]),
	'True Love': array('i', [4]),
	'Nine Lives': array('i', [6]),
	'True Faith': array('i', [7]),
}

flaws = {
	'Smell of the Grave': array('i', [1]),
	'Short': array('i', [1]),
	'Hard of Hearing': array('i', [1]),
	'14th Generation': array('i', [2]),
	'Infectious Bite': array('i', [2]),
	'Bad Sight': array('i', [1, 3]),
	'One Eye': array('i', [2]),
	'Disfigured': array('i', [2]),
	'Child': array('i', [3]),
	'Deformity': array('i', [3]),
	'Lame': array('i', [3]),
	'Monstrous': array('i', [3]),
	'Permanent Wound': array('i', [3]),
	'Slow Healing': array('i', [3]),
	'Addiction': array('i', [3]),
	'Mute': array('i', [4]),
	'Thin Blood': array('i', [4]),
	'Disease Carrier': array('i', [4]),
	'Deaf': array('i', [4]),
	'Flesh of the Corpse': array('i', [5]),
	'Blind': array('i', [6]),
	'Deep Sleeper': array('i', [1]),
	'Nightmares': array('i', [1]),
	'Phobia': array('i', [2]),
	'Prey Exclusion': array('i', [1]),
	'Shy': array('i', [1]),
	'Soft-Hearted': array('i', [1]),
	'Speech Impediment': array('i', [1]),
	'Short Fuse': array('i', [2]),
	'Territorial': array('i', [2]),
	'Vengeful': array('i', [2]),
	'Amnesia': array('i', [2]),
	'Lunacy': array('i', [2]),
	'Weak-Willed': array('i', [3]),
	'Conspicuous Consumption': array('i', [4]),
	'Dark Secret': array('i', [1]),
	'Infamous Sire': array('i', [1]),
	'Mistaken Identity': array('i', [1]),
	'Sire\'s Resentment': array('i', [1]),
	'Enemy': array('i', [1, 2, 3, 4, 5]),
	'Hunted': array('i', [4]),
	'Probationary Sect Member': array('i', [4]),
	'Touch of Frost': array('i', [1]),
	'Repulsed by Garlic': array('i', [1]),
	'Cursed': array('i', [1, 2, 3, 4, 5]),
	'Cast No Reflection': array('i', [1]),
	'Eerie Presence': array('i', [2]),
	'Repelled by Crosses': array('i', [3]),
	'Can\'t Cross Running Water': array('i', [3]),
	'Haunted': array('i', [3]),
	'Grip of the Damned': array('i', [4]),
	'Dark Fate': array('i', [5]),
	'Light-Sensitive': array('i', [5]),
}

def sheet2xml(sheet,dom):
    root = dom.documentElement
    root.setAttribute("universe",universe)

    mknode = xmlutils.mktextnode
    mkelement = dom.createElement

    root.appendChild(mknode(dom,"name",sheet.name.GetValue()))
    root.appendChild(mknode(dom,"player",sheet.player.GetValue()))
    root.appendChild(mknode(dom,"chronicle",sheet.chronicle.GetValue()))
    root.appendChild(mknode(dom,"nature",sheet.nature.GetValue()))
    root.appendChild(mknode(dom,"demeanor",sheet.demeanor.GetValue()))
    root.appendChild(mknode(dom,"clan",sheet.clan.GetValue()))
    root.appendChild(mknode(dom,"generation",sheet.generation.GetValue()))
    root.appendChild(mknode(dom,"haven",sheet.haven.GetValue()))
    root.appendChild(mknode(dom,"concept",sheet.concept.GetValue()))

    node = mkelement("attributes")
    node2 = mkelement("physical")
    node2.appendChild(mknode(dom,"strength",sheet.strength.value))
    node2.appendChild(mknode(dom,"dexterity",sheet.dexterity.value))
    node2.appendChild(mknode(dom,"stamina",sheet.stamina.value))
    node.appendChild(node2)
    node2 = mkelement("social")
    node2.appendChild(mknode(dom,"charisma",sheet.charisma.value))
    node2.appendChild(mknode(dom,"manipulation",sheet.manipulation.value))
    node2.appendChild(mknode(dom,"appearance",sheet.appearance.value))
    node.appendChild(node2)
    node2 = mkelement("mental")
    node2.appendChild(mknode(dom,"perception",sheet.perception.value))
    node2.appendChild(mknode(dom,"intelligence",sheet.intelligence.value))
    node2.appendChild(mknode(dom,"wits",sheet.wits.value))
    node.appendChild(node2)
    root.appendChild(node)

    node = mkelement("abilities")
    node2 = mkelement("talents")
    node2.appendChild(mknode(dom,"alertness",sheet.alertness.value))
    node2.appendChild(mknode(dom,"athletics",sheet.athletics.value))
    node2.appendChild(mknode(dom,"brawl",sheet.brawl.value))
    node2.appendChild(mknode(dom,"dodge",sheet.dodge.value))
    node2.appendChild(mknode(dom,"empathy",sheet.empathy.value))
    node2.appendChild(mknode(dom,"expression",sheet.expression.value))
    node2.appendChild(mknode(dom,"intimidation",sheet.intimidation.value))
    node2.appendChild(mknode(dom,"leadership",sheet.leadership.value))
    node2.appendChild(mknode(dom,"streetwise",sheet.streetwise.value))
    node2.appendChild(mknode(dom,"subterfuge",sheet.subterfuge.value))
    node.appendChild(node2)
    node2 = mkelement("skills")
    node2.appendChild(mknode(dom,"animalken",sheet.animalken.value))
    node2.appendChild(mknode(dom,"crafts",sheet.crafts.value))
    node2.appendChild(mknode(dom,"drive",sheet.drive.value))
    node2.appendChild(mknode(dom,"etiquette",sheet.etiquette.value))
    node2.appendChild(mknode(dom,"firearms",sheet.firearms.value))
    node2.appendChild(mknode(dom,"melee",sheet.melee.value))
    node2.appendChild(mknode(dom,"performance",sheet.performance.value))
    node2.appendChild(mknode(dom,"security",sheet.security.value))
    node2.appendChild(mknode(dom,"stealth",sheet.stealth.value))
    node2.appendChild(mknode(dom,"survival",sheet.survival.value))
    node.appendChild(node2)
    node2 = mkelement("knowledges")
    node2.appendChild(mknode(dom,"academics",sheet.academics.value))
    node2.appendChild(mknode(dom,"computer",sheet.computer.value))
    node2.appendChild(mknode(dom,"finance",sheet.finance.value))
    node2.appendChild(mknode(dom,"investigation",sheet.investigation.value))
    node2.appendChild(mknode(dom,"law",sheet.law.value))
    node2.appendChild(mknode(dom,"linguistics",sheet.linguistics.value))
    node2.appendChild(mknode(dom,"medicine",sheet.medicine.value))
    node2.appendChild(mknode(dom,"occult",sheet.occult.value))
    node2.appendChild(mknode(dom,"politics",sheet.politics.value))
    node2.appendChild(mknode(dom,"science",sheet.science.value))
    node.appendChild(node2)
    root.appendChild(node)
	
    node = mkelement("advantages")
    node2 = mkelement("backgrounds")
    node3 = mkelement("background")
    node3.appendChild(mknode(dom,"background_name",sheet.background_1_name.GetValue()))
    node3.appendChild(mknode(dom,"background_level",sheet.background_1_level.value))
    node2.appendChild(node3)
    node3 = mkelement("background")
    node3.appendChild(mknode(dom,"background_name",sheet.background_2_name.GetValue()))
    node3.appendChild(mknode(dom,"background_level",sheet.background_2_level.value))
    node2.appendChild(node3)
    node3 = mkelement("background")
    node3.appendChild(mknode(dom,"background_name",sheet.background_3_name.GetValue()))
    node3.appendChild(mknode(dom,"background_level",sheet.background_3_level.value))
    node2.appendChild(node3)
    node3 = mkelement("background")
    node3.appendChild(mknode(dom,"background_name",sheet.background_4_name.GetValue()))
    node3.appendChild(mknode(dom,"background_level",sheet.background_4_level.value))
    node2.appendChild(node3)
    node3 = mkelement("background")
    node3.appendChild(mknode(dom,"background_name",sheet.background_5_name.GetValue()))
    node3.appendChild(mknode(dom,"background_level",sheet.background_5_level.value))
    node2.appendChild(node3)
    node3 = mkelement("background")
    node3.appendChild(mknode(dom,"background_name",sheet.background_6_name.GetValue()))
    node3.appendChild(mknode(dom,"background_level",sheet.background_6_level.value))
    node2.appendChild(node3)
    node3 = mkelement("background")
    node3.appendChild(mknode(dom,"background_name",sheet.background_7_name.GetValue()))
    node3.appendChild(mknode(dom,"background_level",sheet.background_7_level.value))
    node2.appendChild(node3)
    node.appendChild(node2)

    node2 = mkelement("disciplines")
    node3 = mkelement("discipline")
    node3.appendChild(mknode(dom,"discipline_name",sheet.discipline_1_name.GetValue()))
    node3.appendChild(mknode(dom,"discipline_level",sheet.discipline_1_level.value))
    node2.appendChild(node3)
    node3 = mkelement("discipline")
    node3.appendChild(mknode(dom,"discipline_name",sheet.discipline_2_name.GetValue()))
    node3.appendChild(mknode(dom,"discipline_level",sheet.discipline_2_level.value))
    node2.appendChild(node3)
    node3 = mkelement("discipline")
    node3.appendChild(mknode(dom,"discipline_name",sheet.discipline_3_name.GetValue()))
    node3.appendChild(mknode(dom,"discipline_level",sheet.discipline_3_level.value))
    node2.appendChild(node3)
    node3 = mkelement("discipline")
    node3.appendChild(mknode(dom,"discipline_name",sheet.discipline_4_name.GetValue()))
    node3.appendChild(mknode(dom,"discipline_level",sheet.discipline_4_level.value))
    node2.appendChild(node3)
    node3 = mkelement("discipline")
    node3.appendChild(mknode(dom,"discipline_name",sheet.discipline_5_name.GetValue()))
    node3.appendChild(mknode(dom,"discipline_level",sheet.discipline_5_level.value))
    node2.appendChild(node3)
    node3 = mkelement("discipline")
    node3.appendChild(mknode(dom,"discipline_name",sheet.discipline_6_name.GetValue()))
    node3.appendChild(mknode(dom,"discipline_level",sheet.discipline_6_level.value))
    node2.appendChild(node3)
    node3 = mkelement("discipline")
    node3.appendChild(mknode(dom,"discipline_name",sheet.discipline_7_name.GetValue()))
    node3.appendChild(mknode(dom,"discipline_level",sheet.discipline_7_level.value))
    node2.appendChild(node3)
    node.appendChild(node2)

    node2 = mkelement("virtues")
    node3 = mkelement("conscience_conviction")
    node3.appendChild(mknode(dom,"conscience_conviction_name",sheet.conscience_conviction_name.GetValue()))
    node3.appendChild(mknode(dom,"conscience_conviction_level",sheet.conscience_conviction_level.value))
    node2.appendChild(node3)
    node3 = mkelement("selfcontrol_instinct")
    node3.appendChild(mknode(dom,"selfcontrol_instinct_name",sheet.selfcontrol_instinct_name.GetValue()))
    node3.appendChild(mknode(dom,"selfcontrol_instinct_level",sheet.selfcontrol_instinct_level.value))
    node2.appendChild(node3)
    node3 = mkelement("courage")
    node3.appendChild(mknode(dom,"courage_name",sheet.courage_name.GetValue()))
    node3.appendChild(mknode(dom,"courage_level",sheet.courage_level.value))
    node2.appendChild(node3)
    node.appendChild(node2)
    root.appendChild(node)

    node = mkelement("merits_flaws")
    node2 = mkelement("merit")
    v = sheet.merit_1.GetSelection()
    dat = None
    if v == wx.NOT_FOUND or v == 0:
        txtdata = sheet.merit_1.GetValue()
    else:
        dat = sheet.merit_1.GetClientData(v)
	if dat:
	    txtdata = dat[0]
    node2.appendChild(mknode(dom,"merit_name",txtdata))
    if dat:
	node2.appendChild(mknode(dom,"merit_value",dat[1]))
    node.appendChild(node2)
    node2 = mkelement("merit")
    v = sheet.merit_2.GetSelection()
    dat = None
    if v == wx.NOT_FOUND or v == 0:
        txtdata = sheet.merit_2.GetValue()
    else:
        dat = sheet.merit_2.GetClientData(v)
	if dat:
	    txtdata = dat[0]
    node2.appendChild(mknode(dom,"merit_name",txtdata))
    if dat:
	node2.appendChild(mknode(dom,"merit_value",dat[1]))
    node.appendChild(node2)
    node2 = mkelement("merit")
    v = sheet.merit_3.GetSelection()
    dat = None
    if v == wx.NOT_FOUND or v == 0:
        txtdata = sheet.merit_3.GetValue()
    else:
        dat = sheet.merit_3.GetClientData(v)
	if dat:
	    txtdata = dat[0]
    node2.appendChild(mknode(dom,"merit_name",txtdata))
    if dat:
	node2.appendChild(mknode(dom,"merit_value",dat[1]))
    node.appendChild(node2)

	
    node2 = mkelement("flaw")
    v = sheet.flaw_1.GetSelection()
    dat = None
    if v == wx.NOT_FOUND or v == 0:
        txtdata = sheet.flaw_1.GetValue()
    else:
        dat = sheet.flaw_1.GetClientData(v)
	if dat:
	    txtdata = dat[0]
    node2.appendChild(mknode(dom,"flaw_name",txtdata))
    if dat:
	node2.appendChild(mknode(dom,"flaw_value",dat[1]))
    node.appendChild(node2)
    node2 = mkelement("flaw")
    v = sheet.flaw_2.GetSelection()
    dat = None
    if v == wx.NOT_FOUND or v == 0:
        txtdata = sheet.flaw_2.GetValue()
    else:
        dat = sheet.flaw_2.GetClientData(v)
	if dat:
	    txtdata = dat[0]
    node2.appendChild(mknode(dom,"flaw_name",txtdata))
    if dat:
	node2.appendChild(mknode(dom,"flaw_value",dat[1]))
    node.appendChild(node2)
    node2 = mkelement("flaw")
    v = sheet.flaw_3.GetSelection()
    dat = None
    if v == wx.NOT_FOUND or v == 0:
        txtdata = sheet.flaw_3.GetValue()
    else:
        dat = sheet.flaw_3.GetClientData(v)
	if dat:
	    txtdata = dat[0]
    node2.appendChild(mknode(dom,"flaw_name",txtdata))
    if dat:
	node2.appendChild(mknode(dom,"flaw_value",dat[1]))
    node.appendChild(node2)
    root.appendChild(node)

    node = mkelement("humanity_path")
    tmp = sheet.humanity_path_name.GetValue()
    if tmp.lower() == "humanity":
	node2 = mknode(dom,"humanity",sheet.humanity_path_level.value)
    else:
        node2 = mkelement("path")
	node2.appendChild(mknode(dom,"path_name",tmp))
	node2.appendChild(mknode(dom,"path_level",sheet.humanity_path_level.value))
    node.appendChild(node2)
    root.appendChild(node)

    node = mkelement("willpower")
    node.appendChild(mknode(dom,"willpower_max",sheet.willpower_max.value))
    node.appendChild(mknode(dom,"willpower_current",sheet.willpower_current.value))
    root.appendChild(node)

    root.appendChild(mknode(dom,"bloodpool",sheet.blood_pool.value))
    node = mkelement("health")
    node.appendChild(mknode(dom,"aggravated",sheet.health.aggravated))
    node.appendChild(mknode(dom,"normal",sheet.health.normal))
    root.appendChild(node)
    root.appendChild(mknode(dom,"experience",sheet.experience.GetValue()))

def xml2sheet(dom,sheet):
    gettxt = xmlutils.getnodetext
    sheet.name.SetValue(gettxt(dom.getElementsByTagName("name")[0]))
    sheet.player.SetValue(gettxt(dom.getElementsByTagName("player")[0]))
    sheet.chronicle.SetValue(gettxt(dom.getElementsByTagName("chronicle")[0]))
    sheet.nature.SetValue(gettxt(dom.getElementsByTagName("nature")[0]))
    sheet.demeanor.SetValue(gettxt(dom.getElementsByTagName("demeanor")[0]))
    sheet.clan.SetValue(gettxt(dom.getElementsByTagName("clan")[0]))
    sheet.generation.SetValue(int(gettxt(dom.getElementsByTagName("generation")[0])))
    sheet.haven.SetValue(gettxt(dom.getElementsByTagName("haven")[0]))
    sheet.concept.SetValue(gettxt(dom.getElementsByTagName("concept")[0]))

    attnode = dom.getElementsByTagName("attributes")[0]
    physnode = attnode.getElementsByTagName("physical")[0]
    sheet.strength.setvalue(int(gettxt(physnode.getElementsByTagName("strength")[0])))
    sheet.dexterity.setvalue(int(gettxt(physnode.getElementsByTagName("dexterity")[0])))
    sheet.stamina.setvalue(int(gettxt(physnode.getElementsByTagName("stamina")[0])))

    socnode = attnode.getElementsByTagName("social")[0]
    sheet.charisma.setvalue(int(gettxt(socnode.getElementsByTagName("charisma")[0])))
    sheet.manipulation.setvalue(int(gettxt(socnode.getElementsByTagName("manipulation")[0])))
    sheet.appearance.setvalue(int(gettxt(socnode.getElementsByTagName("appearance")[0])))
 
    mentnode = attnode.getElementsByTagName("mental")[0]
    sheet.perception.setvalue(int(gettxt(mentnode.getElementsByTagName("perception")[0])))
    sheet.intelligence.setvalue(int(gettxt(mentnode.getElementsByTagName("intelligence")[0])))
    sheet.wits.setvalue(int(gettxt(mentnode.getElementsByTagName("wits")[0])))
 
    abinode = dom.getElementsByTagName("abilities")[0]
    talnode = abinode.getElementsByTagName("talents")[0]
    sheet.alertness.setvalue(int(gettxt(talnode.getElementsByTagName("alertness")[0])))
    sheet.athletics.setvalue(int(gettxt(talnode.getElementsByTagName("athletics")[0])))
    sheet.brawl.setvalue(int(gettxt(talnode.getElementsByTagName("brawl")[0])))
    sheet.dodge.setvalue(int(gettxt(talnode.getElementsByTagName("dodge")[0])))
    sheet.empathy.setvalue(int(gettxt(talnode.getElementsByTagName("empathy")[0])))
    sheet.expression.setvalue(int(gettxt(talnode.getElementsByTagName("expression")[0])))
    sheet.intimidation.setvalue(int(gettxt(talnode.getElementsByTagName("intimidation")[0])))
    sheet.leadership.setvalue(int(gettxt(talnode.getElementsByTagName("leadership")[0])))
    sheet.streetwise.setvalue(int(gettxt(talnode.getElementsByTagName("streetwise")[0])))
    sheet.subterfuge.setvalue(int(gettxt(talnode.getElementsByTagName("subterfuge")[0])))
 
    skilnode = abinode.getElementsByTagName("skills")[0]
    sheet.animalken.setvalue(int(gettxt(skilnode.getElementsByTagName("animalken")[0])))
    sheet.crafts.setvalue(int(gettxt(skilnode.getElementsByTagName("crafts")[0])))
    sheet.drive.setvalue(int(gettxt(skilnode.getElementsByTagName("drive")[0])))
    sheet.etiquette.setvalue(int(gettxt(skilnode.getElementsByTagName("etiquette")[0])))
    sheet.firearms.setvalue(int(gettxt(skilnode.getElementsByTagName("firearms")[0])))
    sheet.melee.setvalue(int(gettxt(skilnode.getElementsByTagName("melee")[0])))
    sheet.performance.setvalue(int(gettxt(skilnode.getElementsByTagName("performance")[0])))
    sheet.security.setvalue(int(gettxt(skilnode.getElementsByTagName("security")[0])))
    sheet.stealth.setvalue(int(gettxt(skilnode.getElementsByTagName("stealth")[0])))
    sheet.survival.setvalue(int(gettxt(skilnode.getElementsByTagName("survival")[0])))
  
    knownode = abinode.getElementsByTagName("knowledges")[0]
    sheet.academics.setvalue(int(gettxt(knownode.getElementsByTagName("academics")[0])))
    sheet.computer.setvalue(int(gettxt(knownode.getElementsByTagName("computer")[0])))
    sheet.finance.setvalue(int(gettxt(knownode.getElementsByTagName("finance")[0])))
    sheet.investigation.setvalue(int(gettxt(knownode.getElementsByTagName("investigation")[0])))
    sheet.law.setvalue(int(gettxt(knownode.getElementsByTagName("investigation")[0])))
    sheet.linguistics.setvalue(int(gettxt(knownode.getElementsByTagName("linguistics")[0])))
    sheet.medicine.setvalue(int(gettxt(knownode.getElementsByTagName("medicine")[0])))
    sheet.occult.setvalue(int(gettxt(knownode.getElementsByTagName("occult")[0])))
    sheet.politics.setvalue(int(gettxt(knownode.getElementsByTagName("politics")[0])))
    sheet.science.setvalue(int(gettxt(knownode.getElementsByTagName("science")[0])))

    advnode = dom.getElementsByTagName("advantages")[0]
    bgn = advnode.getElementsByTagName("backgrounds")[0].getElementsByTagName("background")
    sheet.background_1_name.SetValue(gettxt(bgn[0].getElementsByTagName("background_name")[0]))
    sheet.background_1_level.setvalue(int(gettxt(bgn[0].getElementsByTagName("background_level")[0])))
    sheet.background_2_name.SetValue(gettxt(bgn[1].getElementsByTagName("background_name")[0]))
    sheet.background_2_level.setvalue(int(gettxt(bgn[1].getElementsByTagName("background_level")[0])))
    sheet.background_3_name.SetValue(gettxt(bgn[2].getElementsByTagName("background_name")[0]))
    sheet.background_3_level.setvalue(int(gettxt(bgn[2].getElementsByTagName("background_level")[0])))
    sheet.background_4_name.SetValue(gettxt(bgn[3].getElementsByTagName("background_name")[0]))
    sheet.background_4_level.setvalue(int(gettxt(bgn[3].getElementsByTagName("background_level")[0])))
    sheet.background_5_name.SetValue(gettxt(bgn[4].getElementsByTagName("background_name")[0]))
    sheet.background_5_level.setvalue(int(gettxt(bgn[4].getElementsByTagName("background_level")[0])))
    sheet.background_6_name.SetValue(gettxt(bgn[5].getElementsByTagName("background_name")[0]))
    sheet.background_6_level.setvalue(int(gettxt(bgn[5].getElementsByTagName("background_level")[0])))
    sheet.background_7_name.SetValue(gettxt(bgn[6].getElementsByTagName("background_name")[0]))
    sheet.background_7_level.setvalue(int(gettxt(bgn[6].getElementsByTagName("background_level")[0])))
	
    dpn = advnode.getElementsByTagName("disciplines")[0].getElementsByTagName("discipline")
    sheet.discipline_1_name.SetValue(gettxt(dpn[0].getElementsByTagName("discipline_name")[0]))
    sheet.discipline_1_level.setvalue(int(gettxt(dpn[0].getElementsByTagName("discipline_level")[0])))
    sheet.discipline_2_name.SetValue(gettxt(dpn[1].getElementsByTagName("discipline_name")[0]))
    sheet.discipline_2_level.setvalue(int(gettxt(dpn[1].getElementsByTagName("discipline_level")[0])))
    sheet.discipline_3_name.SetValue(gettxt(dpn[2].getElementsByTagName("discipline_name")[0]))
    sheet.discipline_3_level.setvalue(int(gettxt(dpn[2].getElementsByTagName("discipline_level")[0])))
    sheet.discipline_4_name.SetValue(gettxt(dpn[3].getElementsByTagName("discipline_name")[0]))
    sheet.discipline_4_level.setvalue(int(gettxt(dpn[3].getElementsByTagName("discipline_level")[0])))
    sheet.discipline_5_name.SetValue(gettxt(dpn[4].getElementsByTagName("discipline_name")[0]))
    sheet.discipline_5_level.setvalue(int(gettxt(dpn[4].getElementsByTagName("discipline_level")[0])))
    sheet.discipline_6_name.SetValue(gettxt(dpn[5].getElementsByTagName("discipline_name")[0]))
    sheet.discipline_6_level.setvalue(int(gettxt(dpn[5].getElementsByTagName("discipline_level")[0])))
    sheet.discipline_7_name.SetValue(gettxt(dpn[6].getElementsByTagName("discipline_name")[0]))
    sheet.discipline_7_level.setvalue(int(gettxt(dpn[6].getElementsByTagName("discipline_level")[0])))
  
    vnode = advnode.getElementsByTagName("virtues")[0]
    ccn = vnode.getElementsByTagName("conscience_conviction")[0]
    sheet.conscience_conviction_name.SetValue(gettxt(ccn.getElementsByTagName("conscience_conviction_name")[0]))
    sheet.conscience_conviction_level.setvalue(int(gettxt(ccn.getElementsByTagName("conscience_conviction_level")[0])))
    sin = vnode.getElementsByTagName("selfcontrol_instinct")[0]
    sheet.selfcontrol_instinct_name.SetValue(gettxt(sin.getElementsByTagName("selfcontrol_instinct_name")[0]))
    sheet.selfcontrol_instinct_level.setvalue(int(gettxt(sin.getElementsByTagName("selfcontrol_instinct_level")[0])))
    cn = vnode.getElementsByTagName("courage")[0]
    sheet.courage_name.SetValue(gettxt(cn.getElementsByTagName("courage_name")[0]))
    sheet.courage_level.setvalue(int(gettxt(cn.getElementsByTagName("courage_level")[0])))

    mfnode = dom.getElementsByTagName("merits_flaws")
    if mfnode:
        mtn = mfnode[0].getElementsByTagName("merit")
        if mtn[0]:
            mn = mtn[0].getElementsByTagName("merit_name")[0]
            mv = mtn[0].getElementsByTagName("merit_value")
	    if mv:
	        st = gettxt(mn) + " (" + gettxt(mv[0]) + "-pt. Merit)"
	        sheet.merit_1.SetStringSelection(st)
	    else:
	        sheet.merit_1.SetValue(gettxt(mn))
        if mtn[1]:
            mn = mtn[1].getElementsByTagName("merit_name")[0]
            mv = mtn[1].getElementsByTagName("merit_value")
	    if mv:
	        st = gettxt(mn) + " (" + gettxt(mv[0]) + "-pt. Merit)"
	        sheet.merit_2.SetStringSelection(st)
	    else:
	        sheet.merit_2.SetValue(gettxt(mn))
        if mtn[2]:
            mn = mtn[2].getElementsByTagName("merit_name")[0]
            mv = mtn[2].getElementsByTagName("merit_value")
	    if mv:
	        st = gettxt(mn) + " (" + gettxt(mv[0]) + "-pt. Merit)"
	        sheet.merit_3.SetStringSelection(st)
	    else:
	        sheet.merit_3.SetValue(gettxt(mn))
        fln = mfnode[0].getElementsByTagName("flaw")
        if fln[0]:
            fn = fln[0].getElementsByTagName("flaw_name")[0]
	    fv = fln[0].getElementsByTagName("flaw_value")
	    if fv:
	        st = gettxt(fn) + " (" + gettxt(fv[0]) + "-pt. Flaw)"
	        sheet.flaw_1.SetStringSelection(st)
            else:
	        sheet.flaw_1.SetValue(gettxt(fn))
        if fln[1]:
            fn = fln[1].getElementsByTagName("flaw_name")[0]
	    fv = fln[1].getElementsByTagName("flaw_value")
	    if fv:
	        st = gettxt(fn) + " (" + gettxt(fv[0]) + "-pt. Flaw)"
	        sheet.flaw_2.SetStringSelection(st)
            else:
	        sheet.flaw_2.SetValue(gettxt(fn))
        if fln[2]:
            fn = fln[2].getElementsByTagName("flaw_name")[0]
	    fv = fln[2].getElementsByTagName("flaw_value")
	    if fv:
	        st = gettxt(fn) + " (" + gettxt(fv[0]) + "-pt. Flaw)"
	        sheet.flaw_3.SetStringSelection(st)
            else:
	        sheet.flaw_3.SetValue(gettxt(fn))

    
    hpnode = dom.getElementsByTagName("humanity_path")[0]
    hn = hpnode.getElementsByTagName("humanity")
    if hn:
        sheet.humanity_path_name.SetValue("Humanity")
	sheet.humanity_path_level.setvalue(int(gettxt(hn[0])))
    else:
        pn = hpnode.getElementsByTagName("path")[0]
	sheet.humanity_path_name.SetValue(gettxt(pn.getElementsByTagName("path_name")[0]))
	sheet.humanity_path_level.setvalue(int(gettxt(pn.getElementsByTagName("path_level")[0])))
	
    wn = dom.getElementsByTagName("willpower")[0]
    sheet.willpower_max.setvalue(int(gettxt(wn.getElementsByTagName("willpower_max")[0])))
    sheet.willpower_current.setvalue(int(gettxt(wn.getElementsByTagName("willpower_current")[0])))
    sheet.blood_pool.setvalue(int(gettxt(dom.getElementsByTagName("bloodpool")[0])))

    heln = dom.getElementsByTagName("health")[0]
    n = heln.getElementsByTagName("aggravated")
    if n:
        sheet.health.setaggravated(int(gettxt(n[0])))
    n = heln.getElementsByTagName("normal")
    if n:
        sheet.health.setnormal(int(gettxt(n[0])))

    sheet.experience.SetValue(int(gettxt(dom.getElementsByTagName("experience")[0])))

def dtd():
    return u"""\
  <!ELEMENT soulforge_character (name, player, chronicle, nature, demeanor, clan, generation, haven, concept, attributes, abilities, advantages, merits_flaws, humanity_path, willpower, bloodpool, health, experience)>
  <!ATTLIST soulforge_character
        universe	CDATA	#REQUIRED
  >
  <!ELEMENT name (#PCDATA)>
  <!ELEMENT player (#PCDATA)>
  <!ELEMENT chronicle (#PCDATA)>
  <!ELEMENT nature (#PCDATA)>
  <!ELEMENT demeanor (#PCDATA)>
  <!ELEMENT clan (#PCDATA)>
  <!ELEMENT generation (#PCDATA)>
  <!ELEMENT haven (#PCDATA)>
  <!ELEMENT concept (#PCDATA)>
  <!ELEMENT attributes (physical, social, mental)>
  <!ELEMENT physical (strength, dexterity, stamina)>
  <!ELEMENT strength (#PCDATA)>
  <!ELEMENT dexterity (#PCDATA)>
  <!ELEMENT stamina (#PCDATA)>
  <!ELEMENT social (charisma, manipulation, appearance)>
  <!ELEMENT charisma (#PCDATA)>
  <!ELEMENT manipulation (#PCDATA)>
  <!ELEMENT appearance (#PCDATA)>
  <!ELEMENT mental (perception, intelligence, wits)>
  <!ELEMENT perception (#PCDATA)>
  <!ELEMENT intelligence (#PCDATA)>
  <!ELEMENT wits (#PCDATA)>
  <!ELEMENT abilities (talents, skills, knowledges)>
  <!ELEMENT talents (alertness, athletics, brawl, dodge, empathy, expression, intimidation, leadership, streetwise, subterfuge)>
  <!ELEMENT alertness (#PCDATA)>
  <!ELEMENT athletics (#PCDATA)>
  <!ELEMENT brawl (#PCDATA)>
  <!ELEMENT dodge (#PCDATA)>
  <!ELEMENT empathy (#PCDATA)>
  <!ELEMENT expression (#PCDATA)>
  <!ELEMENT intimidation (#PCDATA)>
  <!ELEMENT leadership (#PCDATA)>
  <!ELEMENT streetwise (#PCDATA)>
  <!ELEMENT subterfuge (#PCDATA)>
  <!ELEMENT skills (animalken, crafts, drive, etiquette, firearms, melee, performance, security, stealth, survival)>
  <!ELEMENT animalken (#PCDATA)>
  <!ELEMENT crafts (#PCDATA)>
  <!ELEMENT drive (#PCDATA)>
  <!ELEMENT etiquette (#PCDATA)>
  <!ELEMENT firearms (#PCDATA)>
  <!ELEMENT melee (#PCDATA)>
  <!ELEMENT performance (#PCDATA)>
  <!ELEMENT security (#PCDATA)>
  <!ELEMENT stealth (#PCDATA)>
  <!ELEMENT survival (#PCDATA)>
  <!ELEMENT knowledges (academics, computer, finance, investigation, law, linguistics, medicine, occult, politics, science)>
  <!ELEMENT academics (#PCDATA)>
  <!ELEMENT computer (#PCDATA)>
  <!ELEMENT finance (#PCDATA)>
  <!ELEMENT investigation (#PCDATA)>
  <!ELEMENT law (#PCDATA)>
  <!ELEMENT linguistics (#PCDATA)>
  <!ELEMENT medicine (#PCDATA)>
  <!ELEMENT occult (#PCDATA)>
  <!ELEMENT politics (#PCDATA)>
  <!ELEMENT science (#PCDATA)>
  <!ELEMENT advantages (backgrounds, disciplines, virtues)>
  <!ELEMENT backgrounds (background*)>
  <!ELEMENT background (background_name, background_level)>
  <!ELEMENT background_name (#PCDATA)>
  <!ELEMENT background_level (#PCDATA)>
  <!ELEMENT disciplines (discipline*)>
  <!ELEMENT discipline (discipline_name, discipline_level)>
  <!ELEMENT discipline_name (#PCDATA)>
  <!ELEMENT discipline_level (#PCDATA)>
  <!ELEMENT virtues (conscience_conviction, selfcontrol_instinct, courage)>
  <!ELEMENT conscience_conviction (conscience_conviction_name, conscience_conviction_level)>
  <!ELEMENT conscience_conviction_name (#PCDATA)>
  <!ELEMENT conscience_conviction_level (#PCDATA)>
  <!ELEMENT selfcontrol_instinct (selfcontrol_instinct_name, selfcontrol_instinct_level)>
  <!ELEMENT selfcontrol_instinct_name (#PCDATA)>
  <!ELEMENT selfcontrol_instinct_level (#PCDATA)>
  <!ELEMENT courage (courage_name, courage_level)>
  <!ELEMENT courage_name (#PCDATA)>
  <!ELEMENT courage_level (#PCDATA)>
  <!ELEMENT merits_flaws (merit*, flaw*)>
  <!ELEMENT merit (merit_name, merit_value?)>
  <!ELEMENT merit_name (#PCDATA)>
  <!ELEMENT merit_value (#PCDATA)>
  <!ELEMENT flaw (flaw_name, flaw_value?)>
  <!ELEMENT flaw_name (#PCDATA)>
  <!ELEMENT flaw_value (#PCDATA)>
  <!ELEMENT humanity_path (humanity | path+)>
  <!ELEMENT humanity (#PCDATA)>
  <!ELEMENT path (path_name, path_level)>
  <!ELEMENT path_name (#PCDATA)>
  <!ELEMENT path_level (#PCDATA)>
  <!ELEMENT willpower (willpower_max, willpower_current)>
  <!ELEMENT willpower_max (#PCDATA)>
  <!ELEMENT willpower_current (#PCDATA)>
  <!ELEMENT bloodpool (#PCDATA)>
  <!ELEMENT health (aggravated, normal)>
  <!ELEMENT aggravated (#PCDATA)>
  <!ELEMENT normal (#PCDATA)>
  <!ELEMENT experience (#PCDATA)>
"""
