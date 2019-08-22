/*
On startup, connect to the "ping_pong" app.
*/
var port = browser.runtime.connectNative("app");

/*
Listen for messages from the app.
*/
port.onMessage.addListener((response) => {
  console.log("Backgroud Received: " + response);
});

browser.runtime.onMessage.addListener(notify);

function notify(message) {
  //var messageString = JSON.stringify(message);
  console.log("Background Sending:  ping");
  //console.log(messageString);allMovieData.replace(/\n/g, '');
  var jsonString= JSON.stringify(message)
  console.log(jsonString);
  jsonMessage= JSON.parse(jsonString)
  port.postMessage(jsonMessage);
}
