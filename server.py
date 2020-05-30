import socket
import time

ip = '0.0.0.0'
port = 9999

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

connection.bind((ip,port))
connection.listen(5)

print("listening on port 9999")

while True:
    client, addr = connection.accept()
    time.sleep(1)
    while True:
        x= str(input(f"${addr[0]}: "))
        client.send(x.encode())
        if x == "exit":
            client.close()
            break
        result = client.recv(1024)
        print(result.decode())
