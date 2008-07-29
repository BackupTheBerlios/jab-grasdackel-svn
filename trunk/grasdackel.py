#!/usr/bin/python

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

import sys
import os
import xmpp
import thread
import re
# Wofuer war signal ?
import signal

def messageCB(conn,msg):
	# print msg
	if msg.getType() == "groupchat":
		temp = str(msg.getFrom()).split("/", 1)
		sender = temp[0]	# Naricht kommt vom Gruppenchat
	elif msg.getType() == "chat":
		sender = msg.getFrom()	# Naricht kommt aus dem privat Chat
	if not re.search('.*/' + BOTNAME+'.*',str(msg.getFrom())): # Wenn Naricht nicht vom Bot stammt
		if msg.getSubject():	# wenn das Topic dabei ist - speicher es
			global topic
			topic = msg.getSubject().encode('utf-8')
		if msg.getBody():	# Wenn Text vorhanden ist
			if not msg.getTimestamp(): # wenn Message keinen Timestamp enthaelt -- Annahme: sonst veraltet
				text = msg.getBody().encode('utf-8')
				print str(msg.getFrom()) +": " + text # Ausgabe auf Terminal
				splittext = text.split(" ", 1)
				global COMMAND_HANDLERS
				if text == "!help":
					global bothelp
					sendit(msg.getFrom(), msg.getType(), bothelp)
				if COMMAND_HANDLERS.has_key(splittext[0]):
					if " " in text:
						thread.start_new(COMMAND_HANDLERS[splittext[0]], (sender, msg.getType(), splittext[1]))
					else:
						thread.start_new(COMMAND_HANDLERS[splittext[0]], (sender, msg.getType(), ""))
				else:
					pass
					#Logging()
def presenceCB(conn,msg):
	global kontaktliste
	global status
	global initial
	raumkontakte = RAUMLISTE
	absender = str(msg.getFrom()).split("/", 1)
	raum = absender[0]

	print msg
	
	if RAUMLISTE.count(raum) == 1:
		print "Meldung aus einem Gruppenchat!"
		#print msg
	else:
		print "Globale Kontaktliste Meldung"
		if str(msg.getFrom()) not in kontaktliste:
			#print msg
			kontaktliste[str(msg.getFrom())] = [True, "Online"]
			#print kontaktliste.keys()
			#print kontaktliste.values()
			#print str(msg.getFrom()) + " ist online."
			#initial.append(True)
def register_command_handler(instance, command, description='', examples=[]):
	COMMAND_HANDLERS[command] = instance
	COMMANDS[command] = {'description': description, 'examples': examples}
def sendit(recipient, type, msg, topic=None):
	if topic:
		cl.send(xmpp.protocol.Message(recipient,"", type, topic))
	else:
		cl.send(xmpp.protocol.Message(recipient,msg,type))
def StepOn(conn):
	try:
		conn.Process(1)
	except KeyboardInterrupt:
		return 0
	return 1
def GoOn(conn):
	while StepOn(conn):
		pass
def handler_python_sh(parameters):
	# Send STDERR to STDOUT.
	pipe = os.popen('sh -c "%s" 2>&1' % parameters)
	# time.sleep(0.5)
	# 4k buffer equals to 2 standard console (80x25) pages.
	return_value = pipe.read(4096)
	return unicode(return_value, 'utf8')
def find_plugins():
	valid_plugins = []
	possibilities = os.listdir('plugins')
	for possibility in possibilities:
		if possibility[-3:].lower() == '.py':
			valid_plugins.append(possibility)
	return valid_plugins
def load_plugins():
	valid_plugins = find_plugins()
	for valid_plugin in valid_plugins:
		try:
			print 'Plugin ' + valid_plugin + ' gefunden.'
			fp = file('plugins/' + valid_plugin)
			exec fp in globals()
			fp.close()
		except:
			raise
def main():  
	jid=xmpp.protocol.JID(JABBERID)
	global cl
	cl = xmpp.Client(jid.getDomain(), debug=[])
	cl.connect((SERVER,PORT))
	cl.auth(jid.getNode(),PASSWORT)
	cl.sendInitPresence()
	cl.RegisterHandler('message', messageCB)
	cl.RegisterHandler('presence',presenceCB)
	for raum in RAUMLISTE:
		cl.send(xmpp.Presence(to=raum+"/"+BOTNAME))
	load_plugins()
	global bothelp
	bothelp = "Folgende Funktionen werden angeboten:\n"
	for name, description in COMMANDS.items():
		anhang = eval(str(description))
		liste = anhang['examples']
		if liste[0] == '':
			bothelp = bothelp + name + " - " + anhang['description'] + "\n"
		else:
			bothelp = bothelp + name + " - " + anhang['description'] + " - Beispiel: " +liste[0] + "\n"
	GoOn(cl)
kontaktliste = {}
topic = ''
bothelp = ""
COMMAND_HANDLERS = {}
COMMANDS = {}
fp = file('config.cfg')
exec fp in globals()
fp.close()
main()
