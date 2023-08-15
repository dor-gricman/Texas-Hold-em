
from holdem_package.Tests.flush_test import generate_hand
from holdem_package.players import Players
from holdem_package.hand_evaluation import set_hand_value, set_hand_name
from holdem_package.pot import Pot
from holdem_package.table import Table
from holdem_package.winner import evaluate_winner, pot_to_winner

test_case_1_players = Players.generate_players(6)

""" setting the hands of the players """

test_case_1_players[0].hand = generate_hand(["14 ♡", "3 ♤", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"]) # pair 3
test_case_1_players[1].hand = generate_hand(["2 ♤", "10 ♧", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])
test_case_1_players[2].hand = generate_hand(["9 ♤", "7 ♤", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])  # straight 6-10
test_case_1_players[3].hand = generate_hand(["11 ♤", "11 ♢", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"]) # pair jacks
test_case_1_players[4].hand = generate_hand(["9 ♡", "8 ♤", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])  # straight 6-10
test_case_1_players[5].hand = generate_hand(["11 ♧", "10 ♤", "3 ♧", "8 ♧", "10 ♢", "7 ♢", "6 ♡"])# pair 10


""" setting the balance of the players """

test_case_1_players[0].balance = 1000
test_case_1_players[1].balance = 1000
test_case_1_players[2].balance = 400
test_case_1_players[3].balance = 700
test_case_1_players[4].balance = 500
test_case_1_players[5].balance = 1000



main_pot = Pot()
""" creating table and passing the players, the blinds and the main pot. """
table = Table(5, 10, test_case_1_players, main_pot)

table.main_pot.pot_members = table.players

"""assigning the best hand of each player."""
set_hand_value(table.players)
set_hand_name(table.players)

""" setting the bets of the players and status of the players """
test_case_1_players[0].bet = 1000
test_case_1_players[0].balance = 0
test_case_1_players[0].is_all_in = True

table.current_bet = 1000
table.main_pot.total += 1000

test_case_1_players[1].bet = 0
test_case_1_players[1].in_game = False

test_case_1_players[2].bet = 400
test_case_1_players[2].balance = 0
test_case_1_players[2].is_all_in = True
table.main_pot.total += 400


test_case_1_players[3].bet = 700
test_case_1_players[3].balance = 0
test_case_1_players[3].is_all_in = True
table.main_pot.total += 700

test_case_1_players[4].bet = 500
test_case_1_players[4].balance = 0
test_case_1_players[4].is_all_in = True
table.main_pot.total += 500

test_case_1_players[5].bet = 1000
test_case_1_players[5].balance = 0
test_case_1_players[5].is_all_in = True
table.main_pot.total += 1000


assert table.main_pot.total == 3600, f'expected 3600, got {table.main_pot.total}'



table.handle_side_pot()
if len(table.in_game_players) == 1:
    winner = table.in_game_players[0]
    print(f'{winner.name} is the winner of this round with {winner.hand_name}')
    pot_to_winner(winner, table.main_pot)

elif not table.side_pot:
    winner = evaluate_winner(table.main_pot.pot_members)
    pot_to_winner(winner, table.main_pot)
    print(f'{winner} is the winner of this round with {winner[0].hand_name}')

else:
    for pot in table.side_pot:
        winner = evaluate_winner(pot.pot_members)
        print(f'side pot {winner} is the winner of this round with {winner[0].hand_name}')
        pot_to_winner(winner, pot)
        table.table_status()
    winner = evaluate_winner(table.main_pot.pot_members)
    print(f'main_pot{winner} is the winner of this round with {winner[0].hand_name}')
    pot_to_winner(winner, table.main_pot)

assert len(table.side_pot) == 3, f'expected 3, got {len(table.side_pot)}'


assert table.side_pot[0].total == 2000, f'expected 2000, got {table.side_pot[0].total}'
assert table.side_pot[0].pot_members == [test_case_1_players[0], test_case_1_players[2], test_case_1_players[3],
    test_case_1_players[4], test_case_1_players[5]], f'' \
    f'expected [test_case_1_players[0], test_case_1_players[2], test_case_1_players[3],' \
    f' test_case_1_players[4], test_case_1_players[5]], got {table.side_pot[0].pot_members}'

assert table.side_pot[1].total == 400, f'expected 400, got {table.side_pot[1].total}'
assert table.side_pot[1].pot_members == [test_case_1_players[0], test_case_1_players[3],
    test_case_1_players[4], test_case_1_players[5]],\
    f'expected [test_case_1_players[0], test_case_1_players[3], test_case_1_players[4],' \
    f' test_case_1_players[5]], got {table.side_pot[1].pot_members}'

assert test_case_1_players[0].balance == 0, f'expected 0, got {test_case_1_players[0].balance}'
assert test_case_1_players[1].balance == 1000, f'expected 1000, got {test_case_1_players[1].balance}'
assert test_case_1_players[2].balance == 1000, f'expected 1000, got {test_case_1_players[2].balance}'
assert test_case_1_players[3].balance == 600, f'expected 600, got {test_case_1_players[3].balance}'
assert test_case_1_players[4].balance == 1400, f'expected 1400, got {test_case_1_players[4].balance}'
assert test_case_1_players[5].balance == 600, f'expected 600, got {test_case_1_players[5].balance}'
print('test case 1 passed')





