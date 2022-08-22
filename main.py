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


def deal_cards(shuffled_deck, num_of_players):
    all_hands = []

    for _ in range(num_of_players):
        hand = []

        for index in range(0, 5):
            hand.append(shuffled_deck.pop(index))

        all_hands += [hand]
    
    return all_hands


def start_game(number_of_players, rounds_to_play):

    deck = generate_deck()
    shuffled_deck = shuffle_deck(deck)
    hands = deal_cards(shuffled_deck, number_of_players)
    for key, value in enumerate(hands):
        print(f'Player {key + 1} has a hand of {value}')


start_game(4, 1)
