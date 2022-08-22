from random import randrange


def generate_deck():
    cards = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    new_deck = []

    for card in cards:
        for _ in range(4):
            new_deck.append(str(card))

    return new_deck


def shuffle_deck(deck):

    for index in range(len(deck)):
        random_number = randrange(0, len(deck))
        card = deck.pop(index)
        deck.insert(random_number, card)

    return deck


deck = generate_deck()
shuffled_deck = shuffle_deck(deck)
print('Shuffled deck of cards', shuffled_deck)
