from holdem_package.players import Players
from holdem_package.cards import Cards
from cards_index import card_index
from holdem_package.hand_evaluation import set_hand_value
from holdem_package.tiebreaker import two_pairs_winners_tie_breaker

test_case_1_players = Players.generate_players(8)
test_case_2_players = Players.generate_players(8)
test_case_3_players = Players.generate_players(8)

deck = Cards.generate_deck()


def generate_hand(hand_repr):
    player_hand = [deck[card_index[card]] for card in hand_repr]
    return player_hand


# -----------------------multiple players with two pairs-----------------------


# multiple players with two pairs only one max first pair - one winner

test_case_1_players[0].hand = generate_hand(['10 ♤', '8 ♡', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_1_players[1].hand = generate_hand(['4 ♧', '13 ♡', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_1_players[2].hand = generate_hand(['11 ♧', '7 ♤', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_1_players[3].hand = generate_hand(['8 ♢', '9 ♢', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_1_players[4].hand = generate_hand(['2 ♤', '2 ♡', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_1_players[5].hand = generate_hand(['8 ♤', '6 ♤', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_1_players[6].hand = generate_hand(['6 ♧', '10 ♡', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_1_players[7].hand = generate_hand(['3 ♧', '14 ♧', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])

# 2 players with max two pairs only one max kicker - one winner

test_case_2_players[0].hand = generate_hand(['10 ♤', '8 ♡', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_2_players[1].hand = generate_hand(['4 ♧', '13 ♡', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_2_players[2].hand = generate_hand(['11 ♧', '7 ♤', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_2_players[3].hand = generate_hand(['8 ♢', '9 ♢', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_2_players[4].hand = generate_hand(['2 ♤', '2 ♡', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_2_players[5].hand = generate_hand(['13 ♤', '14 ♤', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '6 ♤'])
test_case_2_players[6].hand = generate_hand(['6 ♧', '10 ♡', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_2_players[7].hand = generate_hand(['3 ♧', '14 ♧', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '6 ♤'])


# multiple players with two pairs and max kicker - multiple winners

test_case_3_players[0].hand = generate_hand(['10 ♤', '8 ♡', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_3_players[1].hand = generate_hand(['4 ♧', '14 ♢', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_3_players[2].hand = generate_hand(['11 ♧', '7 ♤', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_3_players[3].hand = generate_hand(['8 ♢', '9 ♢', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_3_players[4].hand = generate_hand(['2 ♤', '2 ♡', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_3_players[5].hand = generate_hand(['4 ♤', '14 ♤', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_3_players[6].hand = generate_hand(['6 ♧', '10 ♡', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])
test_case_3_players[7].hand = generate_hand(['3 ♧', '14 ♧', '12 ♢', '6 ♡', '5 ♢', '14 ♡', '5 ♤'])


set_hand_value(test_case_1_players)
set_hand_value(test_case_2_players)
set_hand_value(test_case_3_players)


test_case_1_expected_result = [test_case_1_players[7]]
test_case_1_actual_result = two_pairs_winners_tie_breaker(test_case_1_players)
assert test_case_1_expected_result == test_case_1_actual_result, \
    f'test case 1 failed. expected {test_case_1_expected_result}, got {test_case_1_actual_result}'
print('test case 1 passed')

test_case_2_expected_result = [test_case_2_players[5]]
test_case_2_actual_result = two_pairs_winners_tie_breaker(test_case_2_players)
assert test_case_2_expected_result == test_case_2_actual_result, \
    f'test case 2 failed. expected {test_case_2_expected_result}, got {test_case_2_actual_result}'
print('test case 2 passed')

test_case_3_expected_result = [test_case_3_players[1], test_case_3_players[5], test_case_3_players[7]]
test_case_3_actual_result = two_pairs_winners_tie_breaker(test_case_3_players)
assert test_case_3_expected_result == test_case_3_actual_result, \
    f'test case 3 failed. expected {test_case_3_expected_result}, got {test_case_3_actual_result}'
print('test case 3 passed')
