"""
Generates a deck of cards of user-defined length.
"""

__author__ = "Collin Crites"
__creation_date__ = "20240615"

import numpy as np
import random


class Deck:
    """
    A 'Deck' class represents a deck of cards as a np.array.

    TODO: Write more here later. Perhaps write out some example code.
    """

    def __init__(self, premade_deck: np.array, preshuffled: bool = False, number_of_cards: int | None = None):
        """
        Creates a Deck of cards with number values representing each card.

        If 'premade_deck' is True, uses the decklist provided as the deck.
        
        If 'preshuffled' is True, the array is filled with ranom integers from 1 to 'number_of_cards.'
        Must provide a value for 'number_of_cards' if 'preshuffled' is set to True.
        ---
        Parameters:
            premade_deck, np.array: A list of cards from a previously created deck.
            preshuffled, bool: Determines whether to create a randomly ordered deck of cards.
            number_of_cards, int: The number of cards to put in the created deck.
        """

        if list(premade_deck):
            self.cards = premade_deck
        
        elif preshuffled:
            self.preshuffled = preshuffled
            if number_of_cards:
                self.cards = self._preshuffled(number_of_cards)
            else:
                print("Please provide the size of the deck you would like to make.")
        else:
            if number_of_cards:
                self.cards = self._standard_deck(number_of_cards)
            else:
                print("Please provide the size of the deck you would like to make.")

        self.number_of_cards = len(self.cards)
        self.original_state = self.cards # Creating a copy of the deck to remember what it looked like before it was shuffled.
        self.shuffle_history = {} # Remembering which shuffle methods were used on the Deck.
        self.index_movement = {} # Keeping track of how much the indices of the cards moved with each shuffle. TODO: Might need to change this.
        self.entropy = 0 # A property of the deck that is utilized by the Stats object. TODO: Might remove. It's already a function of the Stats object, and the functionality works there.

    def _standard_deck(self, number_of_cards: int):
        """
        Creates a linearly ordered list of cards.
        """

        self.cards = np.linspace(1, number_of_cards, number_of_cards, dtype=int)

    def _preshuffled(self, number_of_cards: int):
        """
        Creates a randomly ordered list of cards.
        """

        _cards = []

        while len(_cards) != number_of_cards:
            rand_ind = random.randint(1, number_of_cards)
            if rand_ind not in _cards:
                _cards.append(rand_ind)

        self.cards = np.asarray(_cards)
