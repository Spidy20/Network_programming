import socket
import speech_recognition as sr
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.106", 100))

r = sr.Recognizer()
print(sr.Microphone())
with sr.Microphone() as source:
    print("Speak anything:")
    audio = r.listen(source)

s.send(audio)
s.close()
print('Connection closed')

