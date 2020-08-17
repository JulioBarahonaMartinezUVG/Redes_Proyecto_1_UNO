#cliente
import socket
import os
import pickle
import subprocess
HEADER_SIZE = 10
s = socket.socket()
host =input("ingrese la ip del servidor: ")
port = 4000
s.connect((host, port))

class cosa:
    x = 5

while True:
    #data = str(s.recv(1024), "utf-8")
    #data = recv_obj()
    data = s.recv(1024)
    data = pickle.loads(data[HEADER_SIZE:])
    if data:
        print(data.x)
        k = input()
        s.send(str.encode(k))


#con este podemos enviar objetos a otros clientes
def send_obj(o):
    print("a")
    obj = pickle.dumps(o)
    print("b")
    obj = bytes(f"{len(obj):<{HEADERSIZE}}", 'utf-8') + obj
    print("c")
    s.send(obj)
    print("d")

#con esta funcion podemos recibir objetos que nos manden
def recv_obj():
    obj = s.recv(1024)
    obj = pickle.loads(obj)
    return obj

def wake_up_server():
    pass
