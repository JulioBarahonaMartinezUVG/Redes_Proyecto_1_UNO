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
username=""
isTurn=False
myhand=[]
centerCard=None
playerCardsAmmount=[]
usernames=[]
turno=0

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
    global centerCard
    if ((card.get_color()==centerCard.get_color())||(card.get_value()==centerCard.get_value())||(card.get_color()=='m')):
        if isTurn:
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
    global username
    username=name
    msg = Modelos.ClientMessage(4,name)
    send_obj(msg)

def send_start():
    msg = Modelos.ClientMessage(5,null)
    send_obj(msg)



def desplegar_chat(chat):
    print(chat)

def actualizar_board(board):
    global turno
    global isTurn
    global centerCard
    global myHand
    global playerCardsAmmount
    lplay = board.get_lPlayers()
    isTurn=(turno==board.get_turno())
    centerCard=board.get_cenCard()
    myHand=lplay[turno-1]
    playerCardsAmmount=[]
    for i in lplay:
        playerCardsAmmount.append(len(i))
    


def definir_turno(pos):
    global turno
    turno=pos

def llenar_usernames(users):
    global usernames
    usernames=users

def pedir_color():
    a=True
    while a:
        color=input("Ingrese el numero del color que desea ponerle (1 rojo, 2 azul, 3 amarillo, 4 verde: \n")
        if (color==1):
            color="rojo"
            a=False
        elif(color==2):
            color="azul"
            a=False
        elif(color==3):
            color="amarillo"
            a=False
        elif(color==4):
            color="verde"
            a=False
    msg = Modelos.ClientMessage(6,color)
    send_obj(msg)

def unido_al_room(booleano):
    if (booleano):
        print("Se Conecto al room")

while True:
    #data = str(s.recv(1024), "utf-8")
    #data = recv_obj()
    data = recv_obj()
    if data:
        if (data.get_tipo()==0):
            actualizar_board(data.get_content())
        elif (data.get_tipo()==1):
            pedir_color()
        elif (data.get_tipo()==2):
            desplegar_chat(data.get_content())
        elif (data.get_tipo()==3):
            unido_al_room(data.get_content())
        elif (data.get_tipo()==5):
            definir_turno(data.get_content())
        elif (data.get-tipo()==6):
            llenar_usernames(data.get_content())




def wake_up_server():
    pass
