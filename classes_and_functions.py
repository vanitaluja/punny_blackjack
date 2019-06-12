""" Classes and functions used in my project. """

# Classes:

import random

class DeckOfCards():
    """
    Creates a deck of cards with which to play. 
    For loop based on code found on StackExchange.
    """

    # creates a deck of cards with 4 of each type
    deck = ['A' ,'K' ,'Q' , 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'] * 4
    
    
    def shuffle(self, value):
        """Picks a certain number of cards randomly from the deck.
        
        Parameters
        ----------
        value : int
            Number of cards to randomly choose.
            
        Returns
        -------
        cards : list
            List of the random cards.
        """
        
        cards = []
        
        # choses a card randomly and puts it in the cards list
        # Citation: https://codereview.stackexchange.com/questions/194812/
        #     a-simple-blackjack-game-implementation-in-python
        for num in range(value):
            
            max_num = len(self.deck) - 1
            picked = random.randint(0,max_num)
            cards.append(self.deck[picked])
    
        # takes out the chosen card from the deck
        self.deck.pop(picked)
        
        return cards
        

class Player():
    """Creates a player with their own characteristics. """
    
    def __init__(self, name):
        """Gives each player a name, money, and a hand of cards, 
        and keeps track of the money they bet.
        
        Parameters
        ----------
        name : str
            Input name of player. 
        """
        
        self.name = name
        self.money = 500
        self.hand = []
        self.bet = 0


class Dealer():
    """Creates a dealer with a hand of cards against which players compete. 
    Also keeps track of the total money lost by the players."""
     
    def __init__(self):
        self.hand = []
        self.total_money = 0


# Functions: 

def player_names():
    """Asks for each players' name, creates an instance of Player for each, 
    and puts them in a list.
    
    Returns
    -------
    player_instances : list
        The list of all instances of players in the game.
        
    """
    
    player_instances = []
    keep_asking = True
    
    # continues to request new players' names as long as there are more
    while keep_asking == True:
        
        # asks for the player's name
        name = input('What is this player\'s name?: ')
        player_instances.append(Player(name))
        new_player = True
        
        # checks if there are more to be input
        while new_player == True:
            
            try:
                
                another = input('Is there another player?: ')
                
                # there is another player, so continues onto next player
                if another == 'Yes'or another == 'yes':

                    keep_asking = True
                    new_player = False
                
                # there are no more players, so ends loops
                elif another == 'No' or another == 'no':
                    
                    keep_asking = False
                    new_player = False
                 
                # unclear answer, so asks again
                else:
                    
                    raise Exception
                    
            except Exception:
                
                print('Whoops! Please print yes or no.')
                
    return player_instances
    
    
def bet(list_of_names, dealer):
    """
    Allows players to place bets.
    
    Parameters
    ----------
    list_of_names : list
        Previously defined player list from player_names function.
    dealer : instance of Dealer()
        An instance of the Dealer.
    
    """
    
    # asks each player for inital bets
    for person in list_of_names:
        
        valid = True
        
        while valid:
            
            try:
                
                person.bet = input('Player {}, place your initial bet: '.format(person.name))
                # takes bet away from personal money total
                person.money -= int(person.bet)
                
                # continues to next player if player has enough money for their bet
                if person.money >= 0:
                    
                    valid = False
                    
                # raises error if player bets more than they have
                elif person.money < 0:
                    
                    person.money = 500
                    raise Exception
                    
            # allows players to bet again if they tried to bet too much
            except Exception:
                
                print('Whoops! You only have 500 USD to start. Try again.')
            
        # gives all the money to the dealer
        dealer.total_money += int(person.bet)
                
    # shows money each player has
    print('\nRemaining Balances: \n')
    for person in list_of_names:
        
        print(person.name + ': ' + str(person.money) + ' USD')
        
    print('\n' + '*****' * 15)
        
        
def cards_value(hand):
    """
    Determines the numeric value of the current hand.
    
    Parameters
    ----------
    hand : list
        List of strings of cards player has.
        
    Returns
    -------
    total : int
        Sum of the values of each card in the hand.
        
    """
    
    # assigns numeric value to each card face
    values_of_cards = {'A': 11, 'K': 10, 'Q': 10, 'J': 10, '10': 10, 
                      '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    total = 0
    
    # sums values of all the cards in the hand
    for card in hand:
        
        this_value = values_of_cards[card]
        total += this_value
        
    # allows ace to have value 11 or 1
    if 'A' in hand and total > 21:
        total -= 10
        
    return total


def pun_machine(total):
    """
    Assigns puns to the different totals a hand can have.
    
    Parameters
    ----------
    total : int
        The sum of the card values in a given hand.
        
    Returns
    -------
    chosen_pun : str
        The pun associated with the input total.
    """
    
    # set of puns associated with most possible total values
    pun_dict = {4: 'Why didn\'t the two 4\'s feel like dinner? Because they already 8.',
                5: 'I got into a fight with 1, 3, 5, 7 and 9. The odds were against me.', 
                6: 'Why is 6 afriad of 7? Because 7 8 9.',
                7: 'How do you make 7 an even number? Take the s out!', 
                8: 'What did the 0 say to the 8? Nice belt.', 
                9: 'Why couldn\'t the German count to 10? Because he was stuck on nein.',
                10: 'Why is 10 afriad of 7? Because 7 8 9, and 10 is next.', 
                11: 'There was a murder. 2, 3, 5, 7 and 11 are the prime suspects.',
                12: 'Why can\'t a nose be 12 inches long? Because then it would be a foot.',
                13: 'The number 13? Not on my watch.',
                14: 'How does a blackjack dealer sneak about? He shuffles a round.', 
                15: 'How are 15 year old girls like their age? They can\'t even.', 
                16: 'Why can\'t you play blackjack in the wild? Because of all the cheetahs.', 
                17: 'To hit or not to hit, that is the question.', 
                18: '18 & 20 were playing a game of blackjack. Twenty one.', 
                19: '19 & 20 were playing a game of blackjack. Twenty one.',
                20: 'Why is 9 afraid of 20? Because twenty eight twenty nine\'s.',
                21: 'BLACKJACK!!', 
                22: 'Why did all the numbers laugh at 22 ? Because it had tu tu’s'}
    
    # chooses pun based on total value of hand
    chosen_pun = pun_dict[total]
    return chosen_pun