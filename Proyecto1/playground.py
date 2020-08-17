from sub_gui_elements import *
import socket

def player_chat(port,username):
    msg = "Maximo de 50 caracteres"
    title = "Chat sala: "+ str(port)
    fieldNames = [username + ':']
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg,title, fieldNames)

    while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
          if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
        if errmsg == "": break # no problems found
        fieldValues = enterbox(errmsg, title, fieldNames, fieldValues)
    print('En chat ' + str(port)+ " " + str(username) + ' dijo:', fieldValues[0])

def player_hand(cards):
    options=[]
    for i in cards:
        print(i)
        options.append(str(i))

    options.append('Jalar Carta')
    options.append('Pasar turno')
    options.append('Enviar')
    options.append('Leer')

    choice = buttonbox(
        msg='Que opcion se va a usar?',
        title='UNO',
        choices=options
    )

    if choice == 'chat':
        player_chat(port=123, username='Julio')

    if choice == 'chat':
        player_chat(port=123, username='Julio')

# player_hand(cards=[1,2,3,4])
#
# msg ="What is your favorite flavor?"
# title = "Ice Cream Survey"
# choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
# choice = choicebox(msg, title, choices)

# create_lobby('Español')


player_hand(['','','',])
#
# value = "+2"
# symbol = "♦"
#
#
# '|--------|\n' +
# '| ' + value + ' ' + symbol + ' |\n' +
# '|--------|'

jugadores= ['julio','jump','luis']

for i in range(7):
    for j in jugadores:
        print('carta #' , str(i+1) , ' para jugador ', str(j))
