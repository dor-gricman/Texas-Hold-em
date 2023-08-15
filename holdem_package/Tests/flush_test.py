from holdem_package.cards import Cards
from cards_index import card_index
from holdem_package.players import Players
from holdem_package.hand_evaluation import set_hand_value
from holdem_package.tiebreaker import flush_tie_breaker

test_case_1_players = Players.generate_players(8)
deck = Cards.generate_deck()


def generate_hand(hand_repr):
    player_hand = [deck[card_index[card]] for card in hand_repr]
    return player_hand


#  test case 1: all players have flush, one player has 6 ♢ instead of the common 2 ♢ - player 7 wins
test_case_1_players[0].hand = generate_hand(["11 ♡", "9 ♧", "10 ♢", "7 ♢", "13 ♢", "14 ♢", "2 ♢"])
test_case_1_players[1].hand = generate_hand(["10 ♤", "6 ♤", "10 ♢", "7 ♢", "13 ♢", "14 ♢", "2 ♢"])
test_case_1_players[2].hand = generate_hand(["9 ♡", "4 ♧", "10 ♢", "7 ♢", "13 ♢", "14 ♢", "2 ♢"])
test_case_1_players[3].hand = generate_hand(["3 ♧", "3 ♢", "10 ♢", "7 ♢", "13 ♢", "14 ♢", "2 ♢"])
test_case_1_players[4].hand = generate_hand(["13 ♡", "5 ♤", "10 ♢", "7 ♢", "13 ♢", "14 ♢", "2 ♢"])
test_case_1_players[5].hand = generate_hand(["6 ♧", "12 ♡", "10 ♢", "7 ♢", "13 ♢", "14 ♢", "2 ♢"])
test_case_1_players[6].hand = generate_hand(["5 ♡", "6 ♢", "10 ♢", "7 ♢", "13 ♢", "14 ♢", "2 ♢"])  # 6 ♢ instead of 2 ♢
test_case_1_players[7].hand = generate_hand(["2 ♤", "2 ♧", "10 ♢", "7 ♢", "13 ♢", "14 ♢", "2 ♢"])


set_hand_value(test_case_1_players)


test_case_1_expected_result = [test_case_1_players[6]]
actual_result = flush_tie_breaker(test_case_1_players)

assert actual_result == test_case_1_expected_result, \
    f"Test case 1 failed. Expected : {test_case_1_expected_result}, got: {actual_result}"
print("Test case 1 passed.")
