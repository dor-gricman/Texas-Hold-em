# This file contains functions that evaluate the hand of each player and assign a hand rank to each player.
def high_card(player_hand):
    kickers = []
    hand_value = [card.value for card in player_hand]
    sorted_hand = sorted(hand_value, reverse=True)
    if all(sorted_hand.count(i) == 1 for i in sorted_hand):
        for i in sorted_hand:
            if len(kickers) < 5:
                kickers.append(i)
        return 1, kickers
    else:
        return None


def pair(player_hand):
    pairs = []
    kickers = []
    hand_value = [card.value for card in player_hand]
    sorted_hand = sorted(hand_value, reverse=True)
    for i in sorted_hand:
        if sorted_hand.count(i) == 2:
            pairs.append(i)
        elif sorted_hand.count(i) == 1 and len(kickers) < 3:
            kickers.append(i)
    if len(pairs) == 2:
        return 2, pairs, kickers
    else:
        return None


def two_pairs(player_hand):
    pairs_list = []
    kickers = []
    hand_value = [card.value for card in player_hand]
    sorted_hand = sorted(hand_value, reverse=True)
    for i in sorted_hand:
        if sorted_hand.count(i) == 2 and len(pairs_list) < 4:
            pairs_list.append(i)
        elif i not in pairs_list and len(kickers) < 1:
            kickers.append(i)
    if len(pairs_list) == 4:
        return 3, pairs_list, kickers
    else:
        return None


def three_of_a_kind(player_hand):
    triplets = []
    kickers = []
    hand_value = [card.value for card in player_hand]
    sorted_hand = sorted(hand_value, reverse=True)
    for i in sorted_hand:
        if sorted_hand.count(i) == 3:
            triplets.append(i)
        elif sorted_hand.count(i) == 1 and len(kickers) < 2:
            kickers.append(i)
    if len(triplets) == 3 and len(kickers) == 2:
        return 4, triplets, kickers
    else:
        return None


def straight(player_hand):
    hand_value = [card.value for card in player_hand]
    sorted_hand = sorted(hand_value, reverse=True)
    hand_set = list(dict.fromkeys(sorted_hand))
    for i in range(len(hand_set) - 4):
        if all(hand_set[j] - hand_set[j - 1] == -1 for j in range(i + 1, i + 5)):
            player_straight = hand_set[i: i + 5]
            return 5, player_straight
        elif {14, 2, 3, 4, 5}.issubset(set(hand_set)):
            player_straight = [5, 4, 3, 2, -14]
            return 5, player_straight
    else:
        return None


def flush(player_hand):
    player_hand = sorted(player_hand, key=lambda x: x.value, reverse=True)
    suit_count = {}
    flush_values = []
    for card in player_hand:
        if card.suit not in suit_count:
            suit_count[card.suit] = 1
        else:
            suit_count[card.suit] += 1
    for suit in suit_count:
        if suit_count[suit] >= 5:
            for card in player_hand:
                if card.suit == suit and len(flush_values) < 5:
                    flush_values.append(card.value)
    if len(flush_values) == 5:
        return 6, flush_values,
    else:
        return None


def full_house(player_hand):
    player_hand = [card.value for card in player_hand]
    triplet = [card for card in player_hand if player_hand.count(card) == 3]
    if len(triplet) >= 1:
        triplet = max(triplet)
    full_pair = [card for card in player_hand if player_hand.count(card) >= 2 and card != triplet]
    if len(full_pair) >= 1:
        full_pair = max(full_pair)
    if triplet and full_pair:
        return 7, ([triplet] * 3, [full_pair] * 2)
    else:
        return None


def four_of_a_kind(player_hand):
    hand_value = [card.value for card in player_hand]
    sorted_hand = sorted(hand_value, reverse=True)
    four_list = None
    four_kicker = None
    for card in sorted_hand:
        if sorted_hand.count(card) == 4:
            four_list = [card] * 4
            break
    if four_list is not None:
        for card in sorted_hand:
            if card not in four_list:
                four_kicker = card
                break
    if four_list is not None and four_kicker is not None:
        return 8, four_list, four_kicker
    else:
        return None


