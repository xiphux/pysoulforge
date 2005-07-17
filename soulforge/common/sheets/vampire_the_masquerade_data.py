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

from xml.dom import minidom
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
	'Acute Sense': (1,),
	'Ambidextrous': (1,),
	'Eat Food': (1,),
	'Catlike Balance': (1,),
	'Blush of Health': (2,),
	'Enchanting Voice': (2,),
	'Daredevil': (3,),
	'Efficient Digestion': (3,),
	'Huge Size': (4,),
	'Common Sense': (1,),
	'Concentration': (1,),
	'Time Sense': (1,),
	'Code of Honor': (2,),
	'Eidetic Memory': (2,),
	'Light Sleeper': (2,),
	'Natural Linguist': (2,),
	'Calm Heart': (3,),
	'Iron Will': (3,),
	'Prestigious Sire': (1,),
	'Natural Leader': (1,),
	'Debt of Gratitude': (1,2,3,),
	'Medium': (2,),
	'Magic Resistance': (2,),
	'Oracular Ability': (3,),
	'Spirit Mentor': (3,),
	'Unbondable': (3,),
	'Lucky': (3,),
	'True Love': (4,),
	'Nine Lives': (6,),
	'True Faith': (7,),
}

flaws = {
	'Smell of the Grave': (1,),
	'Short': (1,),
	'Hard of Hearing': (1,),
	'14th Generation': (2,),
	'Infectious Bite': (2,),
	'Bad Sight': (1, 3,),
	'One Eye': (2,),
	'Disfigured': (2,),
	'Child': (3,),
	'Deformity': (3,),
	'Lame': (3,),
	'Monstrous': (3,),
	'Permanent Wound': (3,),
	'Slow Healing': (3,),
	'Addiction': (3,),
	'Mute': (4,),
	'Thin Blood': (4,),
	'Disease Carrier': (4,),
	'Deaf': (4,),
	'Flesh of the Corpse': (5,),
	'Blind': (6,),
	'Deep Sleeper': (1,),
	'Nightmares': (1,),
	'Phobia': (2,),
	'Prey Exclusion': (1,),
	'Shy': (1,),
	'Soft-Hearted': (1,),
	'Speech Impediment': (1,),
	'Short Fuse': (2,),
	'Territorial': (2,),
	'Vengeful': (2,),
	'Amnesia': (2,),
	'Lunacy': (2,),
	'Weak-Willed': (3,),
	'Conspicuous Consumption': (4,),
	'Dark Secret': (1,),
	'Infamous Sire': (1,),
	'Mistaken Identity': (1,),
	'Sire\'s Resentment': (1,),
	'Enemy': (1,2,3,4,5,),
	'Hunted': (4,),
	'Probationary Sect Member': (4,),
	'Touch of Frost': (1,),
	'Repulsed by Garlic': (1,),
	'Cursed': (1,2,3,4,5,),
	'Cast No Reflection': (1,),
	'Eerie Presence': (2,),
	'Repelled by Crosses': (3,),
	'Can\'t Cross Running Water': (3,),
	'Haunted': (3,),
	'Grip of the Damned': (4,),
	'Dark Fate': (5,),
	'Light-Sensitive': (5,),
}

