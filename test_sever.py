import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((" ", 100))
print('server created')
s.listen(10)
c, addr = s.accept()
print('{} connected.'.format(addr))


global data
data = c.recv(1024)

while data != '':
    f = open("recieved.mp3", "wb")
    data = c.recv(1024)
    f.write(data)
    f.close()
    break
print("Done receiving")
import os
os.system('recieved.mp3')


