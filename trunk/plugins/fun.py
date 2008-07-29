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
PLUGINNAME = "Fun"

##
#Dokumentation
##
#
##

import random

QUOTE_FILE = 'plugins/data/quotes.txt'
DACKEL_FILE = 'plugins/data/dackel.txt'
JOKE_FILE = 'plugins/data/witze.txt'

def handler_quote(recipient, type, parameter):
    myfile = file(QUOTE_FILE,'r')
    sammlung = myfile.readlines()
    myfile.close()
    message = unicode(random.choice(sammlung), 'utf8')
    sendit(recipient, type, message.rstrip())

def handler_fortune(recipient, type, parameter):
    message = handler_python_sh('fortune')
    sendit(recipient, type, message.rstrip())

def handler_status(recipient, type, parameter):
    f = file(DACKEL_FILE,'r')
    sammlung = f.readlines()
    f.close()
    message = unicode(random.choice(sammlung), 'utf8')
    sendit(recipient, type, message.rstrip())
    
def handler_joke(recipient, type, parameter):
    f = file(JOKE_FILE,'r')
    sammlung = f.readlines()
    f.close()
    message = unicode(random.choice(sammlung), 'utf8')
    sendit(recipient, type, message.rstrip())    
    
if AKTIVIERT:
    print PLUGINNAME + " Plugin aktiviert!"
    register_command_handler(handler_quote, '!quote', 'Gives a random quote.', [''])
    register_command_handler(handler_fortune, '!fortune', 'liefert das ergebniss des shell befehls', [''])
    register_command_handler(handler_status, '!status', 'der bot sagt...', [''])
    register_command_handler(handler_joke, '!joke', 'gibt einen Witz aus', [''])
else:
   print PLUGINNAME + " Plugin deaktiviert!"