def sheet2xml(sheet,dom):
    root = dom.documentElement
    root.setAttribute("universe",universe)

    mkelement = dom.createElement
    mktext = dom.createTextNode

    node = mkelement("name")
    node2 = mktext(sheet.name.GetValue())
    node.appendChild(node2)
    root.appendChild(node)
	
    node = mkelement("player")
    node2 = mktext(sheet.player.GetValue())
    node.appendChild(node2)
    root.appendChild(node)

    node = mkelement("chronicle")
    node2 = mktext(sheet.chronicle.GetValue())
    node.appendChild(node2)
    root.appendChild(node)
	
    node = mkelement("nature")
    node2 = mktext(sheet.nature.GetValue())
    node.appendChild(node2)
    root.appendChild(node)
	
    node = mkelement("demeanor")
    node2 = mktext(sheet.demeanor.GetValue())
    node.appendChild(node2)
    root.appendChild(node)
  
    node = mkelement("clan")
    node2 = mktext(sheet.clan.GetValue())
    node.appendChild(node2)
    root.appendChild(node)
    
    node = mkelement("generation")
    node2 = mktext(str(sheet.generation.GetValue()))
    node.appendChild(node2)
    root.appendChild(node)

    node = mkelement("haven")
    node2 = mktext(sheet.haven.GetValue())
    node.appendChild(node2)
    root.appendChild(node)

    node = mkelement("concept")
    node2 = mktext(sheet.concept.GetValue())
    node.appendChild(node2)
    root.appendChild(node)
	
    node = mkelement("attributes")

    node2 = mkelement("physical")

    node3 = mkelement("strength")
    node4 = mktext(str(sheet.strength.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("dexterity")
    node4 = mktext(str(sheet.dexterity.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("stamina")
    node4 = mktext(str(sheet.stamina.value))
    node3.appendChild(node4)
    node2.appendChild(node3)

    node.appendChild(node2)

    node2 = mkelement("social")

    node3 = mkelement("charisma")
    node4 = mktext(str(sheet.charisma.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("manipulation")
    node4 = mktext(str(sheet.manipulation.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("appearance")
    node4 = mktext(str(sheet.appearance.value))
    node3.appendChild(node4)
    node2.appendChild(node3)

    node.appendChild(node2)

    node2 = mkelement("mental")
	
    node3 = mkelement("perception")
    node4 = mktext(str(sheet.perception.value))
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("intelligence")
    node4 = mktext(str(sheet.intelligence.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
 
    node3 = mkelement("wits")
    node4 = mktext(str(sheet.wits.value))
    node3.appendChild(node4)
    node2.appendChild(node3)

    node.appendChild(node2)
 
    root.appendChild(node)

    node = mkelement("abilities")
	
    node2 = mkelement("talents")

    node3 = mkelement("alertness")
    node4 = mktext(str(sheet.alertness.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("athletics")
    node4 = mktext(str(sheet.athletics.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
 
    node3 = mkelement("brawl")
    node4 = mktext(str(sheet.brawl.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
 
    node3 = mkelement("dodge")
    node4 = mktext(str(sheet.dodge.value))
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("empathy")
    node4 = mktext(str(sheet.empathy.value))
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("expression")
    node4 = mktext(str(sheet.expression.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("intimidation")
    node4 = mktext(str(sheet.intimidation.value))
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("leadership")
    node4 = mktext(str(sheet.leadership.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("streetwise")
    node4 = mktext(str(sheet.streetwise.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("subterfuge")
    node4 = mktext(str(sheet.subterfuge.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node.appendChild(node2)
 
    node2 = mkelement("skills")

    node3 = mkelement("animalken")
    node4 = mktext(str(sheet.animalken.value))
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("crafts")
    node4 = mktext(str(sheet.crafts.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("drive")
    node4 = mktext(str(sheet.drive.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("etiquette")
    node4 = mktext(str(sheet.etiquette.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("firearms")
    node4 = mktext(str(sheet.firearms.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("melee")
    node4 = mktext(str(sheet.melee.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("performance")
    node4 = mktext(str(sheet.performance.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("security")
    node4 = mktext(str(sheet.security.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("stealth")
    node4 = mktext(str(sheet.stealth.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
 
    node3 = mkelement("survival")
    node4 = mktext(str(sheet.survival.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node.appendChild(node2)
 
    node2 = mkelement("knowledges")

    node3 = mkelement("academics")
    node4 = mktext(str(sheet.academics.value))
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("computer")
    node4 = mktext(str(sheet.computer.value))
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("finance")
    node4 = mktext(str(sheet.finance.value))
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("investigation")
    node4 = mktext(str(sheet.investigation.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
 
    node3 = mkelement("law")
    node4 = mktext(str(sheet.law.value))
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("linguistics")
    node4 = mktext(str(sheet.linguistics.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("medicine")
    node4 = mktext(str(sheet.medicine.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("occult")
    node4 = mktext(str(sheet.occult.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("politics")
    node4 = mktext(str(sheet.politics.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node3 = mkelement("science")
    node4 = mktext(str(sheet.science.value))
    node3.appendChild(node4)
    node2.appendChild(node3)
	
    node.appendChild(node2)

    root.appendChild(node)
	
    node = mkelement("advantages")

    node2 = mkelement("backgrounds")

    node3 = mkelement("background")
    node4 = mkelement("background_name")
    node5 = mktext(sheet.background_1_name.GetValue())
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("background_level")
    node5 = mktext(str(sheet.background_1_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("background")
    node4 = mkelement("background_name")
    node5 = mktext(sheet.background_2_name.GetValue())
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("background_level")
    node5 = mktext(str(sheet.background_2_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("background")
    node4 = mkelement("background_name")
    node5 = mktext(sheet.background_3_name.GetValue())
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("background_level")
    node5 = mktext(str(sheet.background_3_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("background")
    node4 = mkelement("background_name")
    node5 = mktext(sheet.background_4_name.GetValue())
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("background_level")
    node5 = mktext(str(sheet.background_4_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("background")
    node4 = mkelement("background_name")
    node5 = mktext(sheet.background_5_name.GetValue())
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("background_level")
    node5 = mktext(str(sheet.background_5_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)
 
    node3 = mkelement("background")
    node4 = mkelement("background_name")
    node5 = mktext(sheet.background_6_name.GetValue())
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("background_level")
    node5 = mktext(str(sheet.background_6_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("background")
    node4 = mkelement("background_name")
    node5 = mktext(sheet.background_7_name.GetValue())
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("background_level")
    node5 = mktext(str(sheet.background_7_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)

    node.appendChild(node2)

    node2 = mkelement("disciplines")

    node3 = mkelement("discipline")
    node4 = mkelement("discipline_name")
    node5 = mktext(sheet.discipline_1_name.GetValue())
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("discipline_level")
    node5 = mktext(str(sheet.discipline_1_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("discipline")
    node4 = mkelement("discipline_name")
    node5 = mktext(sheet.discipline_2_name.GetValue())
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("discipline_level")
    node5 = mktext(str(sheet.discipline_2_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("discipline")
    node4 = mkelement("discipline_name")
    node5 = mktext(sheet.discipline_3_name.GetValue())
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("discipline_level")
    node5 = mktext(str(sheet.discipline_3_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("discipline")
    node4 = mkelement("discipline_name")
    node5 = mktext(sheet.discipline_4_name.GetValue())
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("discipline_level")
    node5 = mktext(str(sheet.discipline_4_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)
 
    node3 = mkelement("discipline")
    node4 = mkelement("discipline_name")
    node5 = mktext(sheet.discipline_5_name.GetValue())
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("discipline_level")
    node5 = mktext(str(sheet.discipline_5_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)
 
    node3 = mkelement("discipline")
    node4 = mkelement("discipline_name")
    node5 = mktext(sheet.discipline_6_name.GetValue())
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("discipline_level")
    node5 = mktext(str(sheet.discipline_6_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)

    node3 = mkelement("discipline")
    node4 = mkelement("discipline_name")
    node5 = mktext(sheet.discipline_7_name.GetValue())
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("discipline_level")
    node5 = mktext(str(sheet.discipline_7_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)

    node.appendChild(node2)

    node2 = mkelement("virtues")
	
    node3 = mkelement("conscience_conviction")
    node4 = mkelement("conscience_conviction_name")
    node5 = mktext(str(sheet.conscience_conviction_name.GetValue()))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("conscience_conviction_level")
    node5 = mktext(str(sheet.conscience_conviction_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)
   
    node3 = mkelement("selfcontrol_instinct")
    node4 = mkelement("selfcontrol_instinct_name")
    node5 = mktext(str(sheet.selfcontrol_instinct_name.GetValue()))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("selfcontrol_instinct_level")
    node5 = mktext(str(sheet.selfcontrol_instinct_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)
   
    node3 = mkelement("courage")
    node4 = mkelement("courage_name")
    node5 = mktext(str(sheet.courage_name.GetValue()))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node4 = mkelement("courage_level")
    node5 = mktext(str(sheet.courage_level.value))
    node4.appendChild(node5)
    node3.appendChild(node4)
    node2.appendChild(node3)

    node.appendChild(node2)

    root.appendChild(node)

    node = mkelement("merits_flaws")

    node2 = mkelement("merit")
    node3 = mkelement("merit_name")
    v = sheet.merit_1.GetSelection()
    dat = None
    if v == wx.NOT_FOUND or v == 0:
        node4 = mktext(sheet.merit_1.GetValue())
    else:
        dat = sheet.merit_1.GetClientData(v)
	if dat:
	    node4 = mktext(dat[0])
    node3.appendChild(node4)
    node2.appendChild(node3)
    if dat:
        node3 = mkelement("merit_value")
	node4 = mktext(str(dat[1]))
	node3.appendChild(node4)
	node2.appendChild(node3)
    node.appendChild(node2)
    node2 = mkelement("merit")
    node3 = mkelement("merit_name")
    v = sheet.merit_2.GetSelection()
    dat = None
    if v == wx.NOT_FOUND or v == 0:
        node4 = mktext(sheet.merit_2.GetValue())
    else:
        dat = sheet.merit_2.GetClientData(v)
	if dat:
	    node4 = mktext(dat[0])
    node3.appendChild(node4)
    node2.appendChild(node3)
    if dat:
        node3 = mkelement("merit_value")
	node4 = mktext(str(dat[1]))
	node3.appendChild(node4)
	node2.appendChild(node3)
    node.appendChild(node2)
    node2 = mkelement("merit")
    node3 = mkelement("merit_name")
    v = sheet.merit_3.GetSelection()
    dat = None
    if v == wx.NOT_FOUND or v == 0:
        node4 = mktext(sheet.merit_3.GetValue())
    else:
        dat = sheet.merit_3.GetClientData(v)
	if dat:
	    node4 = mktext(dat[0])
    node3.appendChild(node4)
    node2.appendChild(node3)
    if dat:
        node3 = mkelement("merit_value")
	node4 = mktext(str(dat[1]))
	node3.appendChild(node4)
	node2.appendChild(node3)
    node.appendChild(node2)
	
    node2 = mkelement("flaw")
    node3 = mkelement("flaw_name")
    v = sheet.flaw_1.GetSelection()
    dat = None
    if v == wx.NOT_FOUND or v == 0:
        node4 = mktext(sheet.flaw_1.GetValue())
    else:
        dat = sheet.flaw_1.GetClientData(v)
	if dat:
	    node4 = mktext(dat[0])
    node3.appendChild(node4)
    node2.appendChild(node3)
    if dat:
        node3 = mkelement("flaw_value")
	node4 = mktext(str(dat[1]))
	node3.appendChild(node4)
	node2.appendChild(node3)
    node.appendChild(node2)
    node2 = mkelement("flaw")
    node3 = mkelement("flaw_name")
    v = sheet.flaw_2.GetSelection()
    dat = None
    if v == wx.NOT_FOUND or v == 0:
        node4 = mktext(sheet.flaw_2.GetValue())
    else:
        dat = sheet.flaw_2.GetClientData(v)
	if dat:
	    node4 = mktext(dat[0])
    node3.appendChild(node4)
    node2.appendChild(node3)
    if dat:
        node3 = mkelement("flaw_value")
	node4 = mktext(str(dat[1]))
	node3.appendChild(node4)
	node2.appendChild(node3)
    node.appendChild(node2)
    node2 = mkelement("flaw")
    node3 = mkelement("flaw_name")
    v = sheet.flaw_3.GetSelection()
    dat = None
    if v == wx.NOT_FOUND or v == 0:
        node4 = mktext(sheet.flaw_3.GetValue())
    else:
        dat = sheet.flaw_3.GetClientData(v)
	if dat:
	    node4 = mktext(dat[0])
    node3.appendChild(node4)
    node2.appendChild(node3)
    if dat:
        node3 = mkelement("flaw_value")
	node4 = mktext(str(dat[1]))
	node3.appendChild(node4)
	node2.appendChild(node3)
    node.appendChild(node2)
    
    root.appendChild(node)

    node = mkelement("humanity_path")
    tmp = sheet.humanity_path_name.GetValue()
    if tmp.lower() == "humanity":
        node2 = mkelement("humanity")
	node3 = mktext(str(sheet.humanity_path_level.value))
	node2.appendChild(node3)
    else:
        node2 = mkelement("path")
	node3 = mkelement("path_name")
	node4 = mktext(tmp)
	node3.appendChild(node4)
	node2.appendChild(node3)
	node3 = mkelement("path_level")
	node4 = mktext(str(sheet.humanity_path_level.value))
	node3.appendChild(node4)
	node2.appendChild(node3)

    node.appendChild(node2)

    root.appendChild(node)

    node = mkelement("willpower")
    node2 = mkelement("willpower_max")
    node3 = mktext(str(sheet.willpower_max.value))
    node2.appendChild(node3)
    node.appendChild(node2)
    node2 = mkelement("willpower_current")
    node3 = mktext(str(sheet.willpower_current.value))
    node2.appendChild(node3)
    node.appendChild(node2)
    root.appendChild(node)

    node = mkelement("bloodpool")
    node2 = mktext(str(sheet.blood_pool.value))
    node.appendChild(node2)
    root.appendChild(node)

    node = mkelement("health")
    node2 = mkelement("aggravated")
    node3 = mktext(str(sheet.health.aggravated))
    node2.appendChild(node3)
    node.appendChild(node2)
    node2 = mkelement("normal")
    node3 = mktext(str(sheet.health.normal))
    node2.appendChild(node3)
    node.appendChild(node2)
    root.appendChild(node)
 
    node = mkelement("experience")
    node2 = mktext(str(sheet.experience.GetValue()))
    node.appendChild(node2)
    root.appendChild(node)

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
