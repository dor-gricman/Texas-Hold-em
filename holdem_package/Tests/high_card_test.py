from holdem_package.players import Players
from holdem_package.cards import Cards
from cards_index import card_index
from holdem_package.hand_evaluation import set_hand_value
from holdem_package.tiebreaker import high_card_tiebreaker

test_case_1_players = Players.generate_players(4)

deck = Cards.generate_deck()


def generate_hand(hand_repr):
    player_hand = [deck[card_index[card]] for card in hand_repr]
    return player_hand


# test case 1 - all players have high card, one player has 14 ♡ - player 2 wins
test_case_1_players[0].hand = generate_hand(["5 ♤", "13 ♤", "3 ♡", "4 ♧", "9 ♢", "7 ♡", "11 ♧"])
test_case_1_players[1].hand = generate_hand(["12 ♢", "14 ♡", "3 ♡", "4 ♧", "9 ♢", "7 ♡", "11 ♧"])
test_case_1_players[2].hand = generate_hand(["8 ♢", "5 ♧", "3 ♡", "4 ♧", "9 ♢", "7 ♡", "11 ♧"])
test_case_1_players[3].hand = generate_hand(["12 ♤", "10 ♤", "3 ♡", "4 ♧", "9 ♢", "7 ♡", "11 ♧"])

set_hand_value(test_case_1_players)


test_case_expected_result = [test_case_1_players[1]]
actual_result = high_card_tiebreaker(test_case_1_players)
assert actual_result == test_case_expected_result, \
    f"Test case 1 failed. Expected : {test_case_expected_result}, got: {actual_result}"
print("Test case 1 passed.")
