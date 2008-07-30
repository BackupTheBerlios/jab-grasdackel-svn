### Copyright (C) Grasdackel
##
##  This program is free software; you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation; either version 2 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program; if not, write to the Free Software
##  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
##
###

AKTIVIERT = True
PLUGINNAME = "slap"

##
#Dokumentation
##
#Hier gibt es 2 Befehle:
#1: !slap name parameter
# Mit diesem Befehl "slapt" der bot eine Person
#2: !slap_help
# DIeser Befehl zeit die Parameter an
##

def handler_slap(recipient, type, parameter):
	 parameter = parameter.split(' ',1)
	 name = parameter.pop(0)
	 text = parameter.pop(0)
	 if text == 'drives':
		  message = "/me drives over " + name
	 elif text == 'chainsaw':
		  message = "/me shreds " + name + " with a chainsaw"
	 elif text == 'cookies':
		  message = "/me steals " + name + "'s cookies. Mwahaha!"
	 elif text == 'ddos':
		  message = "/me sends some DDoS in "+ name+"'s direction"
	 elif text == 'desert':
		  message = "/me forgets "+name+" in the desert. awww"
	 elif text == 'goatsex':
		  message = "/me is searching for "+name+" goatsex on google. WEEE 80 hits!"
	 elif text == 'keyboard':
		  message = "/me throws a keyboard at "+name
	 elif text == 'lemmings':
		  message = "/me sends hordes of lemmings over "+name
	 elif text == 'mac':
		  message = "/me slaps "+name+" around with a pink Macintosh"
	 elif text == 'mouse':
		  message = "/me whips "+name+" with a mouse cord"
	 elif text == 'nuclear':
		  message = "/me slaps "+name+" around with nuclear waste"
	 elif text == 'ps':
		  message = "/me throws a playstation at "+name
	 elif text == 'burns':
		  message = "/me burns "+name+"'s house down"
	 elif text == 'picture':
		  message = "/me discovers "+name+"'s picture at uglypeople.com"
	 elif text == 'sneezes':
		  message = "/me sneezes in "+name+"'s face"
	 elif text == 'windows':
		  message = "/me slaps "+name+" around with a Windows System"
	 else:
		  message = "/me slap "+ name +" around with a large trout"
	 sendit(recipient, type, message)

def handler_slap_help(recipient, type, parameter):
	 message = """Folgene Parameter sind bei Slap moeglich
!slap person drives - drives over person
!slap person chainsaw - shreds person with a chainsaw
!slap person cookies - steals person's cookies. Mwahaha!
!slap person ddos - sends some DDoS in person's direction
!slap person desert - forgets person in the desert. awww
!slap person goatsex - is searching for person goatsex on google. WEEE 80 hits!
!slap person keyboard - throws a keyboard at person
!slap person lemmings - sends hordes of lemmings over person
!slap person mac - slaps person around with a pink Macintosh
!slap person mouse - whips person with a mouse cord"
!slap person nuclear - slaps person around with nuclear waste
!slap person ps - throws a playstation at person
!slap person burns - burns person's house down
!slap person picture - discovers person's picture at uglypeople.com
!slap person sneezes - sneezes in person's face
!slap person windows - slaps person around with a Windows System"
!slap person - slap person around with a large trout"""
	 sendit(recipient, type, message)

if AKTIVIERT:
    print PLUGINNAME + " Plugin aktiviert!"
    register_command_handler(handler_slap, '!slap', 'Befehl liefert eine slap ausgabe - large trout', ['!slap person'])
    register_command_handler(handler_slap_help, '!slap_help', 'Befehl liefert eine Hilfe zu slap', ['!slap_help'])
else:
   print PLUGINNAME + " Plugin deaktiviert!"







