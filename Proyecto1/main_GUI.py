#!/usr/bin/env python3
from sub_gui_elements import *
on = True

#lang choice
languague = buttonbox(
    choices=['Español', 'English']
)

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
        image="main_menu.png",
        msg=user_messages[languague]['main_menu_choice'],
        title='UNO',
        choices=[
            user_messages[languague]['join_game'],
            user_messages[languague]['create_game'],
            user_messages[languague]['help'],
            user_messages[languague]['swap'],
            user_messages[languague]['quit']
        ]
    )

    if choice == user_messages[languague]['join_game']:
        pass

    if choice == user_messages[languague]['create_game']:
        pass

    print(choice)
    if choice == user_messages[languague]['help']:
        user_help(languague)

    #user changes language
    if choice ==  user_messages[languague]['swap']:
        languague =  user_messages[languague]['swap']

    #user quits
    if choice == user_messages[languague]['quit']:
        on = False
