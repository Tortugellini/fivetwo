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

    def __init__(self, number_of_cards, preshuffled=False):
        """
        Initializes a 'Deck' that is 'number_of_cards' large.

        If 'preshuffled' is True, the array is filled with random integers
        from 1 to 'number_of_cards' which represent (non-Pythonic) indices
        of the cards' location in an ordered (non-random) deck.
        ---
        Parameters:

        """

        # Holding on to the parameters passed.
        self.number_of_cards = number_of_cards
        self.preshuffled = preshuffled

        # Constructing the deck.
        if preshuffled:
            _cards = []

            while len(_cards) != number_of_cards:
                rand_ind = random.randint(1, number_of_cards)
                if rand_ind not in _cards:
                    _cards.append(rand_ind)
            self.cards = np.asarray(_cards)
        else:
            self.cards = np.linspace(1, number_of_cards, number_of_cards, dtype=int)

        # Making a copy of the deck to remember what it looked like before it was shuffled.
        self.original_state = self.cards

        # Remembering which shuffle methods were used on the Deck.
        self.shuffle_history = {}

        # Keeping track of how much the indices of the cards moved with each shuffle.
        self.index_movement = {}
