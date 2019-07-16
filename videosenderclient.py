import cv2
import numpy as np
import socket
import sys
import pickle
import struct

cap=cv2.VideoCapture(0)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.0.101',8089))
data = b''
payload_size = struct.calcsize("L")

while True:
    ret,frame=cap.read()
    dat = pickle.dumps(frame)
    s.sendall(struct.pack("L", len(dat))+dat)


    while len(data) < payload_size:
        data += s.recv(4096)
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