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
        cards = [
            (1,'b','0'),(2,'b','1'),(2,'b','2'),(2,'b','3'),(2,'b','4'),(2,'b','5'),
            (2,'b','6'),(2,'b','7'),(2,'b','8'),(2,'b','9'),(2,'b','+2'),(2,'b','skip'),
            (2,'b','reverse'),(2,'b','+2'),

            (1, 'r', '0'), (2, 'r', '1'), (2, 'r', '2'), (2, 'r', '3'), (2, 'r', '4'), (2, 'r', '5'),
            (2, 'r', '6'), (2, 'r', '7'), (2, 'r', '8'), (2, 'r', '9'), (2, 'r', '+2'), (2, 'r', 'skip'),
            (2, 'r', 'reverse'), (2, 'r', '+2'),

            (1, 'y', '0'), (2, 'y', '1'), (2, 'y', '2'), (2, 'y', '3'), (2, 'y', '4'), (2, 'y', '5'),
            (2, 'y', '6'), (2, 'y', '7'), (2, 'y', '8'), (2, 'y', '9'), (2, 'y', '+2'), (2, 'y', 'skip'),
            (2, 'y', 'reverse'), (2, 'y', '+2'),

            (1, 'g', '0'), (2, 'g', '1'), (2, 'g', '2'), (2, 'g', '3'), (2, 'g', '4'), (2, 'g', '5'),
            (2, 'g', '6'), (2, 'g', '7'), (2, 'g', '8'), (2, 'g', '9'), (2, 'g', '+2'), (2, 'g', 'skip'),
            (2, 'g', 'reverse'), (2, 'g', '+2'),

            (4,'m','wild'),
            (4,'m','+4'),

        ]
        for card in cards:
            for amount in range(card[0]):
                c = Card(card[1],card[2])
                print(card[1],card[2],' was added')
                self.add_card(c)


d = Deck()
d.populate()


# TODO: create socket, create player list, state and so on
class Game:
    def __init__(self):
        self.max_players = 10
        self.on_going = True
        self.winner = "No winner"
