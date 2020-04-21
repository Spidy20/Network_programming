import socket
s = socket.socket()
host = input(str("Please enter server adress : "))
name = input(str("Please enter your name : "))
port = 8080
s.connect((host,port))
print("Connected...")
s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print( s_name, "has joined the chat room ")
while 1:
    message = s.recv(1024)
    message = message.decode()
    print(s_name,": ",message)
    message = input(name+': ')
    s.send(message.encode())
    if message == 'bye':
        s.send('bye'.encode())
        break