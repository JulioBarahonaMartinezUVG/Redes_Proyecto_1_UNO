#server
# estos son los imports que necesitamos para el funcionamiento del server
import socket
import sys
import pickle
import threading
import time
from queue import Queue
#numero de threads
NUM_OF_THREADS = 3
#la cantidad de trabajos en los threads
JOB_NUM = [1,2,3]
#nuestro Queue de tareas
queue = Queue()
#la lista de jugadores conectados
all_connections = []
#la lista de direcciones
all_addres = []
#no se para que servia esta variable
HEADERSIZE = 10
turno = 0
start = False
Board = False
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
    #en este for se encarga de cerrar todas las conexiones
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addres[:]
    #Aqui se realizan todas conexiones de multiples servers
    while True:
        try:
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
            print(p1)
            send_obj(conn, p1)
        except:
            #print("error accepting connections")
            pass

#2 thread functions - 1) see all the clients 2) select a client 3) send comand to the cconnected client
# interactive promp for sending commands

def Game():
    if start == True:
        while True:
            #recibe una carta
            indef = recv_obj
            #comprueba si es una carta
            if indef.__name__ == "card":
                #activa variable para actualizar el board al final del turno para todos los jugadores
                Board = True

            if Board == True:
                Board = False


#manejando el chat
def handle_chat():
    if start == True:
        while True:
            mesage = recv_obj()
            if mesage.__name__ == "msg":
                for x in range(0, len(all_connections)-1):
                    if x != mesage.numPlayer-1:
                        send_obj(all_connections[x], mesage)



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
        #si se envio un mensaje
        if x == 3:
            handle_chat()

def create_jobs():
    for x in JOB_NUM:
        queue.put(x)
    queue.join()

def actualizar_Board():
    pass

#con este podemos enviar objetos a otros clientes
def send_obj(conn,o):
    print("a")
    obj = pickle.dumps(o)
    print("b")
    obj = bytes(f"{len(obj):<{HEADERSIZE}}", 'utf-8') + obj
    print("c")
    conn.send(obj)
    print("d")

#con esta funcion podemos recibir objetos que nos manden
def recv_obj(conn):
    obj = conn.recv(1024)
    obj = pickle.loads(obj[HEADERSIZE:])
    return obj

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

    # creates the amounts of cards needed to play
    def populate(self):
        import random
        spade = "♠"\
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

class msg:
    def __init__(self, numPlayer, mensaje):
        self.numPlayer = numPlayer #numero del jugador que envia el mensaje
        self.mensaje = mensaje #mensaje a contener

# sets card value and color
class Card:
    def __init__(self, color, value):
        self.color = color # rojo, azul, verde, amarillo, multicolor
        self.value = value # 0-9, skip, reverse, +2, +4, change

    def get_color(self):
        return self.color

    def get_value(self):
        return self.value


create_workers()
create_jobs()
'''
#Establish connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print("connection has been established |" + "IP " + address[0] + " |PORT" + str(address[1]))
    game(conn)
    conn.close()

#Here where the server logic should start
def game(conn):
    conn.send(str.encode("te has conectado al server"))
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")
'''



