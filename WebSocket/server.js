const express = require('express');
const app = express();
const port = 3000;
const SUCCESS = 'Congratulations';

app.use(express.static('public'));

// required for using 'ws' app method
const wsInstance = require('express-ws')(app);
const wss = wsInstance.getWss();

const guessingGame = () => {
  const secret = Math.round(Math.random() * 100);
  return (number) => {
    const n = Number(number);
    if (n === NaN) {
      return 'This is not a number!'
    } else if (n < secret) {
      return 'Too low! Try to guess higher.'
    } else if (n >= 100 || n <= 0) {
      return 'Number needs to be between 1 and 100'
    } else if (n > secret) {
      return 'Too high! Try to guess lower.'
    } else if (n === secret) {
      return SUCCESS;
    }
  }
}

app.get('/', (req, res) => {
  res.sendFile('./index.html', { root: __dirname });
});

app.ws('/guess', (ws, req) => {
  if (wss.clients.size > 1) {
    const msg = 'Server too crowded! Closing the connection'
    console.log(`Server: "${msg}"`);
    ws.send(msg);
    ws.close();
    return;
  }
  console.log('WebSocket Client Connected');
  console.log(`Server: "Guess a number between 1 and 100"`);
  const guess = guessingGame();
  ws.send('Guess a number between 1 and 100');
  ws.on('message', (msg) => {
    const resp = guess(msg);
    console.log(`Client: "${msg}"`);
    console.log(`Server: "${resp}"`);
    ws.send(resp);
    if (resp === SUCCESS) {
      ws.send('Closing the connection now');
      ws.close();
    }
  })
});

app.listen(port, () => console.log(`Example app listening at 
    http://localhost:${port}`));
