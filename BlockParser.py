import FrequencyFunctions
from pythonosc import udp_client

def osc_setup(ip_address="127.0.0.1", port_number=57120):
    return udp_client.SimpleUDPClient(ip_address, port_number)

def block_parser(a, client):
    melody = a[0]
    chords = a[1]
    bass = a[2]
    client.send_message("/melody", melody)
    print("/melody", end=" ")
    print(melody)
    client.send_message("/chords", chords)
    print("/chords", end=" ")
    print(chords)
    client.send_message("/bass", bass)
    print("/bass", end=" ")
    print(bass)
    return

if __name__ == "__main__":
    client = osc_setup()
    block_parser(FrequencyFunctions.c, client)
