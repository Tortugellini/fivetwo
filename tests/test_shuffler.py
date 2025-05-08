import numpy as np

from src.deck import Deck
from src.shuffler import Shuffler

NUM_CARDS = 36
NUMBER_OF_SHUFFLES = 1
NUMBER_OF_PILES = 6


def get_deck(n: int, preshuffled: bool = False) -> Deck:
    """
    Defines and returns a Deck object with n cards in it.
    """

    deck = Deck(n, preshuffled=preshuffled)

    return deck


# TODO Will do when mash_shuffle is fixed.
# def test_mash_shuffle():
#     """
#     A simple test to see if "Mash Shuffle" actually shuffles the deck.

#     #TODO Improve this to be a more granular test.
#     """

#     deck = get_deck(NUM_CARDS)
#     original_cards = deck.cards

#     shuffler = Shuffler(NUMBER_OF_SHUFFLES)

#     shuffler.mash_shuffle(deck)
#     shuffled_cards = deck.cards

#     assert not (original_cards - shuffled_cards == 0).all()


def test_pile_shuffle():
    """
    A simple test to see if "Pile Shuffle" actually shuffles the deck.

    #TODO Improve this to be a more granular test.
    """

    deck = get_deck(NUM_CARDS)
    original_cards = deck.cards

    shuffler = Shuffler(NUMBER_OF_SHUFFLES)
    shuffler.pile_shuffle(deck, NUMBER_OF_PILES)
    shuffled_cards = deck.cards

    assert not (original_cards - shuffled_cards == 0).all()


def test_remember_shuffle():
    """
    Tests that the shuffler decorator '_remember_shuffle' properly updates the deck's
    'memory.'
    """

    deck = get_deck(NUM_CARDS)

    shuffler = Shuffler(NUMBER_OF_SHUFFLES)
    shuffler.pile_shuffle(deck, NUMBER_OF_PILES)

    assert deck.shuffle_history == {"pile_shuffle": 1}
