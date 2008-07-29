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

AKTIVIERT = False
PLUGINNAME = "Beispiel"

##
#Dokumentation
##
#Ein Beispielplugin
#kann zum entwickeln weiterer genutzt werden
##

def handler_beispiel(recipient, type, parameter):
    message = "Nur ein Beispiel!"
    sendit(recipient, type, message)

if AKTIVIERT:
   print PLUGINNAME + " Plugin aktiviert!"
   register_command_handler(handler_beispiel, '!beispiel', 'Befehl liefert eine Beispielausgabe', ['!beispiel'])
else:
    print PLUGINNAME + " Plugin deaktiviert!"
