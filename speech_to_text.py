import speech_recognition as sr
import os

r = sr.Recognizer()
print(sr.Microphone())
with sr.Microphone() as source:
    print("Speak anything:")
    audio = r.listen(source)
    print(audio)
try:
    text = r.recognize_google(audio)
    print("You said : {}".format(text))

    f = open("file.txt", "w+", encoding='utf-8')
    f.write(text)
    f.close()

except:
    print("Sorry could not recognize what you said")