# all the Variables that are going to be used
# TODO: add more
class Player:
    def __init__(self, name):
        self.name = name
        self.in_game = False

    def get_name(self):
        return self.name

#deck
# TODO: pupolate later
class Deck:
    def __init__(self):
        pass

# sets card value and color
class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def get_color(self):
        return self.color

    def get_value(self):
        return self.value

