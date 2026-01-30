"""
write a programme taht answer : 
- What is the expected number of cards you need to draw from a 52-card deck before you see the first ace?
"""

import random
from typing import Tuple 
from itertools import product 

suits = [
    "S", # spades => pic 
    "C" ,# clubs =>  traife 
    "D" , # Diamonds 
    "H" , # Hearts  => coeur 
]

ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Deck : 
    def __init__(self) -> None:
        self.cards = [
            (rank , suit) for rank , suit in product(ranks , suits)
        ]
    
    def shuffle(self) -> None : 
        self.cards = random.sample(self.cards , len(self.cards))

    def draw(self) -> Tuple[str , str]:
        """Draw a card from the deck"""
        return self.cards.pop()
    
    def isEmpty(self) -> bool : 
        """check if the deck has a card"""
        return len(self.cards) == 0


def simulation() -> int  :

    deck : Deck  = Deck()
    deck.shuffle()
    nb = 0 
    while not deck.isEmpty() : 
        rank , suit = deck.draw()
        nb += 1 
        if rank == "A" : 
            return nb 
    return nb 

N = 100_000
cards_sim = [simulation() for _ in range(N)]
print(sum(cards_sim) / len(cards_sim))
print(f"exc_ is : {48/5 + 1}")