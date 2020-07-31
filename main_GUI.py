#!/usr/bin/env python3
from easygui import *
from language_pack import *
on = True

#lang choice
languague = buttonbox(choices=['Español', 'English'])

#welcome message
msgbox('"UNO" '
       '\n Julio Barahona 141206'
       '\n Luis Delgado 17187'
       '\n Josue Lopez 17081'
       ,title=user_messages[languague]['title'],
       image='uno.png')


while on:
    #main instrucions
    choice = buttonbox(
        msg=user_messages[languague]['main_menu_choice'],
        title='Main menu ',
        choices=[
            user_messages[languague]['join_game'],
            user_messages[languague]['create_game'],
            user_messages[languague]['help'],
            user_messages[languague]['swap'],
            user_messages[languague]['quit']
        ]
    )

    print(choice)
    if choice == user_messages[languague]['help']:
        pass

    #user changes language
    if choice ==  user_messages[languague]['swap']:
        languague =  user_messages[languague]['swap']

    #user quits
    if choice == user_messages[languague]['quit']:
        on = False

    # image = "uno.png"
    # msg = "Do you like this picture?"
    # choices = ["Yes", "No", "No opinion"]
    # reply = buttonbox(msg, image=image, choices=choices, width= 480
    #            , height= 320)



    #Exit option
    # msg = "Do you want to continue?"
    # title = "Please Confirm"
    # if ccbox(msg, title):  # show a Continue/Cancel dialog
    #     pass
    # else:  # user chose Cancel
    #     on = False
