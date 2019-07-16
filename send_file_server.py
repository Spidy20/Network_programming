import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((" ", 1820))
print('server created')
s.listen(10)
c, addr = s.accept()
print('COnncected',addr)

f = open("v.mp4", "rb")
datas = f.read(1024)

while datas:
    datas = f.read(1024)
    c.send(datas)
f.close()
print("Done sending...")