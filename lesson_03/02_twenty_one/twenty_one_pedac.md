# PEDAC for Twenty-One
## Understand the Problem
### Inputs:
    # User starts the game, the deck of cards is initialized and shuffled, and dealer deals the cards
    # Dealer deals the cards
### Outputs:
    # The result of three possible outcomes: Player wins, Dealer wins, or it's a tie; resulting from Player choosing specific actions based on the cards Player is dealt and the card shown in the Dealer's hand
### Requirements:
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

## Data Structure:
    # Probably dictionary or list or some combinations of the two
    # Option 1: a tuple or list of dictionaries
        # Each dictionary represents a suit, keys are cards, values are values
    # Option 2: a nested list (LS choice)
        # inner lists are [suit, card_value] 

## Algorithm:
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