import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((" ", 100))
print('server created')
s.listen(10)
c, addr = s.accept()
print('{} connected.'.format(addr))

f = open("ML.rar", "rb")
datas = f.read(1024)

while datas:
    c.send(datas)
    datas = f.read(1024)

f.close()
print("Done sending...")