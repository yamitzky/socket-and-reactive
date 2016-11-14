from flask import Flask
from flask_socketio import SocketIO, send
from pymongo import MongoClient
from bson import json_util


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
sio = SocketIO(app)


@sio.on('query')
def handle_query(query):
    client = MongoClient('db')
    for row in client.test.test.find(query):
        send(json_util.dumps(row))


if __name__ == '__main__':
    sio.run(app, host='0.0.0.0')
