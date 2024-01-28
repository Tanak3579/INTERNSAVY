from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print('Message from {}: {}'.format(data['username'], data['message']))
    emit('message', data, broadcast=True)

@socketio.on('join')
def handle_join(data):
    print('{} has joined the chat.'.format(data['username']))
    emit('message', {'username': 'System', 'message': '{} has joined the chat.'.format(data['username'])}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
