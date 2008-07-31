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
PLUGINNAME = "calc"

##
#Dokumentation
##
#der parameter string koennte noch genauer untersucht werden bevor er an expr angehaengt wird
#z.b. ob die syntax fuer expr korrekt ist und wenn nicht aendern
##


def handler_calc(recipient, type, parameter):
	parameter = "expr "+parameter
	ergebniss = handler_python_sh(parameter)
	print ergebniss[0]
	if ergebniss[0] == "e":
		message = "Falsche Eingabe"
	else:
		message = "Das Ergebniss von "+parameter+" lautet: "+ergebniss
	sendit(recipient, type, message)

if AKTIVIERT:
    print PLUGINNAME + " Plugin aktiviert!"
    register_command_handler(handler_calc, '!calc', 'Ein einfacher Taschenrechner', ['!calc 7+3'])
else:
   print PLUGINNAME + " Plugin deaktiviert!"







