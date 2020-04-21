import socket
import pyaudio
import wave

HOST = '192.168.43.102'
PORT = 50
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
conn, addr = s.accept()
print ('Connected by', addr)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS1 = 40
RECORD_SECONDS = 4

WAVE_OUTPUT_FILENAME = "server_output.wav"
WIDTH = 2
frames = []

while True:
    ##Send voice
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("*recording")

    frames1 = []

    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS1)):
        data  = stream.read(CHUNK)
        frames.append(data)
        conn.send(data)


    ###Recieve a voice data
    p1 = pyaudio.PyAudio()
    stream1 = p1.open(format=p1.get_format_from_width(WIDTH),
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)

    data1 = conn.recv(1024)
    i=1
    while data1 != '':
        stream1.write(data1)
        if data1:
            data1 = conn.recv(1024)
            print('Voice recieving')
        i=i+1
        frames1.append(data1)
        print(frames1)

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    print(wf)
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p1.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames1))
    import os
    os.system(WAVE_OUTPUT_FILENAME)