def straight_flush(player_hand):
    straights_list = []
    hand_value = [card.value for card in player_hand]
    sorted_hand = sorted(hand_value, reverse=True)
    hand_set = list(dict.fromkeys(sorted_hand))
    straight_shape = [card.suit for card in player_hand]

    for i in range(len(hand_set) - 4):
        sub_hand = hand_set[i: i + 5]
        if all(hand_set[j] - hand_set[j - 1] == -1 for j in range(i + 1, i + 5)):
            straights_list.append(sub_hand)
        elif {14, 2, 3, 4, 5}.issubset(set(hand_value)):
            straights_list.append([5, 4, 3, 2, -14])

    for sub_hand in straights_list:
        suite_list = [suite for suite, value in zip(straight_shape, hand_value) if value in sub_hand]
        if suite_list.count('heart') == 5 or suite_list.count('diamond') == 5 or suite_list.count(
                'club') == 5 or suite_list.count('spade') == 5:
            return 9, sub_hand, []

    return None


def royal_flush(player_hand):
    royal_heart = ['14 heart', '13 heart', '12 heart', '11 heart', '10 heart']
    royal_diamond = ['14 diamond', '13 diamond', '12 diamond', '11 diamond', '10 diamond']
    royal_club = ['14 club', '13 club', '12 club', '11 club', '10 club']
    royal_spade = ['14 spade', '13 spade', '12 spade', '11 spade', '10 spade']

    if any(all(card in player_hand for card in royal_suit) for royal_suit in
           [royal_heart, royal_diamond, royal_club, royal_spade]):
        return 10, player_hand, []
    else:
        return None


def set_hand_value(players):
    """ This function evaluates the hand of each player and assigns a hand rank to each player. """
    for player in players:
        if player.in_game:
            player.best_sequence = []
            player.hand_rank = 0
            player.kickers = []

            result = royal_flush(player.hand)
            if result is not None:
                player.hand_rank = result[0]
                player.best_sequence = result[1]
                continue

            result = straight_flush(player.hand)
            if result is not None:
                player.hand_rank = result[0]
                player.best_sequence = result[1]
                continue

            result = four_of_a_kind(player.hand)
            if result is not None:
                player.hand_rank = result[0]
                player.best_sequence = result[1]
                player.kickers = result[2]
                continue

            result = full_house(player.hand)
            if result is not None:
                player.hand_rank = result[0]
                player.best_sequence = result[1]
                continue

            result = flush(player.hand)
            if result is not None:
                player.hand_rank = result[0]
                player.best_sequence = result[1]
                continue

            result = straight(player.hand)
            if result is not None:
                player.hand_rank = result[0]
                player.best_sequence = result[1]
                continue

            result = three_of_a_kind(player.hand)
            if result is not None:
                player.hand_rank = result[0]
                player.best_sequence = result[1]
                player.kickers = result[2]
                continue

            result = two_pairs(player.hand)
            if result is not None:
                player.hand_rank = result[0]
                player.best_sequence = result[1]
                player.kickers = result[2]
                continue

            result = pair(player.hand)
            if result is not None:
                player.hand_rank = result[0]
                player.best_sequence = result[1]
                player.kickers = result[2]
                continue
            result = high_card(player.hand)
            if result is not None:
                player.hand_rank = result[0]
                player.kickers = result[1]
                continue


def set_hand_name(players):
    """ This function assigns a hand name to each player. """
    for player in players:
        if player.hand_rank == 1:
            player.hand_name = "High Card"
        elif player.hand_rank == 2:
            player.hand_name = "Pair"
        elif player.hand_rank == 3:
            player.hand_name = "Two Pairs"
        elif player.hand_rank == 4:
            player.hand_name = "Three of a Kind"
        elif player.hand_rank == 5:
            player.hand_name = "Straight"
        elif player.hand_rank == 6:
            player.hand_name = "Flush"
        elif player.hand_rank == 7:
            player.hand_name = "Full House"
        elif player.hand_rank == 8:
            player.hand_name = "Four of a Kind"
        elif player.hand_rank == 9:
            player.hand_name = "Straight Flush"
        elif player.hand_rank == 10:
            player.hand_name = "Royal Flush"


def print_hand(players):
    """ This function prints the hand of each player. """
    for player in players:
        print(f'{player.name}\n{player.hand}\n{player.hand_name}')
