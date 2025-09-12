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

        print(f'Dealer shows: {dealer_show_one}. '
              f'Player total: {player_total}.')

    elif turn == 'dealer':
        prompt('Dealer:')
        display_hand(dealer_hand)
        print()

        prompt('Player:')
        display_hand(player_hand)
        print()

        print(f'Dealer total: {dealer_total}. Player total: {player_total}.')

    print('----------')

def play_again():
    prompt('Play again? (y)es or (n)o')
    while True:
        play_again_input = input().strip().lower()
        if play_again_input not in ['y', 'n']:
            prompt('Invalid input. Play again? (y)es or (n)o')
        else:
            return True if play_again_input == 'y' else False

def play_twenty_one():
    deck = initialize_deck()
    game_round = 1
    while True:
        player_hand, dealer_hand = deal_cards(deck)
        player_total = total_value(player_hand)
        dealer_total = total_value(dealer_hand)

        turn = 'player'
        display_table(dealer_hand,
                      player_hand,
                      dealer_total,
                      player_total,
                      turn,)

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

        if game_round == 4:
            initialize_deck()
            prompt('Reshuffling deck...')
            input('Press (ENTER) to continue.')
            game_round = 1
        else:
            game_round += 1

    prompt('Thanks for playing!')

play_twenty_one()