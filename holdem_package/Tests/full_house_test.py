from holdem_package.players import Players
from holdem_package.cards import Cards
from cards_index import card_index
from holdem_package.hand_evaluation import set_hand_value
from holdem_package.tiebreaker import full_house_tie_breaker

test_case_1_players = Players.generate_players(8)
test_case_2_players = Players.generate_players(8)
deck = Cards.generate_deck()


def generate_hand(hand_repr):
    player_hand = [deck[card_index[card]] for card in hand_repr]
    return player_hand


# test case 1 - split pot between 2 players with 4 full of 10 - player 4 and 7 wins
# 3 players with full house, 1 players with 4 full of 2, 2 players has 4 full of 10 - 4 full of 10 wins
test_case_1_players[0].hand = generate_hand(["12 ♢", "9 ♤", "4 ♤", "2 ♧", "10 ♤", "4 ♡", "4 ♧"])
test_case_1_players[1].hand = generate_hand(["9 ♢", "12 ♧", "4 ♤", "2 ♧", "10 ♤", "4 ♡", "4 ♧"])
test_case_1_players[2].hand = generate_hand(["11 ♤", "14 ♧", "4 ♤", "2 ♧", "10 ♤", "4 ♡", "4 ♧"])
test_case_1_players[3].hand = generate_hand(["10 ♧", "2 ♢", "4 ♤", "2 ♧", "10 ♤", "4 ♡", "4 ♧"])  # 4 full of 10
test_case_1_players[4].hand = generate_hand(["8 ♢", "7 ♡", "4 ♤", "2 ♧", "10 ♤", "4 ♡", "4 ♧"])
test_case_1_players[5].hand = generate_hand(["9 ♧", "6 ♧", "4 ♤", "2 ♧", "10 ♤", "4 ♡", "4 ♧"])
test_case_1_players[6].hand = generate_hand(["10 ♡", "7 ♧", "4 ♤", "2 ♧", "10 ♤", "4 ♡", "4 ♧"])  # 4 full of 10
test_case_1_players[7].hand = generate_hand(["12 ♡", "2 ♤", "4 ♤", "2 ♧", "10 ♤", "4 ♡", "4 ♧"])  # 4 full of 2


# test case 2 - 4 players with full house, 1 player with 2 triplets , 10, 10, 10, 4, 4, 4, one player with 6, 6, 6, 4, 4
# verifying that the player triplets taken are 10 and not 4 - player 7 wins
test_case_2_players[0].hand = generate_hand(["12 ♢", "9 ♤", "4 ♤", "6 ♢", "10 ♤", "4 ♡", "4 ♧"])
test_case_2_players[1].hand = generate_hand(["9 ♢", "12 ♧", "4 ♤", "6 ♢", "10 ♤", "4 ♡", "4 ♧"])
test_case_2_players[2].hand = generate_hand(["11 ♤", "14 ♧", "4 ♤", "6 ♢", "10 ♤", "4 ♡", "4 ♧"])
test_case_2_players[3].hand = generate_hand(["10 ♧", "2 ♢", "4 ♤", "6 ♢", "10 ♤", "4 ♡", "4 ♧"])  # 4 full of 10
test_case_2_players[4].hand = generate_hand(["8 ♢", "7 ♡", "4 ♤", "6 ♢", "10 ♤", "4 ♡", "4 ♧"])
test_case_2_players[5].hand = generate_hand(["6 ♡", "6 ♧", "7 ♢", "6 ♢", "10 ♤", "4 ♡", "4 ♧"])  # 6 full of 4
test_case_2_players[6].hand = generate_hand(["10 ♡", "10 ♢", "4 ♤", "6 ♢", "10 ♤", "4 ♡", "4 ♧"])  # 10 full of 4
test_case_2_players[7].hand = generate_hand(["12 ♡", "12 ♤", "4 ♤", "6 ♢", "10 ♤", "4 ♡", "4 ♧"])  # 4 full of 12


set_hand_value(test_case_1_players)
set_hand_value(test_case_2_players)


test_case_1_expected_result = [test_case_1_players[3], test_case_1_players[6]]
test_case_1_actual_result = full_house_tie_breaker(test_case_1_players)
assert test_case_1_actual_result == test_case_1_expected_result,\
    f'test case 1 failed. expected {test_case_1_expected_result}, got {test_case_1_actual_result}'
print('test case 1 passed')

test_case_2_expected_result = [test_case_2_players[6]]
test_case_2_actual_result = full_house_tie_breaker(test_case_2_players)
assert test_case_2_actual_result == test_case_2_expected_result,\
    f'test case 2 failed. expected {test_case_2_expected_result}, got {test_case_2_actual_result}'
print('test case 2 passed')
