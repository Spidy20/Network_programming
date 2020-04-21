import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.43.114", 1234))
f = open("KUsh.mp3", 'wb')
while True:
    datas = s.recv(1024)
    f.write(datas)
    f.close()
    break
print("Done receiving")