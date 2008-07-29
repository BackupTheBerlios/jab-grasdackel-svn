=============================================================================
				    TODO
=============================================================================

-1- Die Formatierung der History Funktion
	Topic wechsel
	Größe begrenzen

-2- Wochenplan ausgeben

-3- aktuelle Termine aus dem Kalender ausgeben, evtl. ans Topic anhängen?
	- handeln mehrerer kalenderdateien
	- termine hinzufuegen (moeglich mit user management)

-4- Bei einem Join ausgabe eines fortunes
	Problem: Wenn der Bot neu gestartet wird, muss jeder User erst einmal online und dann offline gegangen sind.
		Erst beim anschließenden Online kommen kann der Bot auf ihn reagieren.	

-6- Quizfunktion  (eher Version 2.0 oder eigener bot)
	Problem: sehr schwer und viel
	siehe moxxquizu

-10- Topic History/change
	- topics in txt datei speichern und evtl. termine (kalenderfunktion) anhängen
	Problem: Bot hängt nach einem neustart neue Termine an alte Termine an, eventuell Sonderzeichen definieren,
		welches dem Bot sagt, ab hier beginnen die Termine?!

-11- Timestamp vergleich - BEOBACHTEN andere Clients oder ist der Server dafür zuständig?

-12- RSS Feed (eher Version 2.0)
	- in verbindung mit usermanagement

-13- Timer Funktion (eher Version 2.0)
	z.b. erriner mich in 10min dadran dass...
	z.b. gib alle 10 Sekunden ein !gbo aus?

-14- Umfrage modul (eher Version 2.0)
	z.b. Heute abend grillen? :D

-15- User management (eher Version 2.0)
	- bestimmte befehle nur mit acc beim bot <-- für markus ;)
	- Bot soll eigene dynamische Kontaktliste führen

-16- Lyrik suchen und ausgeben wenn vorhanden  (eher Version 2.0)
	- lyrik wiki

-17- automatischer reconnect bei disconnect

-18- bot soll mehrere channels joinen (eher Version 2.0)
	- Problem: anpassen der hist funktion etc.
	- halte ich fuer wichtig und solte im Zuge eines dynamischeren Codes implementiert werden (Markus)

-19- admin controll
	- siehe User Management + interne Datenbank

-20- Allgemeines Fehler Management
	- Was passiert wenn das PW falsch ist etc...
	- exeptions werfen :D

-21- mehrsprachig
	- module für mehrere sprachen (Deutsch/Englisch/...)

-22- Hilfe automatisch generieren
	- z.b. als erste zeile eines plugins ein kommentar der den hilfetext zu dem Modul enthält

-23- evtl. mehr fun-befehle (ähnlich slap)
	- siehe IRC

-24- status des bots anzeigen
	- Ich bin in x channel
	- zeige channels und user in chans?

-25- Statistik funktion
	- X hat am X.x.x x zeilen geschrieben
	- in der zeit von 12 bis 14 urden soviele zeilen geschrieben
	- als html speichern und online stellen...
	- der bot hat heute x befehle ausgeführt
	- ...

-27- tip funktion
	- fussballergebnisse etc.

================================================
	Ziele für Version 1.0:
================================================
	weitere Funktionen siehe todo
	modularer Aufbau / dynamisch
		- Pakete wie fun oder kalender erstellen (siehe openbook Chap. 11)
		- Am anfang einer Funktion eine boolean var welche aussagt ob die funktion aktiviert ist oder nicht
		- Status befehl um zu gucken welche plugins aktiviert sind
	quellcode vereinfachen
	help aktualisieren
	quelltext kommentieren!!!
	Exceptions schmeissen

	Zielsetzung: Was soll unseren Bot auszeichen? Einfachheit, viele Funktionen, wenige aber besondere Funktionen
		Wir sollten uns gegenüber anderen Jabber Bots klarmachen, was unser Bot besser / leichter kann.

	!!! WICHTIG: README, todo, LICENSE und knownbugs bearbeiten !!!
	weiteres:
	channel auf offenem server für direkte fragen
	email-adressen 
	jabber kontaktdaten.... 
	veröffentlichen: evtl. bei ubuntuusers

	erstellen einer kleinen website
	später evtl. wiki <-- währe fürs arbeiten angenehm
	 http://www.debacher.de/wiki/Wiki-Installation
