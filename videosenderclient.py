import cv2
import numpy as np
import socket
import sys
import pickle
import struct
import pyaudio
import wave

cap=cv2.VideoCapture(0)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.0.101',8089))
data = b''
payload_size = struct.calcsize("L")



while True:
    #Send voice data
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 40

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data1 = stream.read(CHUNK)
        frames.append(data1)
        s.send(data1)

####Recieve voice data

    RECORD_SECONDS = 4
    WAVE_OUTPUT_FILENAME = "server_output.wav"
    WIDTH = 2
    frames = []

    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(WIDTH),
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)


    data = s.recv(1024)
    i = 1
    while data != '':
        stream.write(data)
        data = s.recv(1024)
        i = i + 1
        frames.append(data)

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))


    import os

    os.system(WAVE_OUTPUT_FILENAME)

#####Send a video data
    ret,frame=cap.read()
    dat = pickle.dumps(frame)
    s.sendall(struct.pack("L", len(dat))+dat)

###Recieve video data
    while len(data) < payload_size:
        data += s.recv(8192)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    while len(data) < msg_size:
        data += s.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    ###

    frame=pickle.loads(frame_data)
    cv2.imshow('frame',frame)
    # add this
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break