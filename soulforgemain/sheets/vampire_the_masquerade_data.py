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

import parser
from xml.dom import minidom

archetypes = ['','Architect','Autocrat','Bon Vivant','Bravo','Caregiver','Celebrant','Child','Competitor','Conformist','Conniver','Curmudgeon','Deviant','Director','Fanatic','Gallant','Judge','Loner','Martyr','Masochist','Monster','Pedagogue','Penitent','Perfectionist','Rebel','Rogue','Survivor','Thrill-Seeker','Traditionalist','Trickster','Visionary']

clans = ['','Brujah','Gangrel','Malkavian','Nosferatu','Toreador','Tremere','Ventrue','Lasombra','Tzimisce','Assamite','Followers of Set','Giovanni','Ravnos']

backgrounds = ['','Allies','Contacts','Fame','Generation','Herd','Influence','Mentor','Resources','Retainers','Status']

disciplines = ['','Animalism','Auspex','Celerity','Chimerstry','Dementation','Dominate','Fortitude','Necromancy','Obfuscate','Obtenebration','Potence','Presence','Protean','Quietus','Serpentis','Thaumaturgy','Vicissitude']

conscience_conviction = ['','Conscience','Conviction']

selfcontrol_instinct = ['','Self-Control','Instinct']

courage = ['','Courage']

humanity_path = ['','Humanity','Path of Blood','Path of Bones','Path of Night','Path of Metamorphosis','Path of Paradox','Path of Typhon']

