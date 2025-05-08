"""
This code analyzes the statistics of the shuffles.
"""

__author__ = "Collin Crites"
__creation_date__ = "2024-06-15"

import numpy as np


class Statistics:
    def __init__(self):
        self.probabilities = {}
        self.entropy = 0

    @staticmethod
    def _differences_greater_than_zero(displacements):
        """
        Creates a mask of the displacements that are greater than 0.
        """

        mask = np.array(list(displacements)) > 0

        return mask

    def _calculate_probabilities(self, displacements):
        """
        A simple calculation that calculates the probability of a card being moved by any of the values
        in the 'displacements' list through a frequentist approach.
        ---
        Parameters:
            displacements, list: The list of displacements between the indices of the cards in the deck.
        ---
        Returns: A dictionary of the probabilities of each value in the 'difference' list.
        """

        probabilities = {}
        for diff in displacements:
            try:
                probabilities[diff] += 1.0 / len(displacements)
            except KeyError:  # Initializes the movement value.
                probabilities[diff] = 1.0 / len(displacements)

        return probabilities

    def shannon_entropy(self, deck):
        """
        Calculates the Shannon Entropy of the cards in their new arrangement using their
        original bin numbers.
        ---
        Parameters:
            deck, object: The deck being shuffled.
        """

        displacements = np.array(list(deck.index_movement.values()))
        differences_greater_than_zero = displacements[
            self._differences_greater_than_zero(displacements)
        ]

        # Calculating the percentages of occurence for ecah value in the list of differences.
        self.probabilities = self._calculate_probabilities(
            differences_greater_than_zero
        )

        # Calculating the entropy from this list.
        self.entropy = -1 * sum(
            np.array(list(self.probabilities.values()))
            * np.log10(list(self.probabilities.values()))
        )

        return self.entropy
