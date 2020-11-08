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

# here are the objects that we are using

#default player object

class Player:
    def __init__(self, name):
        self.name = name
        self.game = ""
        self.cards = []

    #when called returns the player name
    def get_name(self):
        return self.name

    def set_name(self, nombre):
        self.name = nombre

    #sets the player to an
    def set_game(self, gameAddress):
        self.game = gameAddress

    def get_game(self):
        return self.game

    def set_cards(self, card):
        self.cards.append(card)

    def get_cards(self):
        return self.cards

# sets card value and color
class Card:
    def __init__(self, color, value):
        self.color = color # rojo, azul, verde, amarillo, multicolor
        self.value = value # 0-9, skip, reverse, +2, +4, change

    def get_color(self):
        return self.color

    def get_value(self):
        return self.value

    def set_color(self,new_color):
        self.color = new_color

    def set_value(self, new_value):
        self.value = new_value

#When a game starts a deck is assigned
# TODO: shuffle cards and return card
class Deck:
    def __init__(self):
        self.cards = []
        self.populate()
        self.shuffle_Deck()

    #adds a card to the deck
    def add_card(self, Card):
        self.cards.append(Card)

    def get_cards(self):
        return self.cards

    def set_cards(self, new_cards):
        self.cards = new_cards

    def cant_cartas(self):
        return len(self.cards)

    def pop_card(self):
        return self.cards.pop(0)

    # creates the amounts of cards needed to play
    def populate(self):
        import random
        spade = "♠"
        heart = "♥"
        diamond = "♦"
        club = "♣"
        cards = [
            (1, spade, '0'), (2, spade, '1'), (2, spade, '2'), (2, spade, '3'), (2, spade, '4'), (2, spade, '5'),
            (2, spade, '6'), (2, spade, '7'), (2, spade, '8'), (2, spade, '9'), (2, spade, '+2'), (2, spade, 's'),
            (2, spade, 'r'),

            (1, heart, '0'), (2, heart, '1'), (2, heart, '2'), (2, heart, '3'), (2, heart, '4'), (2, heart, '5'),
            (2, heart, '6'), (2, heart, '7'), (2, heart, '8'), (2, heart, '9'), (2, heart, '+2'), (2, heart, 's'),
            (2, heart, 'r'),

            (1, diamond, '0'), (2, diamond, '1'), (2, diamond, '2'), (2, diamond, '3'), (2, diamond, '4'),
            (2, diamond, '5'),
            (2, diamond, '6'), (2, diamond, '7'), (2, diamond, '8'), (2, diamond, '9'), (2, diamond, '+2'),
            (2, diamond, 's'),
            (2, diamond, 'r'),

            (1, club, '0'), (2, club, '1'), (2, club, '2'), (2, club, '3'), (2, club, '4'), (2, club, '5'),
            (2, club, '6'), (2, club, '7'), (2, club, '8'), (2, club, '9'), (2, club, '+2'), (2, club, 's'),
            (2, club, 'r'),

            (4,'m','w'),
            (4,'m','+4'),

        ]
        for card in cards:
            for amount in range(card[0]):
                c = Card(card[1],card[2])
                self.add_card(c)

        s = random.sample(self.get_cards(), len(self.cards))
        self.set_cards(s)

    def shuffle_Deck(self):
        cards = self.get_cards()
        for i in cards:
            print(i.get_value() + " "+ i.get_color())
        print(len(cards))

#each session is defined here
class GameState:
    def __init__(self):
        self.state =  ""
        self.winner = "No winner"

    def get_state(self):
        return self.state

    def get_winner(self):
        return self.winner

    def set_winner(self, name):
        self.winner

    def set_state(self, estado):
        self.state = estado
class ClientMessage:
    def __init__(self, tipo, content):
        self.tipo=tipo
        self.content=content

    def get_content(self):
        return self.content

    def get_tipo(self):
        return self.tipo

class ServerMessage:
    def __init__(self, tipo, content):
        self.tipo = tipo
        self.content = content

    def get_content(self):
        return self.content

    def get_tipo(self):
        return self.tipo

class board:
    def __init__(self):
        self.list_players = []
        self.turno = 0
        self.center_card = Card(None,None)

    def set_lPlayers(self, list):
        self.list_players = list
    def set_turno(self,turn):
        self.turno = turn
    def set_cenCard(self,card):
        self.center_card = card

    def get_lPlayers(self, list):
        return self.list_players
    def get_turno(self,turn):
        return self.turno
    def get_cenCard(self,card):
        return self.center_card

#con este podemos enviar objetos a otros clientes
def send_obj(o):
    obj = pickle.dumps(o)
    obj = bytes(f"{len(obj):<{HEADERSIZE}}", 'utf-8') + obj
    s.send(obj)

#con esta funcion podemos recibir objetos que nos manden
def recv_obj():
    obj = s.recv(1024)
    data = pickle.loads(obj[HEADER_SIZE:])
    return data


def put_card(card):
    global centerCard
    if ((card.get_color()==centerCard.get_color())or(card.get_value()==centerCard.get_value())or(card.get_color()=='m')):
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

def ganador_partida(nombre):
    print(nombre, "ganó la partida")

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
        elif (data.get_tipo()==4):
            ganador_partida(data.get_content())
        elif (data.get_tipo()==5):
            definir_turno(data.get_content())
        elif (data.get_tipo()==6):
            llenar_usernames(data.get_content())




def wake_up_server():
    pass
