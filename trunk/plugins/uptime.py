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
PLUGINNAME = "Uptime"

##
#Dokumentation
##
#
##

def handler_uptime(recipient, type, parameter):
    message = handler_python_sh('uptime')
    sendit(recipient, type, message)

if AKTIVIERT:
   print PLUGINNAME + " Plugin aktiviert!"
   register_command_handler(handler_uptime, '!uptime', 'liefert die Uptime', [''])
else:
   print PLUGINNAME + " Plugin deaktiviert!"
