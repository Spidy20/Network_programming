import socket
import pyaudio
import wave

# record
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "server_output.wav"
WIDTH = 2
HOST = '192.168.43.164'  # The remote host
PORT = 50  # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("*recording")

    frames = []

    # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    while True:
        data = stream.read(CHUNK)
        print(data)
        frames.append(data)
        if data:
            s.send(data)
            print("Sending audio")


    ###Recieve voice data

        frames1 = []
        p1 = pyaudio.PyAudio()
        stream1 = p1.open(format=p1.get_format_from_width(WIDTH),
                          channels=CHANNELS,
                          rate=RATE,
                          output=True,
                          frames_per_buffer=CHUNK)

        data1 = s.recv(1024)
        i = 1
        while data1 != '':
            stream1.write(data1)
            data1 = s.recv(1024)
            i = i + 1
            frames1.append(data1)

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p1.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames1))
        # wf.close()
        # stream.stop_stream()
        import os
        os.system(WAVE_OUTPUT_FILENAME)
    # stream1.close()