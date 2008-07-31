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
PLUGINNAME = "casino"

##
#Dokumentation
##
#Hier gibt es 2 Befehle:
#1: !casino parameter
# Gluecksspiel
#2: !casino_help
# DIeser Befehl zeit die Parameter an
##

import random

def handler_casino(recipient, type, parameter):
        if parameter == 'coin':
                zufall = random.randint(1,1000000)
                if zufall % 2== 1:
                        message = "Sie haben Kopf geworfen"
                else:
                        message = "Sie haben Zahl geworfen"
        elif parameter == 'dice':
                value = 0
                while value == 0:
                        zufall = random.randint(1,1000000)
                        zufall = zufall % 7
                        zufall = str(zufall)
                        if zufall != "0":
                                value = 1
                        else:
                                pass
                message = "Sie haben eine "+zufall+" gewuerfelt"
        else:
                message = "Entweder waehlen sie ein Spiel oder sie werden aus dem casino geschmissen ;)"
        sendit(recipient, type, message)

def handler_casino_help(recipient, type, parameter):
	 message = """Folgene Parameter sind beim Casino moeglich
!casino coin - Eine Muenze wird geworfen
!casino dice - Ein Wuerfel wird geworfen
"""
	 sendit(recipient, type, message)

if AKTIVIERT:
    print PLUGINNAME + " Plugin aktiviert!"
    register_command_handler(handler_casino, '!casino', 'Ein Wuerfel bzw. Muenze wird geworfen', ['!casino dice'])
    register_command_handler(handler_casino_help, '!casino_help', 'Befehl liefert eine Hilfe zum casino', ['!casino_help'])
else:
   print PLUGINNAME + " Plugin deaktiviert!"







