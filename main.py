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
        if 2 <= cards[card] <= 3:
            total_pairs += 1
        elif cards[card] > 3 and cards[card] % 2 == 0:
            total_pairs += cards[card] / 2

    return total_pairs


def deal_cards(shuffled_deck, num_of_players, cards_per_player):
    all_hands = []

    for index in range(num_of_players):
        hand = {
            'name': 'Player ' + str(index + 1),
            'cards': {},
            'pairs': 0
        }

        for index in range(0, cards_per_player):
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
        print(
            f"\n{player['name']} \nHand: {player['cards']} \nNumber of Pairs: {player['pairs']}")


def sort_by_highest_pairs(players):
    players_list_copy = players[:]

    for _ in range(len(players_list_copy)):
        for index in range(len(players_list_copy) - 1):
            if players_list_copy[index + 1]['pairs'] > players_list_copy[index]['pairs']:
                temp = players_list_copy[index]
                players_list_copy[index] = players_list_copy[index + 1]
                players_list_copy[index + 1] = temp

    return players_list_copy


def calculate_game_result(players):
    final_results = [players[0]['name']]

    for index in range(1, len(players)):
        if players[0]['pairs'] == players[index]['pairs']:
            final_results.append(players[index]['name'])

    if len(final_results) == 1:
        print(f"\n{final_results[0]} is the winner!")
    else:
        players_minus_last = ', '.join(final_results[:len(final_results) - 1])
        last_player = final_results[-1]
        print(
            f"\nThere is a tie among {players_minus_last} and {last_player}.")


def start_game():
    print('\nWelcome to Player Pairs!')
    print('In this game each player will receive a hand of cards.\nOnce each hand has been dealt, we will compare to see who has the most pairs!')

    number_of_players = int(input('\nEnter the number of players: '))
    rounds_to_play = int(input('Enter the number of rounds to play: '))

    cards_per_player = 5
    cards_per_game = number_of_players * cards_per_player

    valid_game = True if cards_per_game <= 52 else False

    if valid_game:
        original_deck = generate_deck()
        shuffled_deck = shuffle_deck(original_deck)

        for round in range(1, rounds_to_play + 1):
            print('\nRound:', round)

            if len(shuffled_deck) <= cards_per_game:
                shuffled_deck = shuffle_deck(original_deck)

            hands = deal_cards(
                shuffled_deck, number_of_players, cards_per_player)
            display_player_hands(hands)
            sorted_players_by_pairs = sort_by_highest_pairs(hands)
            calculate_game_result(sorted_players_by_pairs)
    else:
        print('Invalid game: Too many players.')
        return

    print('\nGAME OVER.')


start_game()
