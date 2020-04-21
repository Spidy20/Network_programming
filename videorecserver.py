import socket
import sys
import cv2
import pickle
import numpy as np
import struct
import pyaudio
import wave

HOST=''
PORT= 2020

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ('Socket created')

s.bind((HOST,PORT))
print ('Socket bind complete')
s.listen(10)
print ('Socket now listening')

conn,addr=s.accept()
print(addr)
data = b''
payload_size = struct.calcsize("L")
cap=cv2.VideoCapture(0)


while True:

#####Send frame data
    ret,frame=cap.read()
    dat = pickle.dumps(frame)
    conn.sendall(struct.pack("L", len(dat))+dat)

###Recieve frame data

    while len(data) < payload_size:
        data += conn.recv(1050000000)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    while len(data) < msg_size:
        data += conn.recv(1050000000)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    ###

    frame=pickle.loads(frame_data)
    cv2.imshow('frame',frame)
    # add this
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
#
#      # Send voice data
#     CHUNK = 1024
#     FORMAT = pyaudio.paInt16
#     CHANNELS = 1
#     RATE = 44100
#     RECORD_SECONDS = 40
#
#     p = pyaudio.PyAudio()
#
#     stream = p.open(format=FORMAT,
#                     channels=CHANNELS,
#                     rate=RATE,
#                     input=True,
#                     frames_per_buffer=CHUNK)
#     frames = []
#     for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#         data1 = stream.read(CHUNK)
#         frames.append(data1)
#         conn.send(data1)
#         print('Audio Sending')
#
# ###Recive voice data
#     RECORD_SECONDS = 4
#     WAVE_OUTPUT_FILENAME = "server_output.wav"
#     WIDTH = 2
#     frames = []
#
#     p = pyaudio.PyAudio()
#     stream = p.open(format=p.get_format_from_width(WIDTH),
#                     channels=CHANNELS,
#                     rate=RATE,
#                     output=True,
#                     frames_per_buffer=CHUNK)
#
#     data2 = conn.recv(1024)
#     i = 1
#     while data != '':
#         stream.write(data2)
#         data2 = conn.recv(1024)
#         i = i + 1
#         frames.append(data2)
#
#     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))
#     import os
#     os.system(WAVE_OUTPUT_FILENAME)
#     print('Playing Audio')