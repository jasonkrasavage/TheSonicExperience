import socket
import pyaudio

# Socket
HOST = socket.gethostbyname(socket.gethostname())
# Use this instead if connecting from another computer
# HOST = 'enter server IPV4 here'
PORT = 5000

# Audio
p = pyaudio.PyAudio()
CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

with socket.socket() as client_socket:
    client_socket.connect((HOST, PORT))
    print(client_socket.recv(2048).decode('utf-8'))
    while True:
        data = client_socket.recv(CHUNK)
        stream.write(data)