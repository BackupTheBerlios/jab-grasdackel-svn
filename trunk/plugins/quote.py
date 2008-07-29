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
PLUGINNAME = "Quote"

##
#Dokumentation
##
#
##

import random
import urllib
from BeautifulSoup import BeautifulSoup

PROF_FILE = 'plugins/data/prof.txt'

def handler_bash(recipient, type, parameter):
    zufall = random.randint(1,4)
    if zufall <= 2:
        sock = urllib.urlopen("http://german-bash.org/action/random") 
        temp = sock.read()
        sock.close()
        soup = BeautifulSoup(''.join(temp))
        temp2 = soup.find("div",{"class" : "zitat"})
        text = str(temp2)
        text = text.replace("<span class=\"quote_zeile\">","")
        text = text.replace("</span>","")
        text = text.replace("<div class=\"zitat\">","")
        text = text.replace("</div>","")
        text = text.replace("&lt;","<")
        text = text.replace("&gt;",">")
        text = text.replace("&auml;","ae")
        text = text.replace("&Auml;","Ae")
        text = text.replace("&ouml;","oe")
        text = text.replace("&Ouml;","Oe")
        text = text.replace("&uuml;","ue")
        text = text.replace("&Uuml;","Ue")
        text = text.replace("&szlig;","ss")
        text = text.replace("&euro;","euro")
        text = text.replace("&quot;","\"")
        text = text.replace("\n\r\n","\n")
        tmp = text.strip().replace('\n\r\n', '\r\n')
        tmp = "\n"+tmp
        sendit(recipient, type, text)   
    elif zufall == 3:
        f = file(PROF_FILE,'r')
        sammlung = f.readlines()
        f.close()
        foo = ["1"]
        while foo != "0":
            zufall = random.randint(0, 1086)
            temp = sammlung[zufall]
            if temp[0] == "(":		
                text = "\n"+sammlung[zufall+1]
                text = text + sammlung[zufall+2]
                value = sammlung[zufall+2]
                if value[0] != "(":
                    text = text + sammlung[zufall+3]
                    value = sammlung[zufall+3]
                    if value[0] != "(":
                        text = text + sammlung[zufall+4]
                        value = sammlung[zufall+4]
                        if value[0] != "(":
                            text = text + sammlung[zufall+5]
                            value = sammlung[zufall+5]
                            if value[0] != "(":
                                text = text + sammlung[zufall+6]
                                value = sammlung[zufall+6]
                                if value[0] != "(":
                                    text = text + sammlung[zufall+7]
                                    value = sammlung[zufall+7]
                foo = "0"
        sendit(recipient, type, text)
    else:
        sock = urllib.urlopen("http://www.uni-bash.org/random") 
        temp = sock.read()
        sock.close()
        soup = BeautifulSoup(''.join(temp))
        temp2 = soup.find("div",{"id" : "content"})
        text = str(temp2)
        text = text.replace("<div id=\"content\">","")
        text = text.replace("<br /><br /><br /><br /> <br /> <br /> <br /> <br /> <br /> <br /> <br />","")
        text = text.replace("</span><br />","\r\n")
        text = text.replace("<br />","\r\n")
        text = text.replace("</div>","")
        text = text.replace("<h2>Zufaelliges Zitat</h2>","")
        text = text.replace("<input type=\"submit\" name=\"vote_plus\" value=\"+\" title=\"positiv bewerten\" style=\"background-color: #76CC50; color: white; border: 0px; padding: 0px; font-family: monospace;\" />","")
        text = text.replace("<input type=\"submit\" name=\"vote_minus\" value=\"-\" title=\"negativ bewerten\" style=\"background-color: #DE3F41; color: white; border: 0px; padding: 0px; font-family: monospace;\" />","")
        text = text.replace("<input type=\"hidden\" value=\"358\" name=\"quote_nummer\" />","")
        text = text.replace("</p>","")
        text = text.replace("<h2>Zufaelliges Zitat</h2><p>","")
        text = text.replace("<form action=\"/random\" method=\"post\">","")
        text = text.replace("<span style=\"font-weight: bold;\">","")
        text = text.replace("<p>","")
        text = text.replace("<img src=\"/brief.png\" border=\"0\" alt=\"Dieses Zitat weiterempfehlen\" title=\"Dieses Zitat empfehlen\" />","")
        text = text.replace("<span style=\"font-style: italic; font-weight: bold;\">","")
        text = text.replace("</span>","")
        text = text.replace("</form>","")
        text = text.replace("</a>","")
        text = text.replace("</h2>","")
        text = text.replace("Zufaelliges Zitat","")
        text = text.replace("<h2>","")
        text = text.replace("|","")
        text = text.replace("Zitat","")
        text = text.replace("","")
        text = text.replace("&lt;","<")
        text = text.replace("&gt;",">")
        text = text.replace("&auml;","ae")
        text = text.replace("&Auml;","Ae")
        text = text.replace("&ouml;","oe")
        text = text.replace("&Ouml;","Oe")
        text = text.replace("&uuml;","ue")
        text = text.replace("&Uuml;","Ue")
        text = text.replace("&szlig;","ss")
        text = text.replace("&euro;","euro")
        text = text.replace("&quot;","\"")
        text = text.replace(":"," ")
        text = text.replace("&#039;","'")
        text = text.replace("\n","\n\n")
        text = text.split()
        bar = ""
        foo = 16
        bar = "\n"
        for i in range(16):
            text[i] = ""
        for foo in range(len(text)):
            if text[foo] == "":
                pass
            else:
                if foo == 20:
                    bar = bar + "\n"
                else:
                    bar = bar + " " + text[foo]
        sendit(recipient, type, bar)

def handler_gbo(recipient, type, parameter):
    sock = urllib.urlopen("http://german-bash.org/action/random") 
    temp = sock.read()
    sock.close()
    soup = BeautifulSoup(''.join(temp))
    temp2 = soup.find("div",{"class" : "zitat"})
    text = str(temp2)
    text = text.replace("<span class=\"quote_zeile\">","")
    text = text.replace("</span>","")
    text = text.replace("<div class=\"zitat\">","")
    text = text.replace("</div>","")
    text = text.replace("&lt;","<")
    text = text.replace("&gt;",">")
    text = text.replace("&auml;","ae")
    text = text.replace("&Auml;","Ae")
    text = text.replace("&ouml;","oe")
    text = text.replace("&Ouml;","Oe")
    text = text.replace("&uuml;","ue")
    text = text.replace("&Uuml;","Ue")
    text = text.replace("&szlig;","ss")
    text = text.replace("&euro;","euro")
    text = text.replace("&quot;","\"")
    text = text.replace("\n\r\n","\n")
    tmp = text.strip().replace('\n\r\n', '\r\n')
    tmp = "\n"+tmp
    sendit(recipient, type, tmp) 
    
if AKTIVIERT:
    print PLUGINNAME + " Plugin aktiviert!"
    register_command_handler(handler_bash, '!bash', 'Liefert ein Zitat von Bash seiten', [''])
    register_command_handler(handler_gbo, '!gbo', 'Liefert ein Zitat von German-bash.org', [''])
else:
   print PLUGINNAME + " Plugin deaktiviert!"
