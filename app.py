from flask import Flask, render_template
from flask_socketio import SocketIO
import os

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print('Usuario conectado')

@socketio.on('disconnect')
def handle_disconnect():
    print('Usuario desconectado')

@socketio.on('mensaje')
def handle_message(data):
    username = data.get('username')
    mensaje = data.get('mensaje')

    if username and mensaje:
        mensaje_completo = f'{username}: {mensaje}'
        socketio.emit('mensaje', mensaje_completo)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    socketio.run(app, host='0.0.0.0', port=port)


