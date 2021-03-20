// @repl-it-link:https://repl.it/@4shub/server-sent-events-node
const express = require('express');

const server = express();
const port = 3000;

server.get('/', (req, res) => {
  res.sendFile('./index.html', { root: __dirname });
});

server.get('/stream-random-numbers', (req, res) => {
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');

  /*
   * For efficiency reasons, Node.js normally buffers the request headers until
   * request.end() is called or the first chunk of request data is written. It
   * then tries to pack the request headers and data into a single TCP packet.

   * That's usually desired (it saves a TCP round-trip), but not when the first data
   * is not sent until possibly much later. request.flushHeaders() bypasses the
   * optimization and kickstarts the request.
   */
  res.flushHeaders();

  // We are sending anyone who connects to /stream-random-numbers
  // a random number that's encapsulated in an object
  let interval = setInterval(() => {
      const data = { value: Math.random() };
      const sseFormattedResponse = `data: ${JSON.stringify(data)}\n\n`;
      res.write(sseFormattedResponse);
  }, 1000);

  // close
  res.on('close', () => {
      clearInterval(interval);
      res.end();
  });
});


server.listen(port, () => console.log(`Example app listening at 
    http://localhost:${port}`));

