var socket = io.connect('http://' + document.domain + ':' + location.port);

// Enviar mensaje
function enviarMensaje() {
    var mensaje = document.getElementById('mensaje').value;
    socket.emit('mensaje', mensaje);
}

// Recibir mensaje
socket.on('mensaje', function(msg) {
    var chat = document.getElementById('chat');
    var nuevoMensaje = document.createElement('p');
    nuevoMensaje.innerHTML = msg;
    chat.appendChild(nuevoMensaje);
});
