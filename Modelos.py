# all the Variables that are going to be used
# TODO: add more
class Player:
    def __init__(self, name):
        self.name = name
        self.in_game = False

    def get_name(self):
        return self.name


# sets card value and color
class Card:
    def __init__(self, color, value):
        self.color = color # rojo, azul, verde, amarillo, multicolor
        self.value = value # 0-9, skip, reverse, +2, +4, change

    def get_color(self):
        return self.color

    def get_value(self):
        return self.value

# deck
# TODO: populate later
class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, Card):
        self.cards.append(Card)

    def populate(self):
        for i in range(108):
            c = Card('blue','0')
            self.add_card(c)

d = Deck()
d.add_card()


# TODO: create socket, create player list, state and so on
class Game:
    def __init__(self):
        self.max_players = 10
        self.on_going = True
        self.winner = "No winner"
