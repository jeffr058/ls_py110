# PEDAC
# Understand the Problem
# Inputs:
    # User starts the game, the deck of cards is initialized and shuffled, and dealer deals the cards
    # Dealer deals the cards
# Outputs:
    # The result of three possible outcomes: Player wins, Dealer wins, or it's a tie; resulting from Player choosing specific actions based on the cards Player is dealt and the card shown in the Dealer's hand
# Requirements:
    # Card values:
        # Cards 2-10 are worth their face values
        # Jack, Queen, King are worth 10 each
        # Ace is 1 or J depending on the total value of cards in hand when Ace is received
    # Player always goes first
    # Player can decide to "hit" or "stay"
    # Player can "hit" as many times as he wants
    # If total value exceeds 21 for either player, player "busts" and loses game
    # The turn is over when the player "busts" or "stays"
    # When the player "stays", it's the dealer's turn
    # Dealer must hit until total is at least 17
    # If dealer busts, player wins
    # When the player and dealer both "stay", the values are compared for the highest value

# Data Structure:
    # Probably dictionary or list or some combinations of the two
    # Option 1: a tuple or list of dictionaries
        # Each dictionary represents a suit, keys are cards, values are values
    # Option 2: a nested list (LS choice)
        # inner lists are [suit, card_value] 

# Algorithm:
    # 1. Initialize deck of cards
    # 2. Deal cards
    # 3. Calculate total value
    # 4. Check outcome
        # If total value is 21
            # If total value of Dealer cards is not 21, Player wins
            # If total value of Dealer cards 21, it's a tie
        # If total value is > 21, Player busts
        # If total value is < 21, continue to step 5
    # 5. Prompt Player to hit or stay
        # If Player stays, break loop
        # If Player hits
            # Deal a card to Player
        # Go to step 3
    # Dealer's turn to hit or stay
        # If value is < 17, Dealer hits until value is >= 17
    # If Dealer busts, Player wins
    # The card values are compared and winner determined
    # Player chooses whether to play again

# If hand includes Ace:
            # Ace is 11 by default
            # If sum w/ Ace is > 21, Ace becomes 1

# Calculate total value:
    # Given a hand of cards
    # Compute the total value of all the cards
        # Make a list of values
        # Set sum w/ 0
        # For each value in values, add the numeric value (from CARD_VALUES) to sum
        # Determine how many Aces in cards
            # While sum > 21 and more than one Ace in cards
            # Subtract 10 from sum
            # Subtract 1 from count of Aces
        # Return sum

# Deal cards:
    # Set player_hand to empty list
    # Set dealer_hand to empty list
    # Alternate dealing to Player and Dealer for 4 total cards
        # Take last card from deck and add to player_hand or dealer_hand
    # Return player_hand and dealer_hand

# Code:
import random
import os

CARD_VALUES = {
    '2': 2, 
    '3': 3, 
    '4': 4, 
    '5': 5, 
    '6': 6, 
    '7': 7, 
    '8': 8, 
    '9': 9, 
    '10': 10, 
    'J': 10, 
    'Q': 10, 
    'K': 10, 
    'A': 11,
}
STRING_VALUES = list(CARD_VALUES.keys())
SUITS = ('S', 'H', 'C', 'D')

def prompt(message):
    print(f'=> {message}')

def initialize_deck():
    deck = [[f'{string_value}', f'{suit}'] 
            for string_value in STRING_VALUES 
            for suit in SUITS]
    
    random.shuffle(deck)
    
    return deck

def deal_cards(deck):
    player_hand = []
    dealer_hand = []

    for num in range(4):
        if num % 2 == 0:
            player_hand.append(deck.pop())
        else:
            dealer_hand.append(deck.pop())

    return (player_hand, dealer_hand)

def total_value(cards):
    values = [card[0] for card in cards]
    current_sum = 0

    for value in values:
        current_sum += CARD_VALUES[value]

    ace_count = values.count('A')
    while current_sum > 21 and ace_count:
        current_sum -= 10
        ace_count -= 1

    return current_sum

def busted(total):
    return total > 21

def hit(hand, deck):
    hand.append(deck.pop())
    return hand

def determine_outcome(player_total, dealer_total):
    if player_total > 21:
        return 'Dealer'
    elif dealer_total > 21:
        return 'Player'
    elif player_total < dealer_total:
        return 'Dealer'
    elif player_total > dealer_total:
        return 'Player'
    else:
        return 'tie'

def display_winner(winner, player_total, dealer_total):
    outcome = winner
    print(f'Dealer has {dealer_total}. Player has {player_total}.')

    if outcome == 'tie':
        print("It's a tie!")
    else:
        print(f'{outcome} wins!')

def display_hand(hand):
        string_cards = [' of '.join(card) for card in hand]
        
        result = []
        for string_card in string_cards:
            result.append(f'[{string_card}]')

        print(' '.join(result))

def display_table(dealer_hand, player_hand, dealer_total, player_total, turn):
    os.system('clear')
    dealer_show_one = total_value([dealer_hand[0]])
    
    if turn == 'player':
        prompt('Dealer:')
        print(f'[{dealer_hand[0][0]} of {dealer_hand[0][1]}] [? of ?]')
        print()
        
        prompt('Player:')
        display_hand(player_hand)
        print()

        print(f'Dealer shows: {dealer_show_one}. Player total: {player_total}.')
    elif turn == 'dealer':
        prompt('Dealer:')
        display_hand(dealer_hand)
        print()
        
        prompt(f'Player:')
        display_hand(player_hand)
        print()
        
        print(f'Dealer total: {dealer_total}. Player total: {player_total}.')

    print('----------')

def play_again():
    prompt('Play again? (y)es or (n)o')
    while True:
        play_again = input().strip().lower()
        if play_again not in ['y', 'n']:
            prompt('Invalid input. Play again? (y)es or (n)o')
        else:
            return True if play_again == 'y' else False
    
def play_twenty_one():
    deck = initialize_deck()
    round = 1
    while True:
        player_hand, dealer_hand = deal_cards(deck)
        player_total = total_value(player_hand)
        dealer_total = total_value(dealer_hand)

        turn = 'player'
        display_table(dealer_hand, player_hand, dealer_total, player_total, turn)

        while True:
            if player_total == 21:
                break
            elif busted(player_total):
                print('Player busts!')
                break
            else:
                prompt('Will you (h)it or (s)tay? ')
                player_action = input().strip().lower()
                if player_action == 's':
                    break
                elif player_action == 'h':
                    player_total = total_value(hit(player_hand, deck))

                    display_table(dealer_hand, 
                                  player_hand, 
                                  dealer_total, 
                                  player_total, 
                                  turn,)

        while True:
            turn = 'dealer'
            
            display_table(dealer_hand,
                          player_hand,
                          dealer_total,
                          player_total,
                          turn,)

            if dealer_total >= 17 or player_total > 21:
                break
            else:
                dealer_total = total_value(hit(dealer_hand, deck))
                
                display_table(dealer_hand, 
                              player_hand, 
                              dealer_total, 
                              player_total, 
                              turn,)

                if busted(dealer_total):
                    print('Dealer busts!')
                    break
        
        winner = determine_outcome(player_total, dealer_total)
        display_winner(winner, player_total, dealer_total)

        if not play_again():
            break
        
        if round == 4:
            initialize_deck()
            prompt('Reshuffling deck...')
            input('Press (ENTER) to continue.')
            round = 1
        else:
            round += 1

    prompt('Thanks for playing!')

play_twenty_one()