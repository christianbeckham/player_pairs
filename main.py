import enum
from random import randrange


def generate_deck():
    cards = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    new_deck = []

    for card in cards:
        for _ in range(4):
            new_deck.append(str(card))

    return new_deck


def shuffle_deck(deck):
    temp_deck = deck[:]

    for index in range(len(temp_deck)):
        random_number = randrange(0, len(temp_deck))
        card = temp_deck.pop(index)
        temp_deck.insert(random_number, card)

    return temp_deck


def calculate_pairs(cards):
    total_pairs = 0

    for card in cards:
        if cards[card] >= 2:
            total_pairs += 1

    return total_pairs


def deal_cards(shuffled_deck, num_of_players):
    all_hands = []

    for index in range(num_of_players):
        hand = {
            'name': 'Player ' + str(index + 1),
            'cards': {},
            'pairs': 0
        }

        for index in range(0, 5):
            card = shuffled_deck.pop(0)

            if card not in hand['cards']:
                hand['cards'][card] = 1
            else:
                hand['cards'][card] += 1

        hand['pairs'] = calculate_pairs(hand['cards'])
        all_hands.append(hand)

    return all_hands


def display_player_hands(players):
    for player in players:
        print(f"\n{player['name']} \nHand: {player['cards']} \nNumber of Pairs: {player['pairs']}")


def start_game(number_of_players, rounds_to_play):
    print('\nWelcome to Player Pairs!')
    print('In this game each player will receive 5 cards.\nOnce each hand has been dealt, we will compare to see who has the most pairs!')

    deck = generate_deck()
    shuffled_deck = shuffle_deck(deck)
    hands = deal_cards(shuffled_deck, number_of_players)
    display_player_hands(hands)
    # check_hand_results(hands)


start_game(4, 1)
