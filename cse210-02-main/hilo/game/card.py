import random

class Card:
    def __init__ (self):
        self.value = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    def see_card (self):
        card_number = random.choice(self.value)

        return card_number