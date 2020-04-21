import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print("Sever adress is", host)
name = input(str("Please enter your username : "))
s.listen(1)
print("Waiting for any incoming connections ... ")
conn, addr = s.accept()
print("Recieved connection")
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room")
conn.send(name.encode())
while 1:
    message = input(name+': ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name,": ",message)
    if message == 'bye':
        conn.send('bye'.encode())
        break