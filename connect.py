import socket

s = socket.socket()
port = 2247
s.connect(('192.168.43.153', port))
print(s.recv(1024))
s.close()