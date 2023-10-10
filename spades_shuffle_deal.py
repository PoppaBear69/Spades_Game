import random

# Define a function to create and shuffle a deck of cards
def create_shuffled_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

    # Add Big Joker and Little Joker
    deck.append({'rank': 'Big Joker', 'suit': 'Joker'})
    deck.append({'rank': 'Little Joker', 'suit': 'Joker'})

    # Remove 2 of Hearts and 2 of Clubs
    deck = [card for card in deck if not (card['rank'] == '2' and (card['suit'] == 'Hearts' or card['suit'] == 'Clubs'))]

    random.shuffle(deck)
    return deck

# Define the number of players
num_players = 4

# Create and shuffle the deck
deck = create_shuffled_deck()

# Deal the cards to the players
players = [[] for _ in range(num_players)]

for i, card in enumerate(deck):
    players[i % num_players].append(card)

# Display the hands of each player
for i, player in enumerate(players):
    print(f"Player {i + 1}'s hand:")
    for card in player:
        print(f"{card['rank']} of {card['suit']}")
    print()
