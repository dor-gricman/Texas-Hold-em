from holdem_package.players import Players
from holdem_package.cards import Cards
from cards_index import card_index
from holdem_package.hand_evaluation import set_hand_value
from holdem_package.tiebreaker import pair_winners_tie_breaker

test_case_1_players = Players.generate_players(8)
test_case_2_players = Players.generate_players(8)
test_case_3_players = Players.generate_players(8)
deck = Cards.generate_deck()


def generate_hand(hand_repr):
    player_hand = [deck[card_index[card]] for card in hand_repr]
    return player_hand


# test case 1:
# multiple pairs, only one player with max pair
test_case_1_players[0].hand = generate_hand(["12 ♢", "2 ♧", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_1_players[1].hand = generate_hand(["12 ♡", "8 ♧", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_1_players[2].hand = generate_hand(["11 ♡", "2 ♡", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])  # winner pair [11 ♡, 11 ♧]
test_case_1_players[3].hand = generate_hand(["6 ♢", "10 ♤", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_1_players[4].hand = generate_hand(["12 ♤", "13 ♧", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_1_players[5].hand = generate_hand(["3 ♤", "6 ♤", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_1_players[6].hand = generate_hand(["7 ♢", "4 ♧", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_1_players[7].hand = generate_hand(["5 ♧", "4 ♡", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])

# test case 2:
# multiple players with max pair, only one player with max high card
test_case_2_players[0].hand = generate_hand(["12 ♢", "2 ♧", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_2_players[1].hand = generate_hand(["11 ♢", "8 ♧", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_2_players[2].hand = generate_hand(["11 ♡", "2 ♡", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_2_players[3].hand = generate_hand(["6 ♢", "10 ♤", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_2_players[4].hand = generate_hand(["11 ♤", "13 ♧", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])  # winner - pair [11 ♤, 11 ♧] 13 kicker
test_case_2_players[5].hand = generate_hand(["3 ♤", "6 ♤", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_2_players[6].hand = generate_hand(["7 ♢", "4 ♧", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_2_players[7].hand = generate_hand(["5 ♧", "4 ♡", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])

# test case 3:
# multiple players with max pair, multiple players with max high card
test_case_3_players[0].hand = generate_hand(["12 ♢", "2 ♧", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_3_players[1].hand = generate_hand(["11 ♢", "13 ♤", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])  # winner - pair [11 ♢, 11 ♧] 13 kicker
test_case_3_players[2].hand = generate_hand(["11 ♡", "13 ♡", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])  # winner - pair [11 ♡, 11 ♧] 13 kicker
test_case_3_players[3].hand = generate_hand(["6 ♢", "10 ♤", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_3_players[4].hand = generate_hand(["11 ♤", "13 ♧", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])  # winner - pair [11 ♤, 11 ♧] 13 kicker
test_case_3_players[5].hand = generate_hand(["3 ♤", "6 ♤", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_3_players[6].hand = generate_hand(["7 ♢", "4 ♧", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])
test_case_3_players[7].hand = generate_hand(["5 ♧", "4 ♡", "14 ♢", "7 ♤", "6 ♡", "9 ♤", "11 ♧"])


set_hand_value(test_case_1_players)
set_hand_value(test_case_2_players)
set_hand_value(test_case_3_players)


test_case_1_expected_result = [test_case_1_players[2]] # expected winner - player 3
test_case_1_actual_result = pair_winners_tie_breaker(test_case_1_players) # actual winner
assert test_case_1_expected_result == test_case_1_actual_result,\
    f'test case 1 failed. expected {test_case_1_expected_result}, got {test_case_1_actual_result}' # comparing the expected result to the actual result
print('test case 1 passed')

test_case_2_expected_result = [test_case_2_players[4]]
test_case_2_actual_result = pair_winners_tie_breaker(test_case_2_players)
assert test_case_2_expected_result == test_case_2_actual_result, \
    f'test case 2 failed. expected {test_case_2_expected_result}, got {test_case_2_actual_result}'
print('test case 2 passed')

test_case_3_expected_result = [test_case_3_players[1], test_case_3_players[2], test_case_3_players[4]]
test_case_3_actual_result = pair_winners_tie_breaker(test_case_3_players)
assert test_case_3_expected_result == test_case_3_actual_result, \
    f'test case 3 failed. expected {test_case_3_expected_result}, got {test_case_3_actual_result}'
print('test case 3 passed')
