"""
This code provides a class that acts as a human shuffler for a Deck (class) of cards
that is represented by an array of numbers.
"""

__author__ = "Collin Crites"
__creation_date__ = "2024-06-14"

import numpy as np
import random

from typing import Callable


class Shuffler:
    """
    A class used to apply operations on another class called Deck.
    """

    def __init__(self, number_of_shuffles: int):
        """Initializing the 'Shuffler' with the number of times the 'Deck' will be shuffled."""

        self.number_of_shuffles = number_of_shuffles
        self.remaining_shuffles = number_of_shuffles

    def _remember_shuffle(func: Callable):
        """
        Adds the name of the shuffle technique used and number of times it has been used
        to a list in the 'Deck' class to keep a memory of the shuffle techniques used on
        the 'Deck'.

        Is used as a decorator for the shuffle methods below.
        ---
        Parameters:
            func, function: The shuffle technique used on the deck.
        """

        def _wrapper(*args):
            """
            A _wrapper function used to pass the decorator arguments.
            """

            from fivetwo.deck import Deck

            # Finding the 'Deck' object in the passed arguments.
            for arg in args:
                if isinstance(arg, Deck):
                    deck = arg

            # Updating the shuffle history with the name of the shuffle method used.
            try:
                deck.shuffle_history[" ".join(func.__name__.split("_"))] += 1
            except KeyError:
                deck.shuffle_history[func.__name__] = 1

            return func(*args)

        return _wrapper

    def _card_displacements(self, deck: object):
        """
        Calculates how far each card traveled from its original position.
        Required for visualizing the distribution of the shuffle.
        ---
        Parameters:
            deck, object: The Deck object representing the deck of cards.
        """

        original_bins = {
            number: list(deck.original_state).index(number)
            for number in deck.original_state
        }
        shuffled_bins = {
            number: list(deck.cards).index(number) for number in deck.cards
        }
        shuffled_bins = {_[0][0]: _[0][1] for _ in sorted(zip(shuffled_bins.items()))}

        index_movement = abs(
            np.array(list(original_bins.values()))
            - np.array(list(shuffled_bins.values()))
        )
        deck.index_movement = dict(zip(list(shuffled_bins.keys()), index_movement))

    @_remember_shuffle
    def mash_shuffle(self, deck: object):
        """
        The deck of cards is split at some randomly chosen index 'n' leaving
        a pile of 'n' cards in stack 'A' and 'self.number_of_cards - n' in
        stack 'B'.
        The two stacks are then combined at an index 'm' of stack 'A'.

        # TODO BROKEN! Fix this method!
        ---
        Parameters:
            deck, object: A deck of cards of variable length.
        """

        # Choosing where to split the deck.
        n = random.choice(
            np.linspace(1, len(deck.cards) - 1, len(deck.cards) - 1, dtype=int)
        )

        # Splitting the deck into two stacks.
        _stackA = deck.cards[:n]
        stackB = deck.cards[n:]

        # Recreating 'stackA' with enough space for space to insert all of stackB
        stackA = np.full(2 * len(_stackA), np.nan)
        stackA[::2] = _stackA

        # Choosing the value of 'm'.
        m = int(random.choice(np.linspace(1, len(stackA) - 1, len(stackA) - 1)))

        # Inserting 'stackB' into 'stackA' at index 'm'.
        if len(stackB) > len(stackA[m:]):

            # Adding each card from stackB to stackA.
            for i, value in enumerate(stackA[m:]):
                if np.isnan(value):
                    stackA[m + i] = stackB[i]

            # Adding the rest of the cards at the end of 'stackA'.
            stackA = np.append(stackA, stackB[i:])
        else:

            for j, value in enumerate(stackB):
                if np.isnan(stackA[m + j]):
                    try:
                        stackA[m + j] = value
                    except IndexError:
                        break

        # Removing all 'nan's that remain.
        mask = np.isnan(stackA)
        stackA = stackA[~mask]

        # "Returning" the deck.
        deck.cards = np.asarray(stackA, dtype=int)

        # Calculating how far each card moved from its original position.
        self._card_displacements(deck)

    @_remember_shuffle
    def pile_shuffle(self, deck: object, number_of_piles: int):
        """
        Shuffles the deck by putting them into 'number_of_piles' piles and
        sequentially placing a card in each pile.

        The deck is then reconstructed by placing piles on top of each other
        until all the piles have been stacked together.
        ---
        Parameters:
            deck, object: A deck of cards of variable length.
            number_of_piles, int, np.array: The number of piles that the deck will be split
                                            into. If an array is provided then the stacks
                                            will be uneven by design.
        """

        # Getting the cards from the deck.
        cards = deck.cards

        # Shuffling the cards into 'number_of_piles' equally sized stacks.
        if isinstance(number_of_piles, int) and (len(cards) % number_of_piles == 0):
            array_stacks = np.split(cards, indices_or_sections=number_of_piles)
            randomized_cards = np.split(
                np.vstack(array_stacks),
                indices_or_sections=len(cards) / number_of_piles,
                axis=1,
            )
            random.shuffle(randomized_cards)  # Randomly stacking the piles.
            cards = np.array(randomized_cards).flatten()

        # Shuffling the cards into unequally sized stacks.
        else:
            pass  # TODO Add feature for choosing neither 9 or 11 stacks.

        # Updating the deck.
        deck.cards = cards

        # Calculating how far each card moved from its original position.
        self._card_displacements(deck)
