import io from 'socket.io-client';

const socket = io('http://localhost:8080');

export default {
  state: {
    events: [],
  },
  listenEvents() {
    socket.on('message', (msg) => {
      this.state.events.push(msg);
    });
  },
  clearEvents() {
    this.state.events = [];
  },
  sendRequest(req) {
    socket.emit('query', JSON.parse(req));
  },
};
