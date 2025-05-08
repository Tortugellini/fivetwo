import numpy as np
import random

from src.deck import Deck
from src.stats import Statistics


NUM_CARDS = 42


def test_empty_probability():
    """
    Tests if 'Statistics' will properly add a 'displacement' key and value pair to the
    empty 'probabilities' dictionary.
    """

    statistician = Statistics()

    # Making a list of one random number as a dummy 'displacements' list.
    random_number = random.randint(1, 52)
    dummy_displacements = [random_number]

    probabilities = statistician._calculate_probabilities(dummy_displacements)

    assert probabilities == {random_number: 1}


def test_incrementing_probabilities():
    """
    Tests if 'Statistics' will properly increment the probability values of each
    'displacement' value.
    """

    statistician = Statistics()

    # Making a list of one random number as a dummy 'displacements' list.
    random_number_one = random.randint(1, 50)
    random_number_two = random.randint(51, 52)
    dummy_displacements = [random_number_one, random_number_one, random_number_two]

    probabilities = statistician._calculate_probabilities(dummy_displacements)

    assert probabilities == {random_number_one: 2.0 / 3, random_number_two: 1.0 / 3}


def test_mask_creation():
    """
    Tests that the mask method properly makes a mask.
    """

    statistician = Statistics()

    dummy_array = np.linspace(1, 52, 52)

    displacements = np.abs(dummy_array - 23)

    mask = statistician._differences_greater_than_zero(displacements)
    not_mask = ~mask

    # Checking for the 1 True at '23' because that's the only value in 'displacements' not greater than 0.
    assert not_mask.any()


# TODO Test 'shannon_entropy' method.
