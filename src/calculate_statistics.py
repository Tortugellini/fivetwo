"""
This code analyzes the statistics of the shuffles 
"""

__author__ = "Collin Crites"
__creation_date__ = "2024-06-15"

import math
import numpy as np


class Statistics:
    def __init__(self):
        self.probabilities = {}
        self.entropy = 0

    def shannon_entropy(self, deck):
        """
        Calculates the Shannon Entropy of the cards provided using their original bin
        numbers.
        ---
        Parameters:
            deck, object: The deck being shuffled.
        """

        # Finding the places where there is a absolute difference greater than 0.
        differences_greater_than_one = np.array(list(deck.index_movement.values()))[
            np.array(list(deck.index_movement.values())) > 0
        ]

        # Calculating the percentages of occurence for ecah value in the list of differences.
        self.probabilities = self._calculate_probabilities(differences_greater_than_one)

        # Calculating the entropy from this list.
        self.entropy = -1 * sum(
            np.array(list(self.probabilities.values()))
            * np.log10(list(self.probabilities.values()))
        )

        return self.entropy

    def _calculate_probabilities(self, displacements):
        """
        Calculates the probabilities for each number in the list of displacements.
        ---
        Parameters:
            displacements, list: The list of displacements between the indices of the cards in the deck.
        ---
        Returns: A dictionary of the probabilities of each value in the 'difference' list.
        """

        probabilities = {}
        for diff in displacements:
            try:
                probabilities[diff] += 1 / len(displacements)
            except KeyError:
                probabilities[diff] = 1 / len(displacements)

        return probabilities


# Testing
if __name__ == "__main__":
    from deck import Deck
    from shuffling import Shuffler
    from calculate_statistics import Statistics

    deck = Deck(99)
    shuffler = Shuffler(1)

    deck.cards = shuffler.pile_shuffle(deck, 9)
    stats = Statistics()
    stats._card_displacements(deck)
    print(deck.index_movement)
