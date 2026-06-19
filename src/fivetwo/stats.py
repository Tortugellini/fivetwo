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
    def _differences_greater_than_zero(displacements: list):
        """
        Creates a mask of the displacements that are greater than 0.
        ---
        Parameters:
            displacements, list: The list of displacemenets between the indices of the cards in the deck.
        ---
        Returns:
            mask, np.array: A boolean array used to ignore all 0's in the 'displacements' list.
        """

        mask = np.array(list(displacements)) > 0

        return mask

    def _calculate_probabilities(self, displacements: list):
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

    def shannon_entropy(self, deck: object):
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

    def generate_histograms(self, deck: object, bins: int):
        """
        Generates histograms for each card position in the deck.
        ---
        Parameters:
            deck, object: The deck being shuffled.
            bins, int: The number of bins to use for the histogram.
        ---
        Returns:
            histograms, dict: A dictionary of histograms for each card position in the deck.
                              It is organized into a dictionary in case there are other shuffle
                              methods used.
        """

        histograms = {}
        for matrix in deck.shuffle_history.values():
            try:
                shape = matrix.shape[1]
                for position_in_deck in range(shape):
                    histograms[position_in_deck] = np.histogram(matrix[:, position_in_deck], bins=bins)[0]
            except IndexError:
                shape = matrix.shape[0]    
                for position_in_deck in range(shape):
                    histograms[position_in_deck] = np.histogram(matrix[position_in_deck], bins=bins)[0]
            
        return histograms
