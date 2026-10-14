from card import Card 
import random 

class Deck:

    def __init__(self):
        self.deck = []
        self.create_deck()

    def create_deck(self):
        numbers = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        suits = ["SPADE","CLOVER","HEART","DIAMOND"]

        for i in numbers:
            for j in suits:
                self.deck.append(Card(i,j))

    #shuffles deck 
    def shuffle(self):
        random.shuffle(self.deck)


    def deal(self):
        return self.deck.pop()
    
        