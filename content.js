/*
https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Content_scripts
*/

var knownElement =0;
var urlVar;
var innerHTMLVar;
var outerHTMLVar;
var tagNameVar;
var globalIdCounter = 0;

// Eine einfache Funktion um einen ID-Counter für die verschickten Pakete zu generieren.
function countGlobalId() {
   globalIdCounter++;
   return globalIdCounter;
}

// Dem Mousemove-Event wird ein Listener "notifyExtension" angefügt.
window.addEventListener("mousemove", notifyExtension);

// Die auszuführende Funktion beim auftreten eines Mousemove-Events.
function notifyExtension(e) {
  if (e.target == knownElement) {
    return;
  }
  else {
    // aktuell besuchte URL:
    let currentURL = window.location.href;
    // Eigenschaften des auslösenden DOM-Elements:
    if (e.target.href)
      {urlVar= e.target.href;}
      else {urlVar= "empty";}
    if (e.target.innerHTML)
      {innerHTMLVar= e.target.innerHTML;}
      else {innerHTMLVar= "empty";}
    if (e.target.outerHTML)
      {outerHTMLVar= e.target.outerHTML;}
      else {outerHTMLVar= "empty";}
    if (e.target.tagName)
      {tagNameVar= e.target.tagName;}
      else {tagNameVar= "empty";}

// Die gesammelten Daten werden als JSON-Objekt an Background.js geschickt.
  browser.runtime.sendMessage(
    {"messageId": countGlobalId(),
    "url": urlVar,
    "innerHTML": e.target.innerHTML,
    "outerHTML": e.target.outerHTML,
    "tagName": e.target.tagName,
    "currentURL": currentURL});
  }
}
