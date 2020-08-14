#cliente
import socket
import os
import subprocess
import pickle
s = socket.socket()
host ="192.168.1.17"
port = 4000

s.connect((host, port))

while True:
    data = str(s.recv(1024), "utf-8")

    if len(data) > 0:
        print(data)
        k = input()
        s.send(str.encode(k))

#con este podemos enviar objetos al server
def send_obj(carta):
    obj = pickle.dumps(carta)
    print(obj)
    obj = bytes(f'{len(obj):<{HEADER_SIZE}}', "utf-8") + obj
    s.send(obj)
#con esta funcion podemos recibir objetos que nos manden del server
def recv_obj():
    carta = s.recv(1024)
    carta = pickle.loads(carta)
    print(carta)