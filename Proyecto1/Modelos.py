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
