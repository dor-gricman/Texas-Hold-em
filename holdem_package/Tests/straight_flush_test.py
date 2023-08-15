from holdem_package.cards import Cards
from cards_index import card_index
from holdem_package.players import Players
from holdem_package.hand_evaluation import set_hand_value
from holdem_package.tiebreaker import straight_flush_tiebreaker


test_case_1_players = Players.generate_players(8)
deck = Cards.generate_deck()


def generate_hand(hand_repr):
    player_hand = [deck[card_index[card]] for card in hand_repr]
    return player_hand


#  test case 1: two straight flushes, one player has a higher straight flush - player 1 wins
test_case_1_players[0].hand = generate_hand(['12 ♡', '9 ♡', '11 ♡', '10 ♡', '8 ♡', '13 ♢', '3 ♧'])  # straight flush to 12
test_case_1_players[1].hand = generate_hand(['7 ♡', '9 ♡', '11 ♡', '10 ♡', '8 ♡', '13 ♢', '3 ♧'])  # straight flush to 11
test_case_1_players[2].hand = generate_hand(['4 ♡', '2 ♡', '11 ♡', '10 ♡', '8 ♡', '13 ♢', '3 ♧'])
test_case_1_players[3].hand = generate_hand(['5 ♡', '6 ♡', '11 ♡', '10 ♡', '8 ♡', '13 ♢', '3 ♧'])
test_case_1_players[4].hand = generate_hand(['14 ♡', '2 ♧', '11 ♡', '10 ♡', '8 ♡', '13 ♢', '3 ♧'])
test_case_1_players[5].hand = generate_hand(['14 ♧', '2 ♢', '11 ♡', '10 ♡', '8 ♡', '13 ♢', '3 ♧'])
test_case_1_players[6].hand = generate_hand(['14 ♢', '2 ♤', '11 ♡', '10 ♡', '8 ♡', '13 ♢', '3 ♧'])
test_case_1_players[7].hand = generate_hand(['14 ♤', '3 ♡', '11 ♡', '10 ♡', '8 ♡', '13 ♢', '3 ♧'])

set_hand_value(test_case_1_players)


test_case_1_expected = [test_case_1_players[0]]
test_case_1_actual = straight_flush_tiebreaker(test_case_1_players)
assert test_case_1_expected == test_case_1_actual, f"test case 1 failed. expected: {test_case_1_expected}, got: {test_case_1_actual}"
print("test case 1 passed")
