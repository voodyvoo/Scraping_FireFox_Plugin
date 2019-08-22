#!/usr/bin/env python

import sys
import json
import struct
import time
import csv
# import webbrowser
import os
import pathlib
from PIL import ImageGrab

try:
    # Erstelle einen String mit der codierten Systemzeit.
    ts = time.strftime("%Ss%Mm%Hh%p%d%b%y", time.localtime())
    # derzeitiger Arbeitsordner
    currentpath=os.getcwd()
    # Systemzeit-String wird neuer Arbeitsordner.
    pathlib.Path(currentpath+'/'+ts).mkdir(parents=True, exist_ok=True)
    # Erstelle CSV.Datei mit entsprechendem Header, innerhalb des Ordners zum Speichern der Nachrichten.
    with open(ts+'/'+ts+".csv",'w+', newline='') as csvfile:
        fieldnames = ['messageId', 'url', 'innerHTML', 'outerHTML', 'tagName', 'textContent' ,'currentURL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    # Reaktion auf den Eingang einer JSON-Message über die Stdin-Schnittstelle
    def getMessage():
        rawLength = sys.stdin.buffer.read(4)
        if len(rawLength) == 0:
            sys.exit(0)
        messageLength = struct.unpack('@I', rawLength)[0]
        message = sys.stdin.buffer.read(messageLength).decode()#'utf-8')
        jsonMessage= json.loads(message)
        # Die Werte der JSON-Message sollen in die zu Beginn
        # generierte CSV-Datei geschrieben werden.
        with open(ts+'/'+ts+'.csv', 'a', newline='') as csvfile:
            fieldnames = ['messageId', 'url', 'innerHTML', 'outerHTML', 'tagName', 'textContent', 'currentURL']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(jsonMessage)
        # Ausserdem soll ein Screenshot gemacht und das Ergebnis gespeichert werden.
        # Dieser teil des Codes soll Schnittstelle für spätere Anwendungen werden.
        im=ImageGrab.grab(bbox=(10,10,500,500))
        im.save(ts+'/'+time.strftime("%Ss%Mm%Hh%p%d%b%y", time.localtime())+'.png')
        return jsonMessage

    # Die Antwort der Python App an das Background-Script muss wieder in
    # JSON codiert werden.
    def encodeMessage(messageContent):
        encodedContent = json.dumps(messageContent).encode('utf-8')
        encodedLength = struct.pack('@I', len(encodedContent))
        return {'length': encodedLength, 'content': encodedContent}


    # Die entsprechende NAchricht wird über die Stdout-Schnittstelle verschickt.
    def sendMessage(encodedMessage):
        sys.stdout.buffer.write(encodedMessage['length'])
        sys.stdout.buffer.write(encodedMessage['content'])
        sys.stdout.buffer.flush()

    # Falls eine Nachricht eingegangen ist, soll eine Quittung an das
    # Background-Script geschickt werden.
    while True:
        receivedMessage = getMessage()
        if receivedMessage:
            sendMessage(encodeMessage("pong3"))
except AttributeError:
    # wenn Error, dann kaputt
    sys.exit(0)
