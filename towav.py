import mido
import time
import numpy as np
from datetime import datetime
from scipy.io import wavfile

sampleRate = 44100

def note2freq(note):
    a = 440 #frequency of A (coomon value is 440Hz)
    return (a / 32) * (2 ** ((note - 9) / 12))

def wavdata_sine(frequency, length):
    t = np.linspace(0, length, int(sampleRate * length))  #  Produces a 5 second Audio-File
    y = np.sin(frequency * 2 * np.pi * t)  #  Has frequency of 440Hz
    return y

def wavdata_mute(length):
    y = np.zeros(int(sampleRate * length))
    return y

#y1 = wavdata_sine(440, 1)
#y2 = wavdata_mute(3)
#print(y1.shape)
#print(y2.shape)
#y1 = np.append(y1, y2)
#print(y1.shape)
#exit(1)
port = mido.open_output('Microsoft GS Wavetable Synth 0')
mid = mido.MidiFile('Musics/013.mid')
last = datetime.now()
data = wavdata_mute(0.1)
for msg in mid:
    if(hasattr(msg, 'channel') and msg.channel == 1 and hasattr(msg, 'note')):
        #cur = datetime.now()
        #print("{0}, {1}".format( cur - last, msg))
        #last = cur

        #data = np.append(data, wavdata_mute(0.2))
        data = np.append(data, wavdata_mute(msg.time))
        freq = note2freq(msg.note)
        
        if msg.velocity == 0:
            data = np.append(data, wavdata_mute(0.2))
        else:
            data = np.append(data, wavdata_sine(freq, 0.2))

        #time.sleep(0.2)
        #time.sleep(msg.time)
        #port.send(msg)
        #input('aaa')
wavfile.write('aaa.wav', sampleRate, data)
