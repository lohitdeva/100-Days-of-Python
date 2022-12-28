import os
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

start_condition = 'y'
# Assumption: We are playing with an infinite deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start_condition = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n")

while start_condition == 'y':

    os.system('cls')
    print(logo)

    player_cards = list()
    computer_cards = list()

    # Start of the game where both player and computer and handed 2 cards each
    for _ in range(2):
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    
    pass_condition = 'y'
    player_bust = False
 
    while pass_condition == 'y':
        # If player has an ace and has gone over 21, convert 11 to 1 (soft hand)
        if sum(player_cards) > 21 and 11 in player_cards:
            player_cards[player_cards.index(11)] = 1

        print(f"\nYour cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Player loses because of going over 21
        if sum(player_cards) > 21:
            print("\nYou went bust, you lose! 😭")
            player_bust = True
            break

        # Player doesn't lose, but also doesn't have to draw any more cards because they are at 21
        elif sum(player_cards) == 21:
            break

        pass_condition = input("\nType 'y' to get another card, type 'n' to pass:\n")

        # Another card added to player's hand
        if pass_condition == 'y':
            player_cards.append(random.choice(cards))

    computer_bust = False

    while not computer_bust and not player_bust:

        if sum(computer_cards) > 21:
            # If computer has an ace and has gone over 21, convert 11 to 1 (soft hand)
            if 11 in computer_cards:
                computer_cards[computer_cards.index(11)] = 1
            # If computer has gone over 21
            else:
                computer_bust = True
        
        # Computer stops drawing cards after reaching 17 or above
        if sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))
        else:
            break
    
    # No need to do anything if player hand is bust as loss message is already displayed
    if not player_bust:
        # This condition is only satisfied if the player wins on the first hand with a 10 and an ace
        if sum(player_cards) == 21 and 11 in player_cards and len(player_cards) == 2:
            print('\nYou win by blackjack ♠ 😎')
    
        # Display final hand values. This is not required if player wins by blackjack.
        print(f"\nYour final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        
        # Player automatically wins if computer goes bust
        if computer_bust:
            print("\nThe computer went bust, you win! 😁 👍")
        # If neither player, nor computer are bust, the one closer to 21 (i. e, the one with the greater hand value) wins
        else:    
            if sum(player_cards) > sum(computer_cards):
                print("\nYou win! 🎉")
            elif sum(player_cards) == sum(computer_cards):
                print("\nIt's a standoff! ⚔")
            else:
                print("\nYou lose! 😥")

    start_condition = input("\nDo you want to continue playing? Type 'y' for yes or 'n' for no:\n")

# Stop playing
else:
    print("\nGoodbye")
