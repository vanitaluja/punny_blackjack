"""Tests for my functions that don't require user inputs. """

# imports the 3 functions to test
from classes_and_functions import DeckOfCards, cards_value, pun_machine

def test_shuffle():
    """Tests the shuffle function. """
    
    deck = DeckOfCards()  # creates an instance of class DeckOfCards
    assert isinstance(deck.shuffle(3), list)  # checks that output is a list
    assert isinstance(deck.shuffle(3)[0], str)  # checks that list is of strings
    assert len(deck.shuffle(3)) == 3  # checks that input value returns that many cards
    
def test_cards_value():
    """Tests the cards_value function. """
    
    assert isinstance(cards_value(['6', '2']), int)  # checks that function returns an integer
    assert cards_value(['6', '2', '4']) == 12  # checks value for numeric cards
    assert cards_value(['A', '2', '4']) == 17  # checks value for cards with a normal ace
    assert cards_value(['A', 'K', '4']) == 15  # checks value for cards with a special case ace
    
def test_pun_machine():
    """Tests the pun_machine function. """
    
    assert isinstance(pun_machine(17), str)  # checks that function returns a string
    assert pun_machine(13) == 'The number 13? Not on my watch.'  # checks that pun is correctly assigned to total value

