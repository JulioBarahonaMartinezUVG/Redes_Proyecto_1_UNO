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
HEADER_SIZE = 10
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
        s.listen(10)
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
            #confirma la conexion
            conn, address = s.accept()
            s.setblocking(1) #prevents timeout
            conn.send(str.encode("te has conectado al server"))
            all_connections.append(conn)
            all_addres.append(address)

            print("connection has been established: " + address[0])
        except:
            print("error accepting connections")

#2 thread functions - 1) see all the clients 2) select a client 3) send comand to the cconnected client
# interactive promp for sending commands

def start_Game():

    while True:
        '''
        cmd = input("player mensaje: ")
        if cmd == 'quit':
            #conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            #conn.send(str.encode(cmd))
            #client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")
            '''

#create worket thread
def create_workers():
    for _ in range(NUM_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connection()
        #si se envio una carta
        if x == 2:
            start_Game()
        #si se envio un mensaje

def create_jobs():
    for x in JOB_NUM:
        queue.put(x)
    queue.join()

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

#con este podemos enviar objetos a otros clientes
def send_obj(conn,carta):
    obj = pickle.dumps(carta)
    print(obj)
    obj = bytes(f'{len(obj):<{HEADER_SIZE}}', "utf-8") + obj
    conn.send(obj)
#con esta funcion podemos recibir objetos que nos manden
def recv_obj(conn):
    carta = conn.recv(1024)
    carta = pickle.loads(carta)
    print(carta)
'''