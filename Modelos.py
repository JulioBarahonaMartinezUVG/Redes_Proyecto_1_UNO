# here are the objects that we are using

#default player object
class Player:
    def __init__(self, name):
        self.name = name
        self.game = ""

    #when called returns the player name
    def get_name(self):
        return self.name

    #sets the player to an
    def set_game(self, gameAddress):
        self.game = gameAddress

# sets card value and color
class Card:
    def __init__(self, color, value):
        self.color = color # rojo, azul, verde, amarillo, multicolor
        self.value = value # 0-9, skip, reverse, +2, +4, change

    def get_color(self):
        return self.color

    def get_value(self):
        return self.value

#When a game starts a deck is assigned
# TODO: shuffle cards and return card
class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, Card):
        self.cards.append(Card)

    def populate(self):
        import random
        # order goes
        # (amount_of_cards, color (blue,red,yellow,green), simbol{s=skip, r = reverse, w=wild})
        cards = [
            (1,'b','0'),(2,'b','1'),(2,'b','2'),(2,'b','3'),(2,'b','4'),(2,'b','5'),
            (2,'b','6'),(2,'b','7'),(2,'b','8'),(2,'b','9'),(2,'b','+2'),(2,'b','s'),
            (2,'b','r'),

            (1, 'r', '0'), (2, 'r', '1'), (2, 'r', '2'), (2, 'r', '3'), (2, 'r', '4'), (2, 'r', '5'),
            (2, 'r', '6'), (2, 'r', '7'), (2, 'r', '8'), (2, 'r', '9'), (2, 'r', '+2'), (2, 'r', 's'),
            (2, 'r', 'r'),

            (1, 'y', '0'), (2, 'y', '1'), (2, 'y', '2'), (2, 'y', '3'), (2, 'y', '4'), (2, 'y', '5'),
            (2, 'y', '6'), (2, 'y', '7'), (2, 'y', '8'), (2, 'y', '9'), (2, 'y', '+2'), (2, 'y', 's'),
            (2, 'y', 'r'),

            (1, 'g', '0'), (2, 'g', '1'), (2, 'g', '2'), (2, 'g', '3'), (2, 'g', '4'), (2, 'g', '5'),
            (2, 'g', '6'), (2, 'g', '7'), (2, 'g', '8'), (2, 'g', '9'), (2, 'g', '+2'), (2, 'g', 's'),
            (2, 'g', 'r'),

            (4,'m','w'),
            (4,'m','+4'),

        ]
        for card in cards:
            for amount in range(card[0]):
                c = Card(card[1],card[2])
                self.add_card(c)

        print('general kenobi')
        s = random.sample( cards, len(cards) )
        # print(cards)
        # print(s)

    def shuffle_Deck(self):
        cards = self.cards
        print(type(cards[0]))

# d = Deck()
# d.populate()
# d.shuffle_Deck()

#each session is definned here
class Game:
    def __init__(self, address_input):
        self.max_players = 10
        self.players = []
        self.state = ''
        self.winner = "No winner"
        self.address = address_input

    def get_address(self):
        return self.address

    def get_players(self):
        return self.players()
