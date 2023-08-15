from holdem_package.players import Players
from holdem_package.cards import Cards
from cards_index import card_index
from holdem_package.hand_evaluation import set_hand_value
from holdem_package.tiebreaker import straight_tie_breaker

test_case_1_players = Players.generate_players(8)
test_case_2_players = Players.generate_players(8)
test_case_3_players = Players.generate_players(8)
deck = Cards.generate_deck()


def generate_hand(hand_repr):
    player_hand = [deck[card_index[card]] for card in hand_repr]
    return player_hand


# test case 1: multiple winners with straight
# 3 players have the same straight - split pot between players 3, 5, 7
test_case_1_players[0].hand = generate_hand(["14 ♡", "3 ♤", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])
test_case_1_players[1].hand = generate_hand(["2 ♤", "10 ♧", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])
test_case_1_players[2].hand = generate_hand(["9 ♤", "7 ♤", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])  # straight 6-10
test_case_1_players[3].hand = generate_hand(["11 ♤", "11 ♢", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])
test_case_1_players[4].hand = generate_hand(["9 ♡", "8 ♤", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])  # straight 6-10
test_case_1_players[5].hand = generate_hand(["11 ♧", "10 ♤", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])
test_case_1_players[6].hand = generate_hand(["5 ♧", "9 ♢", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])  # Straight 6-10
test_case_1_players[7].hand = generate_hand(["14 ♢", "7 ♡", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])

# test case 2: highest straight
# 4 players have a straight, but 1 player has the highest straight - player 4 wins
test_case_2_players[0].hand = generate_hand(["14 ♡", "3 ♤", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])
test_case_2_players[1].hand = generate_hand(["2 ♤", "10 ♧", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])
test_case_2_players[2].hand = generate_hand(["9 ♤", "7 ♤", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])  # straight 6-10
test_case_2_players[3].hand = generate_hand(["11 ♤", "9 ♡", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])  # straight 7-11
test_case_2_players[4].hand = generate_hand(["9 ♡", "8 ♤", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])  # straight 6-10
test_case_2_players[5].hand = generate_hand(["11 ♧", "10 ♤", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])
test_case_2_players[6].hand = generate_hand(["5 ♧", "9 ♢", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])  # Straight 6-10
test_case_2_players[7].hand = generate_hand(["14 ♢", "7 ♡", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])


# test case 3: straight with Ace as 14 (10-14) vs straight with ace as 1 (1-5) - player 3 wins

test_case_3_players[0].hand = generate_hand(["13 ♡", "14 ♧", "14 ♤", "5 ♧", "3 ♤", "13 ♢", "11 ♡"])
test_case_3_players[1].hand = generate_hand(["13 ♧", "4 ♡", "14 ♤", "5 ♧", "3 ♤", "13 ♢", "11 ♡"])
test_case_3_players[2].hand = generate_hand(["12 ♧", "10 ♤", "14 ♤", "5 ♧", "3 ♤", "13 ♢", "11 ♡"])  # straight 10-14
test_case_3_players[3].hand = generate_hand(["11 ♢", "9 ♢", "14 ♤", "5 ♧", "3 ♤", "13 ♢", "11 ♡"])
test_case_3_players[4].hand = generate_hand(["3 ♡", "11 ♧", "14 ♤", "5 ♧", "3 ♤", "13 ♢", "11 ♡"])
test_case_3_players[5].hand = generate_hand(["6 ♤", "8 ♧", "14 ♤", "5 ♧", "3 ♤", "13 ♢", "11 ♡"])
test_case_3_players[6].hand = generate_hand(["14 ♡", "9 ♤", "14 ♤", "5 ♧", "3 ♤", "13 ♢", "11 ♡"])
test_case_3_players[7].hand = generate_hand(["4 ♧", "2 ♧", "14 ♤", "5 ♧", "3 ♤", "13 ♢", "11 ♡"])  # straight 1-5


set_hand_value(test_case_1_players)
set_hand_value(test_case_2_players)
set_hand_value(test_case_3_players)


test_case_1_expected_result = [test_case_1_players[2], test_case_1_players[4], test_case_1_players[6]]
test_case_1_actual_result = straight_tie_breaker(test_case_1_players)
assert test_case_1_expected_result == test_case_1_actual_result, \
    f'test case 1 failed. expected {test_case_1_expected_result}, got {test_case_1_actual_result}'
print('test case 1 passed')

test_case_2_expected_result = [test_case_2_players[3]]
test_case_2_actual_result = straight_tie_breaker(test_case_2_players)
assert test_case_2_expected_result == test_case_2_actual_result, \
    f'test case 2 failed. expected {test_case_2_expected_result}, got {test_case_2_actual_result}'
print('test case 2 passed')

test_case_3_expected_result = [test_case_3_players[2]]
test_case_3_actual_result = straight_tie_breaker(test_case_3_players)
assert test_case_3_expected_result == test_case_3_actual_result, \
    f'test case 3 failed. expected {test_case_3_expected_result}, got {test_case_3_actual_result}'
print('test case 3 passed')

''' for testing 
test_case_3_actual_result = two_pairs_winners(test_case_3_players)
print(test_case_3_actual_result)
'''
