# This file contains all the user prompts for the game

def calling_player_action_prompt(player, call_value):
    while True:
        action = input(f'{player.name}, your hand is {player.hand},\n'
                       f'hand name: {player.hand_name},\nyou need to call {call_value},\n'
                       f'your balance is {player.balance},\n'
                       f'What would you like to do: fold, call, or raise? ')
        if action in ['call', 'raise', 'fold']:
            return action
        else:
            print("Invalid action. Please enter a valid action.")


def checking_player_action_prompt(player):
    while True:
        action = input(f'{player.name}, your hand is {player.hand},\n'
                       f'hand name: {player.hand_name},\n'
                       f'your balance is {player.balance},\n'
                       f'What would you like to do: check, raise, or fold? ')
        if action in ['check', 'raise', 'fold']:
            return action
        else:
            print("Invalid action. Please enter a valid action.")


def raise_amount_prompt(player, call_value):
    while True:
        try:
            raise_value = int(input(f'{player.name}, how much do you want to raise: '))
            if raise_value + call_value > player.balance:
                answer = input(f"You don't have enough money. your max raise value is {player.balance - call_value}, would you like to go all in? y/n.")
                while answer not in ['y', 'n']:
                    answer = input("Invalid input. Please enter 'Y' or 'N':")
                if answer == 'y':
                    player.all_in()
                    return player.balance - call_value
                elif answer == 'n':
                    answer = input("how much do you want to raise:")
                    return answer
            return raise_value
        except ValueError:
            print("Invalid input. Please enter a number.")


def welcome():
    print("Welcome to The Poker Room")
    while True:
        try:
            number_of_players = int(input('How many players will play: '))
            if number_of_players < 2:
                print('Minimum number of players is 2')
                continue
            elif number_of_players > 12:
                print('Maximum number of players is 12')
                continue
            else:
                break
        except ValueError:
            print('Please enter a number')
    return number_of_players
