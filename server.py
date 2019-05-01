import socket
import pyaudio
import threading

# To do:
# [done] Handle client disconnect
# - Implement specific client voice communication
# - Identify clients by room number
# - Record microphone input only if broadcasting voice

# Socket
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000
SERVER_ADDRESS = HOST + ':' + str(PORT)
CONNECTED_CLIENTS = []

# Audio
p = pyaudio.PyAudio()
CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


def client_listener():
    while True:
        try:
            connection, address = server_socket.accept()
            handle_client_thread = threading.Thread(target=handle_client, args=(connection, address))
            handle_client_thread.start()
            CONNECTED_CLIENTS.append(connection)
            print(CONNECTED_CLIENTS)
            print('Connection from ' + address[0] + ':' + str(address[1]))
        except KeyboardInterrupt:
            pass


def handle_client(client, client_address):
    client.send(f'Connected to {SERVER_ADDRESS}'.encode('utf-8'))


with socket.socket() as server_socket:
    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print('[Server hosted at ' + SERVER_ADDRESS + ']')

        # Creates a separate thread for listening for clients
        client_listener_thread = threading.Thread(target=client_listener)
        client_listener_thread.start()
        print('Listening for clients...')

        # Records and sends microphone input to connected clients (the main thread)
        while True:
            try:
                microphone_input = stream.read(CHUNK)
                for client in CONNECTED_CLIENTS:
                        client.send(microphone_input)

            # Handles client disconnect
            except ConnectionResetError:
                    print(client.getpeername()[0] + ' Disconnected')
                    CONNECTED_CLIENTS.remove(client)
                    print(CONNECTED_CLIENTS)

            except KeyboardInterrupt:
                for client in CONNECTED_CLIENTS:
                    client.close()
                    break

    except socket.error as error:
        print(str(error))