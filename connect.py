import socket
s = socket.socket()
port = 90
s.connect(('192.168.43.102', port))
print(s.recv(1024))
# close the connection
s.close()