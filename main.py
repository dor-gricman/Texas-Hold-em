import random
from holdem_package.cards import Cards
from holdem_package.players import Players
from holdem_package.hand_evaluation import set_hand_value, set_hand_name
from holdem_package.pot import Pot
from holdem_package.winner import evaluate_winner, pot_to_winner
from holdem_package.table import Table
from holdem_package.user_prompts import welcome

if __name__ == "__main__":
    number_of_players = welcome()
    players = Players.generate_players(number_of_players)
    main_pot = Pot()
    main_pot.pot_members = players
    table = Table(5, 10, players, main_pot)

    while len(table.players) > 1:
        deck = Cards.generate_deck()
        random.shuffle(deck)
        table.deck = deck
        table.blinds()
        set_hand_value(table.players)
        set_hand_name(table.players)

        while len(table.in_game_players) > 1:
            table.pre_flop()
            table.flop()
            table.turn()
            table.river()
            table.handle_side_pot()

            if len(table.in_game_players) == 1:
                winner = table.in_game_players[0]
                print(f'{winner.name} is the winner of this round with {winner.hand_name}')
                pot_to_winner(winner, table.main_pot)
                table.reset_table()

            elif not table.side_pot:
                winner = evaluate_winner(table.main_pot.pot_members)
                pot_to_winner(winner, table.main_pot)
                print(f'{winner} is the winner of this round with {winner[0].hand_name}')
                table.reset_table()

            else:
                for pot in table.side_pot:
                    winner = evaluate_winner(pot.pot_members)
                    print(f'{winner} is the winner of the side pot {winner[0].hand_name}')
                    pot_to_winner(winner, pot)

                if table.main_pot.total > 0:
                    winner = evaluate_winner(table.main_pot.pot_members)
                    print(f'{winner} is the winner of the main pot with {winner[0].hand_name}')
                    pot_to_winner(winner, table.main_pot)
                    table.reset_table()
                else:
                    table.reset_table()
    print("not enough players to continue")
