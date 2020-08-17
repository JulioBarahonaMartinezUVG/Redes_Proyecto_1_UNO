#server
# estos son los imports que necesitamos para el funcionamiento del server
import socket
import sys
import pickle
import threading
import time
from queue import Queue
#numero de threads
NUM_OF_THREADS = 2
#la cantidad de trabajos en los threads
JOB_NUM = [1,2]
#nuestro Queue de tareas
queue = Queue()
#la lista de jugadores conectados
all_connections = []
#la lista de direcciones
all_addres = []
#no se para que servia esta variable
HEADERSIZE = 10
#lista de los jugadores
list_players = []
turno = 0
start = False
Act_board = True
Board = None
Baraja = None
pila = []
cont = 0
#creamos los sockets(para la conexion entre dispositivos)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 4000
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error: " + str(msg))

#binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port: " + str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: "+ str(msg)+ "\n" + "Retrying...")
        #bind_socket()

#manejando la coneccion entre distintos clientes y agregandolos a la lista
#cerrando todas las conexiones anteriores del server.py al ser reseteado
def accepting_connection():
    global cont
    #en este for se encarga de cerrar todas las conexiones
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addres[:]
    #Aqui se realizan todas conexiones de multiples servers
    while True:
        try:
            if len(all_connections) <= 4:
                print(1)
                #confirma la conexion
                conn, address = s.accept()
                print(2)
                s.setblocking(1) #prevents timeout
                #conn.send(str.encode("te has conectado al server"))
                print(3)
                all_connections.append(conn)
                print(4)
                all_addres.append(address)
                print(5)
                print("connection has been established: " + address[0])
                cont += 1
                msg = ServerMessage(5, cont)
                send_obj(conn, msg)
                list_players.append(Player("player " + str(cont)))
                x = threading.Thread(target=jugador, args=(conn,cont,), daemon=True)
                x.start()
                msg = ServerMessage(6,list_players)
                for x in all_connections:
                    send_obj(x, msg)
        except:
            #print("error accepting connections")
            pass

#2 thread functions - 1) see all the clients 2) select a client 3) send comand to the cconnected client
# interactive promp for sending commands

def Game():
    global start
    global Act_board
    global pila
    global Board
    global turno
    global list_players
    global Baraja
    if start == True:
        Baraja = Deck()
        for x in list_players:
            for y in range (0,6):
                x.set_cards(Baraja.pop_card())
        Cen_Card = Baraja.pop_card()
        pila.append(Cen_Card)
        Act_board = False

    while True:
        if Act_board == False:
            Board.set_lPlayers = list_players
            Board.set_turno = turno
            Board.set_cenCard = pila[-1]
            for x in range(0, len(all_connections)):
                msg = ServerMessage(0,Board)
                send_obj(all_connections[x], msg)
            Act_board = True


#create worket thread
def create_workers():
    for _ in range(NUM_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        x = queue.get()
        #para manejar las conexiones nuevas
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connection()
        #si se envio una carta
        if x == 2:
            Game()


def create_jobs():
    for x in JOB_NUM:
        queue.put(x)
    queue.join()

def jugador(coneccion, i):
    global start, all_connections
    global Baraja
    global Act_board
    global pila
    global Board
    global turno
    orden = i
    while True:
        #print("player " + str(var))
        #time.sleep(2)
        data = recv_obj(coneccion)
        if data.get_tipo() == 0:
            game_logic()
        if data.get_tipo() == 1:
            for x in range(0, len(all_connections)):
                msg = ServerMessage(2,list_players[x].name + " : " + data.get_content)
                send_obj(all_connections[x], msg)
        if data.get_tipo() == 2:
            carta = Baraja.pop_card()
            list_players[orden-1].cards.append(carta)
            msg = ServerMessage(3,carta)
            send_obj(coneccion, msg)
            Act_board = False
        if data.get_tipo() == 3:
            list_players[orden-1].game = data.get_content()
        if data.get_tipo() == 4:
            list_players[orden-1].name = data.get_content()
        if data.get_tipo() == 5:
            start = True

def game_logic():
    pass

#con este podemos enviar objetos a otros clientes
def send_obj(conn,o):
    #print("a")
    obj = pickle.dumps(o)
    #print("b")
    obj = bytes(f"{len(obj):<{HEADERSIZE}}", 'utf-8') + obj
    #print("c")
    conn.send(obj)
    #print("d")

#con esta funcion podemos recibir objetos que nos manden
def recv_obj(conn):
    obj = conn.recv(1024)
    obj = pickle.loads(obj[HEADERSIZE:])
    return obj

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
        print(len(self.cards))

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

create_workers()
create_jobs()




