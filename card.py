class Card:

    def __init__(self,number,suit):
        self.number = number 
        self.suit = suit 

    #only called when text representation is needed 
    def __str__(self):
        return f"{self.number} of {self.suit}" 

