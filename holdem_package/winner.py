from holdem_package.tiebreaker import high_card_tiebreaker, pair_winners_tie_breaker,\
    two_pairs_winners_tie_breaker, three_of_a_kind_tie_breaker, straight_tie_breaker,\
    flush_tie_breaker, full_house_tie_breaker,\
    four_of_a_kind_tiebreaker, straight_flush_tiebreaker


def evaluate_winner(players_list):
    best_hand_rank = max([player.hand_rank for player in players_list if player.in_game])
    players_with_best_hand_rank = [player for player in players_list if player.hand_rank == best_hand_rank]
    if len(players_with_best_hand_rank) == 1:
        winner = players_with_best_hand_rank
        return winner
    else:
        if best_hand_rank == 1:
            winner = high_card_tiebreaker(players_with_best_hand_rank)
            return winner
        elif best_hand_rank == 2:
            winner = pair_winners_tie_breaker(players_with_best_hand_rank)
            return winner
        elif best_hand_rank == 3:
            winner = two_pairs_winners_tie_breaker(players_with_best_hand_rank)
            return winner
        elif best_hand_rank == 4:
            winner = three_of_a_kind_tie_breaker(players_with_best_hand_rank)
            return winner
        elif best_hand_rank == 5:
            winner = straight_tie_breaker(players_with_best_hand_rank)
            return winner
        elif best_hand_rank == 6:
            winner = flush_tie_breaker(players_with_best_hand_rank)
            return winner
        elif best_hand_rank == 7:
            winner = full_house_tie_breaker(players_with_best_hand_rank)
            return winner
        elif best_hand_rank == 8:
            winner = four_of_a_kind_tiebreaker(players_with_best_hand_rank)
            return winner
        elif best_hand_rank == 9:
            winner = straight_flush_tiebreaker(players_with_best_hand_rank)
            return winner


def pot_to_winner(winner, pot):
    for player in winner:
        share = pot.total // len(winner)
        player.balance += share



