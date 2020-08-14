from easygui import *
from language_pack import *

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
                'S',
                'W',
                'UNO!',
                'Stack',
                user_messages[lang]['quit']
            ]
        )
        if help_choice == '+2':
            display= user_messages[lang]['help_+2']
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