class vampire_the_masquerade_parser(parser.sheetparser):
    def __init__(self):
        pass
	
    def sheet2xml(self,sheet,dom):
        root = dom.documentElement
	root.setAttribute("universe","vampire_the_masquerade")

	node = dom.createElement("name")
	node2 = dom.createTextNode(sheet.name.GetValue())
	node.appendChild(node2)
	root.appendChild(node)
	
	node = dom.createElement("player")
	node2 = dom.createTextNode(sheet.player.GetValue())
	node.appendChild(node2)
	root.appendChild(node)
	
	node = dom.createElement("nature")
	node2 = dom.createTextNode(sheet.nature.GetValue())
	node.appendChild(node2)
	root.appendChild(node)
	
	node = dom.createElement("demeanor")
	node2 = dom.createTextNode(sheet.demeanor.GetValue())
	node.appendChild(node2)
	root.appendChild(node)
	
	node = dom.createElement("clan")
	node2 = dom.createTextNode(sheet.clan.GetValue())
	node.appendChild(node2)
	root.appendChild(node)

	node = dom.createElement("generation")
	node2 = dom.createTextNode(str(sheet.generation.GetValue()))
	node.appendChild(node2)
	root.appendChild(node)
	
	node = dom.createElement("attributes")
	
	node2 = dom.createElement("physical")
	
	node3 = dom.createElement("strength")
	node4 = dom.createTextNode(str(sheet.strength.value))
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("dexterity")
	node4 = dom.createTextNode(str(sheet.dexterity.value))
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("stamina")
	node4 = dom.createTextNode(str(sheet.stamina.value))
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node.appendChild(node2)
	
	node2 = dom.createElement("social")
	
	node3 = dom.createElement("charisma")
	node4 = dom.createTextNode(str(sheet.charisma.value))
        node3.appendChild(node4)
	node2.appendChild(node3)
	
        node3 = dom.createElement("manipulation")
	node4 = dom.createTextNode(str(sheet.manipulation.value))
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("appearance")
	node4 = dom.createTextNode(str(sheet.appearance.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node.appendChild(node2)
	
	node2 = dom.createElement("mental")
	
	node3 = dom.createElement("perception")
	node4 = dom.createTextNode(str(sheet.perception.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("intelligence")
	node4 = dom.createTextNode(str(sheet.intelligence.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("wits")
	node4 = dom.createTextNode(str(sheet.wits.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node.appendChild(node2)
	
	root.appendChild(node)
	
	node = dom.createElement("abilities")
	
	node2 = dom.createElement("talents")
	
	node3 = dom.createElement("alertness")
	node4 = dom.createTextNode(str(sheet.alertness.value))
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("athletics")
	node4 = dom.createTextNode(str(sheet.athletics.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("brawl")
	node4 = dom.createTextNode(str(sheet.brawl.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("dodge")
	node4 = dom.createTextNode(str(sheet.dodge.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("empathy")
	node4 = dom.createTextNode(str(sheet.empathy.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("expression")
	node4 = dom.createTextNode(str(sheet.expression.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("intimidation")
	node4 = dom.createTextNode(str(sheet.intimidation.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("leadership")
	node4 = dom.createTextNode(str(sheet.leadership.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("streetwise")
	node4 = dom.createTextNode(str(sheet.streetwise.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("subterfuge")
	node4 = dom.createTextNode(str(sheet.subterfuge.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node.appendChild(node2)
	
	node2 = dom.createElement("skills")
	
	node3 = dom.createElement("animalken")
	node4 = dom.createTextNode(str(sheet.animalken.value))
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("crafts")
	node4 = dom.createTextNode(str(sheet.crafts.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("drive")
	node4 = dom.createTextNode(str(sheet.drive.value))
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("etiquette")
	node4 = dom.createTextNode(str(sheet.etiquette.value))
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("firearms")
	node4 = dom.createTextNode(str(sheet.firearms.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("melee")
	node4 = dom.createTextNode(str(sheet.melee.value))
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("performance")
	node4 = dom.createTextNode(str(sheet.performance.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("security")
	node4 = dom.createTextNode(str(sheet.security.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("stealth")
	node4 = dom.createTextNode(str(sheet.stealth.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("survival")
	node4 = dom.createTextNode(str(sheet.survival.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node.appendChild(node2)
	
	node2 = dom.createElement("knowledges")
	
	node3 = dom.createElement("academics")
	node4 = dom.createTextNode(str(sheet.academics.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("computer")
	node4 = dom.createTextNode(str(sheet.computer.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("finance")
	node4 = dom.createTextNode(str(sheet.finance.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("investigation")
	node4 = dom.createTextNode(str(sheet.investigation.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("law")
	node4 = dom.createTextNode(str(sheet.law.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("linguistics")
	node4 = dom.createTextNode(str(sheet.linguistics.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("medicine")
	node4 = dom.createTextNode(str(sheet.medicine.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("occult")
	node4 = dom.createTextNode(str(sheet.occult.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("politics")
	node4 = dom.createTextNode(str(sheet.politics.value))
	node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("science")
	node4 = dom.createTextNode(str(sheet.science.value))
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node.appendChild(node2)
	
	root.appendChild(node)
	
	node = dom.createElement("advantages")
	
	node2 = dom.createElement("backgrounds")
	
	node3 = dom.createElement("background")
	node4 = dom.createElement("background_name")
	node5 = dom.createTextNode(sheet.background_1_name.GetValue())
	node4.appendChild(node5)
        node3.appendChild(node4)
	node4 = dom.createElement("background_level")
	node5 = dom.createTextNode(str(sheet.background_1_level.value))
	node4.appendChild(node5)
        node3.appendChild(node4)
	node2.appendChild(node3)

	node3 = dom.createElement("background")
	node4 = dom.createElement("background_name")
	node5 = dom.createTextNode(sheet.background_2_name.GetValue())
	node4.appendChild(node5)
        node3.appendChild(node4)
	node4 = dom.createElement("background_level")
	node5 = dom.createTextNode(str(sheet.background_2_level.value))
	node4.appendChild(node5)
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("background")
	node4 = dom.createElement("background_name")
	node5 = dom.createTextNode(sheet.background_3_name.GetValue())
	node4.appendChild(node5)
        node3.appendChild(node4)
	node4 = dom.createElement("background_level")
	node5 = dom.createTextNode(str(sheet.background_3_level.value))
	node4.appendChild(node5)
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("background")
	node4 = dom.createElement("background_name")
	node5 = dom.createTextNode(sheet.background_4_name.GetValue())
	node4.appendChild(node5)
        node3.appendChild(node4)
	node4 = dom.createElement("background_level")
	node5 = dom.createTextNode(str(sheet.background_4_level.value))
	node4.appendChild(node5)
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("background")
	node4 = dom.createElement("background_name")
	node5 = dom.createTextNode(sheet.background_5_name.GetValue())
	node4.appendChild(node5)
        node3.appendChild(node4)
	node4 = dom.createElement("background_level")
	node5 = dom.createTextNode(str(sheet.background_5_level.value))
	node4.appendChild(node5)
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("background")
	node4 = dom.createElement("background_name")
	node5 = dom.createTextNode(sheet.background_6_name.GetValue())
	node4.appendChild(node5)
        node3.appendChild(node4)
	node4 = dom.createElement("background_level")
	node5 = dom.createTextNode(str(sheet.background_6_level.value))
	node4.appendChild(node5)
        node3.appendChild(node4)
	node2.appendChild(node3)

	node3 = dom.createElement("background")
	node4 = dom.createElement("background_name")
	node5 = dom.createTextNode(sheet.background_7_name.GetValue())
	node4.appendChild(node5)
        node3.appendChild(node4)
	node4 = dom.createElement("background_level")
	node5 = dom.createTextNode(str(sheet.background_7_level.value))
	node4.appendChild(node5)
        node3.appendChild(node4)
	node2.appendChild(node3)

	node.appendChild(node2)

	node2 = dom.createElement("disciplines")

	node3 = dom.createElement("discipline")
	node4 = dom.createElement("discipline_name")
	node5 = dom.createTextNode(sheet.discipline_1_name.GetValue())
	node4.appendChild(node5)
        node3.appendChild(node4)
	node4 = dom.createElement("discipline_level")
	node5 = dom.createTextNode(str(sheet.discipline_1_level.value))
	node4.appendChild(node5)
        node3.appendChild(node4)
	node2.appendChild(node3)

	node3 = dom.createElement("discipline")
	node4 = dom.createElement("discipline_name")
	node5 = dom.createTextNode(sheet.discipline_2_name.GetValue())
	node4.appendChild(node5)
        node3.appendChild(node4)
	node4 = dom.createElement("discipline_level")
	node5 = dom.createTextNode(str(sheet.discipline_2_level.value))
	node4.appendChild(node5)
        node3.appendChild(node4)
	node2.appendChild(node3)

	node3 = dom.createElement("discipline")
	node4 = dom.createElement("discipline_name")
	node5 = dom.createTextNode(sheet.discipline_3_name.GetValue())
	node4.appendChild(node5)
        node3.appendChild(node4)
	node4 = dom.createElement("discipline_level")
	node5 = dom.createTextNode(str(sheet.discipline_3_level.value))
	node4.appendChild(node5)
        node3.appendChild(node4)
	node2.appendChild(node3)

	node3 = dom.createElement("discipline")
	node4 = dom.createElement("discipline_name")
	node5 = dom.createTextNode(sheet.discipline_4_name.GetValue())
	node4.appendChild(node5)
        node3.appendChild(node4)
	node4 = dom.createElement("discipline_level")
	node5 = dom.createTextNode(str(sheet.discipline_4_level.value))
	node4.appendChild(node5)
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("discipline")
	node4 = dom.createElement("discipline_name")
	node5 = dom.createTextNode(sheet.discipline_5_name.GetValue())
	node4.appendChild(node5)
        node3.appendChild(node4)
	node4 = dom.createElement("discipline_level")
	node5 = dom.createTextNode(str(sheet.discipline_5_level.value))
	node4.appendChild(node5)
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("discipline")
	node4 = dom.createElement("discipline_name")
	node5 = dom.createTextNode(sheet.discipline_6_name.GetValue())
	node4.appendChild(node5)
        node3.appendChild(node4)
	node4 = dom.createElement("discipline_level")
	node5 = dom.createTextNode(str(sheet.discipline_6_level.value))
	node4.appendChild(node5)
        node3.appendChild(node4)
	node2.appendChild(node3)
	
	node3 = dom.createElement("discipline")
	node4 = dom.createElement("discipline_name")
	node5 = dom.createTextNode(sheet.discipline_7_name.GetValue())
	node4.appendChild(node5)
        node3.appendChild(node4)
	node4 = dom.createElement("discipline_level")
	node5 = dom.createTextNode(str(sheet.discipline_7_level.value))
	node4.appendChild(node5)
        node3.appendChild(node4)
	node2.appendChild(node3)

	node.appendChild(node2)
	
	node2 = dom.createElement("virtues")
	
	node3 = dom.createElement(str(sheet.conscience_conviction_name.GetValue().lower()))
	node4 = dom.createTextNode(str(sheet.conscience_conviction_level.value))
	node3.appendChild(node4)
	node2.appendChild(node3)

	node3 = dom.createElement(str(sheet.selfcontrol_instinct_name.GetValue().lower()))
	node4 = dom.createTextNode(str(sheet.selfcontrol_instinct_level.value))
	node3.appendChild(node4)
	node2.appendChild(node3)

	node3 = dom.createElement(str(sheet.courage_name.GetValue().lower()))
	node4 = dom.createTextNode(str(sheet.courage_level.value))
	node3.appendChild(node4)
	node2.appendChild(node3)

	node.appendChild(node2)
	
	root.appendChild(node)
	
	node = dom.createElement("humanity_path")
	tmp = sheet.humanity_path_name.GetValue()
	if tmp.lower() == "humanity":
	  node2 = dom.createElement("humanity")
	  node3 = dom.createTextNode(str(sheet.humanity_path_level.value))
	  node2.appendChild(node3)
	else:
	  node2 = dom.createElement("path")
	  node3 = dom.createElement("path_name")
	  node4 = dom.createTextNode(tmp)
	  node3.appendChild(node4)
	  node2.appendChild(node3)
	  node3 = dom.createElement("path_level")
	  node4 = dom.createTextNode(str(sheet.humanity_path_level.value))
	  node3.appendChild(node4)
	  node2.appendChild(node3)

	node.appendChild(node2)

	root.appendChild(node)

        node = dom.createElement("willpower")
	node2 = dom.createElement("willpower_max")
	node3 = dom.createTextNode(str(sheet.willpower_max.value))
	node2.appendChild(node3)
	node.appendChild(node2)
	node2 = dom.createElement("willpower_current")
	node3 = dom.createTextNode(str(sheet.willpower_current.value))
	node2.appendChild(node3)
	node.appendChild(node2)
	root.appendChild(node)

	node = dom.createElement("bloodpool")
	node2 = dom.createTextNode(str(sheet.blood_pool.value))
	node.appendChild(node2)
	root.appendChild(node)

	node = dom.createElement("health")
	node2 = dom.createTextNode(str(sheet.health.value))
	node.appendChild(node2)
	root.appendChild(node)

	node = dom.createElement("experience")
	node2 = dom.createTextNode(str(sheet.experience.GetValue()))
	node.appendChild(node2)
	root.appendChild(node)

    def xml2sheet(self,dom,sheet):
        pass
