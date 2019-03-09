import FrequencyFunctions as ff
from pythonosc import udp_client
'''
#CompAlgorithm(440)


a = ff.Create12TETChromatic(440)
b = ff.StandardMajScale(a)
#c = TETMajScale(440, 9)
#d = calculateCents(b, c)

c = ff.genBlock(b, 5) #the scale i created above and the fifth chord in the scale
#print(c)



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
'''

def osc_setup(ip_address="127.0.0.1", port_number=57120):
    return udp_client.SimpleUDPClient(ip_address, port_number)
    
def triad_send(array, client):
    #a is a 1 dimensional array with only three values
    #if more than 3 values are in the array, the rest is ignored
    client.send_message("/triad", array)
    #possiblity of adding error handling to return function or to send data elsewhere or external analysis
    return 

def tone_send(tone, client):
    #tone is a single floating point integer
    client.send_message("/tone", float(tone))
    #possiblity of adding error handling to return function or to send data elsewhere or external analysis
    return

if __name__ == "__main__":
    client = osc_setup()
    triad_send([0,200,400], client)
    tone_send(700, client)