"""Script to run the game."""

import sys
sys.path.append('../')


# imports all the classes and fuctions needed to run the script
from my_module.classes_and_functions import DeckOfCards, Player, Dealer
from my_module.classes_and_functions import player_names, cards_value, bet, pun_machine


# fun introduction
initial_answer = input('WELCOME TO VANI\'S ZESTY GAME OF BLACKJACK. Are you ready to play?: ')
print('\nWonderful. Game on.',
     '\n' + '*****' * 15)

# allows players to play again
play_again = True
while play_again == True:
    
    # creates instances of a deck of cards and a dealer, then starts the game
    total_hand = DeckOfCards()
    dealer = Dealer()
    squad = player_names()
    print('\nI am your dealer. This game is punny blackjack',
          '\nand your goal is to beat me. The stakes are high.',
          '\n' + '*****' * 15,
          '\n\nEach player begins with 500 USD.')

    # allows players to place bets
    bets = bet(squad, dealer)

    # starts with one random card face up for dealer
    dealer.hand = total_hand.shuffle(1)
    print('Dealer\'s first card: ' + str(dealer.hand))   

    # choses two random cards for each player and adds them to their hand
    print('\nPlayer\'s hands: \n')
    for person in squad:
        
        # puts cards in hand
        person.hand = total_hand.shuffle(2)
        print(person.name + ': ' + str(person.hand))
        
        # shows total value of hand
        total = cards_value(person.hand)
        print('   Your total is ' + str(total) + '.')
        
        # prints pun for each hand total, depending on the value
        try:
            
            print('\n The chosen pun for your hand --\n\t' + pun_machine(total),
                      '\n' + '*****' * 15 + '\n')
            
        except KeyError:
            
            print('\n' + '*****' * 15)

    
    remaining_players = []
    
    # goes through each player's turn
    for person in squad:
        
        repeat = True
        total = cards_value(person.hand)
        
        # checks to see if first two cards gave blackjack
        if total == 21:
            
            # adds gained money for winning
            person.money += int(person.bet)*2.5
            print('Hand: ' + str(person.hand) + '\t Total: ' + str(total))
            print('\nCongrats Player {}! You win! \
                You now have {} USD!'.format(person.name, person.money))
            
            # stops player's turn
            repeat = False
        
        # continues player's turn
        while repeat:
            
            # asks player to hit or pass
            again = input('Player ' + person.name + ', would you like to hit or pass? \
                \nYour current total is {}: '.format(total))
        
            if again == 'hit':
                
                # gives the player a new card and adds its value to their total
                new_card = total_hand.shuffle(1)
                person.hand.append(new_card[0])
                total = cards_value(person.hand)
                print('New hand: ' + str(person.hand) + '\t New total: ' + str(total))
            
            elif again != 'hit':
                
                # shows the player where they stand if they don't want a new card
                total = cards_value(person.hand)
                print('Current hand: ' + str(person.hand) + '\t Current total: ' + str(total))
                
                # ends player's turn
                break
                
            # prints pun for each hand total, depending on the value
            try:
                
                print('\n The chosen pun for your hand --\n\t' + pun_machine(total),
                      '\n' + '*****' * 15)
                
            except KeyError:
                
                print('\n' + '*****' * 15)
        
        
            # stops player's turn if they bust (get over 21)
            if total > 21:
                
                repeat = False
                print('\nSorry, your cards exceeded 21. '
                 'You\'re out. You leave today with {} USD.\n'.format(person.money))
            
            # stops player's turn if they get blackjack (exactly 21)
            elif total == 21:
                
                repeat = False
                person.money += int(person.bet)*2.5
                print('\nCongrats! You win! You now have {} USD!'.format(person.money))
                break
            
            # continues player's turn if they want to, and can hit again
            elif again == 'hit' and total < 21:
                
                continue
            
            # stops player's turn if they don't want to, but can hit again
            else:
                
                break
        
        # if player doesn't bust or get blackjack, 
        # adds player to list that will go against the dealer
        if again == 'pass':
            remaining_players.append(person)
        
        # creates a space between each player to make it easier to see
        print('\n')
    
    
    # checks if any players will face the dealer
    if bool(remaining_players):
        
        dealer_total = cards_value(dealer.hand)
    
        # gives dealer a random new card while their hand is less than 17
        while dealer_total < 17:
            
            new_card = total_hand.shuffle(1)
            dealer.hand.append(new_card[0])
            dealer_total = cards_value(dealer.hand)
            print('The dealer hits with a new hand of ' + str(dealer.hand),
                'and a total of ' + str(dealer_total) + '. \n' + '*****' * 15)
        
        # output if dealer gets blackjack
        if dealer_total == 21:
            
            print('The dealer has blackjack! {} goes to the house.'.format(dealer.total_money),
                 ' Better luck next time!')
        
        # output if dealer cannot hit anymore but doesn't get blackjack
        elif dealer_total >= 17 and dealer_total < 21:
            
            print('The dealer cannot hit again.')
            
            # checks if each player beat the dealer
            for person in remaining_players:
                
                total = cards_value(person.hand)
                
                # output if dealer beat player
                if dealer_total > total:
                    
                    print('Sorry Player {}, the dealer\'s cards',
                          'are higher than yours, you lose.'.format(person.name),
                         '\nYou leave today with {} USD.'.format(person.money))
                
                # output if player beat dealer
                elif dealer_total < total:
                    
                    person.money += int(person.bet) * 2
                    print('Player {} beat the dealer!'.format(person.name),
                    '\tYou win with {} USD.'.format(person.money))
                    
                # output for a push (player/dealer tie)
                else:
                    
                    print('Push! Player {} tied with the dealer.'.format(person.name),
                         '\tYou\'re balance returns to 500 USD.')
        
        # output if dealer busts
        elif dealer_total > 21:
            
            print('The dealer lost! \n\nWinners\' balances: \n')
            
            # gives each remaining player winning money
            for person in remaining_players:
                
                person.money += int(person.bet) * 2
                print(person.name + ': ' + str(person.money) + ' USD')
    
    # end if no players face the dealer
    else:
        print('The dealer leaves with {} USD.'.format(dealer.total_money),
              'Good game!')
        
    # allows players to play again
    final_answer = input('Type "again" if you would like a rematch: ')
    if final_answer == 'again':
        
        play_again = True
        
    else:
        
        # breaks loop to end game 
        play_again = False
        print('\nThanks for playing! See you next time!')