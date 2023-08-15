from holdem_package.cards import Cards
from cards_index import card_index
from holdem_package.players import Players
from holdem_package.hand_evaluation import set_hand_value
from holdem_package.tiebreaker import four_of_a_kind_tiebreaker


test_case_1_players = Players.generate_players(8)
deck = Cards.generate_deck()


def generate_hand(hand_repr):
    player_hand = [deck[card_index[card]] for card in hand_repr]
    return player_hand


# all players have four of a kind, but player 5 has the highest kicker, 14 ♤ - player 5 wins
test_case_1_players[0].hand = generate_hand(["4 ♡", "6 ♢", "5 ♡", "5 ♢", "5 ♤", "5 ♧", "9 ♧"])
test_case_1_players[1].hand = generate_hand(["3 ♡", "13 ♧", "5 ♡", "5 ♢", "5 ♤", "5 ♧", "9 ♧"])
test_case_1_players[2].hand = generate_hand(["2 ♢", "11 ♤", "5 ♡", "5 ♢", "5 ♤", "5 ♧", "9 ♧"])
test_case_1_players[3].hand = generate_hand(["7 ♤", "8 ♡", "5 ♡", "5 ♢", "5 ♤", "5 ♧", "9 ♧"])
test_case_1_players[4].hand = generate_hand(["9 ♡", "14 ♤", "5 ♡", "5 ♢", "5 ♤", "5 ♧", "9 ♧"])  # player 5 has the highest kicker
test_case_1_players[5].hand = generate_hand(["7 ♡", "10 ♧", "5 ♡", "5 ♢", "5 ♤", "5 ♧", "9 ♧"])
test_case_1_players[6].hand = generate_hand(["10 ♢", "9 ♤", "5 ♡", "5 ♢", "5 ♤", "5 ♧", "9 ♧"])
test_case_1_players[7].hand = generate_hand(["7 ♧", "6 ♤", "5 ♡", "5 ♢", "5 ♤", "5 ♧", "9 ♧"])


set_hand_value(test_case_1_players)


expected_result = [test_case_1_players[4]]
actual_result = four_of_a_kind_tiebreaker(test_case_1_players)

assert expected_result == actual_result, f"Test case 1 failed. Expected {expected_result}, got {actual_result}"
print("Test case 1 passed.")
