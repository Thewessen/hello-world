const ws = new WebSocket('ws://localhost:3000/guess');
let closed = false;

ws.onopen = function() {
  console.log('WebSocket Client Connected');
};

ws.onmessage = function(e) {
  addMessage('server', e.data);
};

ws.onclose = function() {
  closed = true;
  console.log('WebSocket connection closed');
};

function sendMessage() {
  const input = document.getElementById('input')
  if (input && input.value) {
    addMessage('client', input.value);
    ws.send(input.value);
  }
  return false;
}

function addMessage(source, msg) {
  if (!closed) {
    console.log(`${source}: "${msg}"`);
    const root = document.getElementById('message-box');
    const p = document.createElement('p');
    p.classList.add('message')
    p.classList.add(source)
    p.innerText = msg
    root.appendChild(p);
    window.scrollTo(0, document.body.scrollHeight);
  }
}
