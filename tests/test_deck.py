import numpy as np

from src.deck import Deck

NUM_CARDS = 80


def get_deck(n: int, preshuffled: bool = False) -> Deck:
    """
    Defines and returns a Deck object with n cards in it.
    """

    deck = Deck(n, preshuffled=preshuffled)

    return deck


def test_number():
    """
    Tests the type of the deck.
    """

    assert get_deck(NUM_CARDS).number_of_cards == NUM_CARDS


def test_if_ordered_upon_request():
    """
    Tests that the deck is ordered if requested.
    """

    preshuffled = False

    deck = get_deck(NUM_CARDS, preshuffled=preshuffled)
    cards = deck.cards

    assert (cards - np.linspace(1, NUM_CARDS, NUM_CARDS) == 0).all()


def test_if_not_ordered_upon_request():
    """
    Tests that the deck is not ordered if not requested.
    """

    preshuffled = True

    deck = get_deck(NUM_CARDS, preshuffled=preshuffled)
    cards = deck.cards

    assert not (cards - np.linspace(1, NUM_CARDS, NUM_CARDS) == 0).all()
