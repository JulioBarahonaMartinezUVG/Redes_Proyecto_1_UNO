#cliente
import socket
import os
import pickle
import subprocess
import Modelos

HEADER_SIZE = 10
s = socket.socket()
host =input("ingrese la ip del servidor: ")
port = 4000
s.connect((host, port))

#con este podemos enviar objetos a otros clientes
def send_obj(o):
    obj = pickle.dumps(o)
    obj = bytes(f"{len(obj):<{HEADERSIZE}}", 'utf-8') + obj
    s.send(obj)

#con esta funcion podemos recibir objetos que nos manden
def recv_obj():
    obj = s.recv(1024)
    data = pickle.loads(data[HEADER_SIZE:])
    return obj


def put_card(card):
    msg = Modelos.ClientMessage(0,card)
    send_obj(msg)

def put_chat(message):
    msg = Modelos.ClientMessage(1,message)
    send_obj(msg)

def take_card():
    msg = Modelos.ClientMessage(2,null)
    send_obj(msg)

def join_room(room):
    msg = Modelos.ClientMessage(3,room)
    send_obj(msg)

def change_name(name):
    msg = Modelos.ClientMessage(4,name)
    send_obj(msg)

def send_start():
    msg = Modelos.ClientMessage(5,null)
    send_obj(msg)
    

while True:
    #data = str(s.recv(1024), "utf-8")
    #data = recv_obj()
    data = recv_obj()
    if data:
        print(data.x)
        k = input()
        s.send(str.encode(k))



def wake_up_server():
    pass
