# this file contains the tiebreaker functions for each hand rank

def high_card_tiebreaker(players_list):
    players = [player for player in players_list if player.hand_rank == 1]
    players_kickers = [player.kickers for player in players]
    flattened_kickers = [kicker for player_kickers in players_kickers for kicker in player_kickers]
    sorted_kickers = sorted(flattened_kickers, reverse=True)
    sorted_kickers = sorted_kickers[:5]
    while len(players) > 1 and len(sorted_kickers):
        highest_kicker = sorted_kickers.pop(0)
        players = [player for player in players if highest_kicker in player.kickers]
        if len(players) == 1 or not sorted_kickers:
            winner = players
            return winner


def pair_winners_tie_breaker(players_list):
    players = [player for player in players_list if player.hand_rank == 2]
    players_best_sequence = [player.best_sequence for player in players]
    flattened_players_best_sequence = ([item for sublist in players_best_sequence for item in sublist])
    flattened_players_best_sequence_set = list(dict.fromkeys(flattened_players_best_sequence))
    players_with_best_pair = [player for player in players if max(flattened_players_best_sequence_set) in player.best_sequence]
    if len(players_with_best_pair) == 1:
        winner = players_with_best_pair
        return winner
    elif len(players_with_best_pair) > 1:
        players_best_kickers = [player.kickers for player in players_with_best_pair]
        players_best_kickers = ([item for sublist in players_best_kickers for item in sublist])
        players_best_kickers_set = list(dict.fromkeys(players_best_kickers))
        best_kickers_sorted = sorted(players_best_kickers_set, reverse=True)
        while len(players_with_best_pair) > 1 or best_kickers_sorted:
            best_kicker = best_kickers_sorted.pop(0)
            players_with_best_pair = [player for player in players_with_best_pair if best_kicker in player.kickers]
            if len(players_with_best_pair) == 1 or not best_kickers_sorted:
                winner = players_with_best_pair
                return winner


def two_pairs_winners_tie_breaker(players_list):
    players = [player for player in players_list if player.hand_rank == 3]
    players_best_sequence = [player.best_sequence for player in players]
    flattened_players_best_sequence = set([item for sublist in players_best_sequence for item in sublist])
    players_with_best_pair = [player for player in players if max(flattened_players_best_sequence) in player.best_sequence]
    players_with_best_pair_sequence = [player.best_sequence for player in players_with_best_pair]
    if len(players_with_best_pair) == 1:
        winner = players_with_best_pair
        return winner
    elif len(players_with_best_pair) > 1:
        flattened_players_best_pair_sequence = set([item for sublist in players_with_best_pair_sequence for item in sublist])
        flattened_players_best_pair_sequence.remove(max(flattened_players_best_pair_sequence))
        players_with_best_second_pair = [player for player in players_with_best_pair if max(flattened_players_best_pair_sequence) in player.best_sequence]
        if len(players_with_best_second_pair) == 1:
            winner = players_with_best_second_pair
            return winner
        elif len(players_with_best_second_pair) > 1:
            best_kicker = [max(player.kickers) for player in players_with_best_second_pair]
            players_with_best_kicker = [player for player in players_with_best_second_pair if max(best_kicker) in player.kickers]
            winner = players_with_best_kicker
            return winner


def three_of_a_kind_tie_breaker(players):
    players = [player for player in players if player.hand_rank == 4]
    players_best_sequence = [player.best_sequence for player in players]
    flattened_players_best_sequence = [item for sublist in players_best_sequence for item in sublist]
    players_with_best_triplet = [player for player in players if max(flattened_players_best_sequence) in player.best_sequence]
    if len(players_with_best_triplet) == 1:
        winner = players_with_best_triplet
        return winner
    elif len(players_with_best_triplet) > 1:
        players_kickers = [player.kickers for player in players_with_best_triplet]
        flattened_kickers = [item for sublist in players_kickers for item in sublist]
        flattened_kickers = flattened_kickers[0:2]
        flattened_kickers.sort(reverse=True)
        while len(players_with_best_triplet) > 1 or not flattened_kickers:
            max_kicker = flattened_kickers.pop(0)
            players_with_best_triplet = [player for player in players_with_best_triplet if max_kicker in player.kickers]
            if len(players_with_best_triplet) == 1 or not flattened_kickers:
                winner = players_with_best_triplet
                return winner


def straight_tie_breaker(players_list):
    players = [player for player in players_list if player.hand_rank == 5]
    highest_straight_card = [player.best_sequence[0] for player in players]
    players_with_best_straight = [player for player in players if max(highest_straight_card) in player.best_sequence]
    winner = players_with_best_straight
    return winner


def flush_tie_breaker(players_list):
    players = [player for player in players_list if player.hand_rank == 6]
    players_best_sequence = [player.best_sequence for player in players]
    flattened_players_best_sequence = [card for sublist in players_best_sequence for card in sublist]
    players_best_sequence_set = sorted(list(dict.fromkeys(flattened_players_best_sequence)), reverse=True)
    players_best_sequence_set = players_best_sequence_set[:5]
    while len(players) > 1 or not players_best_sequence_set:
        highest_flush_card = players_best_sequence_set.pop(0)
        players = [player for player in players if highest_flush_card in player.best_sequence]
        if len(players) == 1 or not players_best_sequence_set:
            winner = players
            return winner


def full_house_tie_breaker(players_list):
    players = [player for player in players_list if player.hand_rank == 7]
    players_best_triplet = [player.best_sequence[0] for player in players]
    flattened_players_best_triplet = [item for sublist in players_best_triplet for item in sublist]
    players_with_best_triplets = [player for player in players if max(flattened_players_best_triplet) in player.best_sequence[0]]
    if len(players_with_best_triplets) == 1:
        winner = players_with_best_triplets
        return winner
    elif len(players_with_best_triplets) > 1:
        players_best_pair = [player.best_sequence[1] for player in players_with_best_triplets]
        flattened_players_best_pair = [item for sublist in players_best_pair for item in sublist]
        players_with_best_pair = [player for player in players_with_best_triplets if max(flattened_players_best_pair) in player.best_sequence[1]]
        winner = players_with_best_pair
        return winner


def four_of_a_kind_tiebreaker(players_list):
    players = [player for player in players_list if player.hand_rank == 8]
    players_best_sequence = [player.best_sequence for player in players]
    flattened_best_sequence = [card for sublist in players_best_sequence for card in sublist]
    players_with_best_four_of_a_kind = [player for player in players if max(flattened_best_sequence) in player.best_sequence]
    if len(players_with_best_four_of_a_kind) == 1:
        winner = players_with_best_four_of_a_kind
        return winner
    elif len(players_with_best_four_of_a_kind) > 1:
        players_kickers = [player.kickers for player in players_with_best_four_of_a_kind]
        sorted_kickers = sorted(players_kickers, reverse=True)
        sorted_kickers = sorted_kickers[0:5]
        max_kicker = sorted_kickers.pop(0)
        while len(players_with_best_four_of_a_kind) > 1 or not sorted_kickers:
            players_with_best_four_of_a_kind = [player for player in players_with_best_four_of_a_kind if max_kicker == player.kickers]
            if len(players_with_best_four_of_a_kind) == 1 or not sorted_kickers:
                winner = players_with_best_four_of_a_kind
                return winner


def straight_flush_tiebreaker(players_list):
    players = [player for player in players_list if player.hand_rank == 9]
    highest_straight_flush_card = [player.best_sequence[0] for player in players]
    players_with_best_straight = [player for player in players if max(highest_straight_flush_card) in player.best_sequence]
    winner = players_with_best_straight
    return winner
