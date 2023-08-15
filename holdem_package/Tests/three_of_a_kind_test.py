from holdem_package.cards import Cards
from cards_index import card_index
from holdem_package.players import Players
from holdem_package.hand_evaluation import set_hand_value
from holdem_package.tiebreaker import three_of_a_kind_tie_breaker


test_case_1_players = Players.generate_players(8)
test_case_2_players = Players.generate_players(8)
deck = Cards.generate_deck()


def generate_hand(hand_repr):
    player_hand = [deck[card_index[card]] for card in hand_repr]
    return player_hand


# test case 1: two players with the same three of a kind, one player with a better kicker - player 1 wins
test_case_1_players[0].hand = generate_hand(["14 ♤", "5 ♤", "11 ♢", "12 ♤", "7 ♡", "5 ♧", "5 ♢"])  # three of a kind 5, 14, 12 kickers
test_case_1_players[1].hand = generate_hand(["4 ♧", "10 ♢", "11 ♢", "12 ♤", "7 ♡", "5 ♧", "5 ♢"])
test_case_1_players[2].hand = generate_hand(["2 ♤", "2 ♡", "11 ♢", "12 ♤", "7 ♡", "5 ♧", "5 ♢"])
test_case_1_players[3].hand = generate_hand(["5 ♡", "10 ♤", "11 ♢", "12 ♤", "7 ♡", "5 ♧", "5 ♢"])  # three of a kind 5, 12, 11 kickers
test_case_1_players[4].hand = generate_hand(["7 ♧", "4 ♡", "11 ♢", "12 ♤", "7 ♡", "5 ♧", "5 ♢"])
test_case_1_players[5].hand = generate_hand(["3 ♢", "14 ♡", "11 ♢", "12 ♤", "7 ♡", "5 ♧", "5 ♢"])
test_case_1_players[6].hand = generate_hand(["10 ♧", "11 ♡", "11 ♢", "12 ♤", "7 ♡", "5 ♧", "5 ♢"])
test_case_1_players[7].hand = generate_hand(["9 ♡", "6 ♧", "11 ♢", "12 ♤", "7 ♡", "5 ♧", "5 ♢"])


# test case 2: three players with three of a kind, one player with the highest three of a kind  - player 7 wins
test_case_2_players[0].hand = generate_hand(["5 ♧", "5 ♤", "11 ♢", "10 ♧", "7 ♡", "14 ♤", "5 ♢"])  # three of a kind 5,
test_case_2_players[1].hand = generate_hand(["4 ♧", "10 ♢", "11 ♢", "10 ♧", "7 ♡", "14 ♤", "5 ♢"])
test_case_2_players[2].hand = generate_hand(["2 ♤", "2 ♡", "11 ♢", "10 ♧", "7 ♡", "14 ♤", "5 ♢"])
test_case_2_players[3].hand = generate_hand(["5 ♡", "10 ♤", "11 ♢", "10 ♧", "7 ♡", "14 ♤", "5 ♢"])
test_case_2_players[4].hand = generate_hand(["7 ♧", "4 ♡", "11 ♢", "10 ♧", "7 ♡", "14 ♤", "5 ♢"])
test_case_2_players[5].hand = generate_hand(["3 ♢", "14 ♡", "11 ♢", "10 ♧", "7 ♡", "14 ♤", "5 ♢"])
test_case_2_players[6].hand = generate_hand(["11 ♤", "11 ♡", "11 ♢", "10 ♧", "7 ♡", "14 ♤", "5 ♢"])  # three of a kind 11
test_case_2_players[7].hand = generate_hand(["9 ♡", "6 ♧", "11 ♢", "10 ♧", "7 ♡", "14 ♤", "5 ♢"])


set_hand_value(test_case_1_players)
set_hand_value(test_case_2_players)


test_case_1_expected_result = [test_case_1_players[0]]
actual_result = three_of_a_kind_tie_breaker(test_case_1_players)
assert actual_result == test_case_1_expected_result, \
    f"Test case 1 failed. Expected : {test_case_1_expected_result}, got: {actual_result}"
print("Test case 1 passed.")

test_case_2_expected_result = [test_case_2_players[6]]
actual_result = three_of_a_kind_tie_breaker(test_case_2_players)
assert actual_result == test_case_2_expected_result, \
    f"Test case 2 failed. Expected : {test_case_2_expected_result}, got: {actual_result}"
print("Test case 2 passed.")
