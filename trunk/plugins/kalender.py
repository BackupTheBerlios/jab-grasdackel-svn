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
PLUGINNAME = "Kalender"

##
#Dokumentation
##
#
##

import csv
import time

def calendar(typ):
    reader = csv.reader(open("plugins/data/freunde.csv", "rb"))
    liste=[]
    if typ == "topic":
        toprint = ' # Termine in den folgenden 7 Tagen:'
        for auswahl in reader:
            if time.time() < time.mktime(time.strptime(auswahl[8],' %d.%m.%Y %H:%M:%S')) < time.time()+604800: # 1 Woche
                liste.append(time.mktime(time.strptime(auswahl[8],' %d.%m.%Y %H:%M:%S')))
    elif typ == "ausgabe":
        toprint = 'Termine in den kommenden 3 Wochen:\n'
        for auswahl in reader:
            if time.time() < time.mktime(time.strptime(auswahl[8],' %d.%m.%Y %H:%M:%S')) < time.time()+1814400: # 3 Wochen
                liste.append(time.mktime(time.strptime(auswahl[8],' %d.%m.%Y %H:%M:%S')))
    liste.sort()
    for i in liste:
        auslese = csv.reader(open("plugins/data/freunde.csv", "rb"))
        for auswahl in auslese:
            if i == time.mktime(time.strptime(auswahl[8],' %d.%m.%Y %H:%M:%S')):
                if typ == "topic":
                    toprint = toprint + auswahl[1] + " am" + auswahl[8] + " # "
                elif typ == "ausgabe":
                    toprint = toprint + auswahl[1] + " am" + auswahl[8] + " bis" + auswahl[9] + "\n"
    if toprint == ' # Termine in den folgenden 7 Tagen:':
	toprint = ' # Keine Termine in den folgenden 7 Tagen.'
    
    return toprint.replace('00:00:00','')

def handler_kalender(recipient, type, parameter):
    message = calendar("ausgabe")
    sendit(recipient, type, message)
    
def handler_topic(recipient, type, aktuelltopic):
    global topic
    newtopic = topic + calendar("topic")
    if str(type) == "chat":
        sendit(recipient, type, "Topic Wechsel nur im Chat moeglich.")
    else:
        sendit(recipient,type,"", newtopic)

if AKTIVIERT:
    print PLUGINNAME + " Plugin aktiviert!"
    register_command_handler(handler_kalender, '!termine', 'liefert die Termine der naechsten 3 Wochen', [''])
    register_command_handler(handler_topic, '!topic', 'setzt das Topic mit Terminen in den kommenden 7 Tagen', [''])
else:
   print PLUGINNAME + " Plugin deaktiviert!"
