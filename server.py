import socket
s = socket.socket()
print("Socket successfully created")
try:
    port = 90
    s.bind(('', port))
    print("socket binded to %s" % (port))
    s.listen(5)
    print("socket is listening")
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)
        output = 'hello i am kushal bhavsar'
        c.sendall(output.encode('utf-8'))
        c.close()
except Exception as e:
    print(e)

