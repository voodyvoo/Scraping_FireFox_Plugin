# Scraping_FireFox_Plugin
A little FireFox Plugin with native Python Component to scrape visited Websites.

Dieses Projekt wurde im Rahmen des Informatik-Studiums erstellt. Eine ausführliche Dokumentation ist in der Datei ProjektDokumentation.pdf zu finden.


Vorraussetzungen:
1. Betriebssystem: die Software wurde für das Betriebssystem Win10 entwickelt.
2. Browser: Der Browser-Extension Anteil der Software ist für den Browser Firefox von Mozilla ausgelegt.
3. Python: Die native Programm-Komponente setzt voraus, dass auf dem Anwender-Computer Python installiert ist.
Bei der Entwicklung wurde die Version 3.7 genutzt. Es ist darauf zu achten, dass alle notwendigen Bibiliotheken vorhanden sind.

Um die Software zu installieren sind folgende Schritte notwendig:
1. Die Dateien app.py, app.bat und app.json müssen im Ordner C:\praktWebExt gespeichert werden. 
2. Die Datei install.bat legt einen Registry-Key an, der benötigt wird um das Zusammenspiel der nativen Anwendung
mit der Browser-Extension zu ermöglichen.
3. In Firefox ist die Seite about:addons aufzurufen. Im Menü dieser Seite, 
wird das eigentliche Add-on aus der Datei praktikumextension-3.0-an+fx-windows.xpi installiert.

Hinweis:
Es ist möglich die Dateien der nativen Komponente in einem anderen Ordner zu speichern. In dem Fall funktioniert die install.bat Datei 
nict mehr. Statt dessen muss dann per Hand ein standard Registry Key unter angelegt werden:
REG ADD HKEY_LOCAL_MACHINE\"alternativer eigener Dateipfad"\app /d C:\praktWebExt\app.json

Sobald die Installation abgeschlossen ist, legt das Programm im Ordner C:\praktWebExt für jede Firefox-Sitzung
neue Subordner an, in denen die Ergebnisse gespeichert werden.
Während das Programm läuft können die Abläufe über die Browser-Entwickler-Konsole verfolgt werden.
