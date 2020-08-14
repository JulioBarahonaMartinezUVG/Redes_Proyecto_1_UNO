from easygui import *
from language_pack import *
from Modelos import *

hosts_list=[
    4000,
    4001,
    4002,
    4003,
    4004]
available_hosts=[
    4000,
    4001,
    4002,
    4003,
    4004
]
full_hosts=[

]

def user_help(lang):
    display = user_messages[lang]['main_menu_choice']
    user_help_flag = True
    while user_help_flag:
        help_choice = buttonbox(
            msg= display,
            title='SOS',
            choices=[
                '+2',
                '+4',
                'R',
                'S',
                'W',
                'UNO!',
                'Stack',
                user_messages[lang]['quit']
            ]
        )
        if help_choice == '+2':
            display= user_messages[lang]['help_+2']
        if help_choice == 'R':
            display= user_messages[lang]['help_reverse']
        if help_choice == '+4':
            display= user_messages[lang]['help_+4']
        if help_choice == 'S':
            display= user_messages[lang]['help_skip']
        if help_choice == 'W':
            display= user_messages[lang]['help_wild']
        if help_choice == 'UNO!':
            display= user_messages[lang]['help_uno']
        if help_choice == 'Stack':
            display= user_messages[lang]['help_stack']

        if help_choice == user_messages[lang]['quit']:
            user_help_flag = False

# crea un lobby de uno de los 5 designados
def create_lobby(lang):
    if available_hosts:
        host_address = available_hosts[0]
        del available_hosts[0]
        msgbox(
            title='Lobby ' + str(host_address),
            msg = user_messages[lang]['waiting_for_players'],
            ok_button=user_messages[lang]['try_start_game']
        )

        # check if lobby is ready
        if True:
            startGame(port_number=host_address)
        else:
            msgbox(
                title='Lobby ' + str(host_address),
                msg=user_messages[lang]['not_enough_players'],
            )
    else:
        msgbox(user_messages[lang]['no_server'])

def join_lobby(lang):
    options = []
    for i in hosts_list:
        if i not in available_hosts and i not in full_hosts:
            options.append(str(i))
    choices = options
    choice = buttonbox(
        msg=user_messages[lang]['pick_a_lobby'],
        choices=options)

def startGame(port_number):
    print(str(port_number),'game her')
