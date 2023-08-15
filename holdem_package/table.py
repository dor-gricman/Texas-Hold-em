from typing import List
from holdem_package.bets import raising, call, sum_to_call
from holdem_package.dealer import deal_pre_flop, deal_flop, deal_turn, deal_river
from holdem_package.hand_evaluation import set_hand_value, set_hand_name
from holdem_package.pot import Pot
from holdem_package.players import Players
from holdem_package.user_prompts import calling_player_action_prompt, raise_amount_prompt, \
    checking_player_action_prompt


class Table:
    def __init__(self, small_blind: int, big_blind: int, players: List[Players], main_pot: Pot):
        self.big_blind = big_blind
        self.small_blind = small_blind
        self.players = [player for player in players if player.balance > 0]
        self.deck = []
        self.main_pot = main_pot
        self.side_pot = []
        self.current_bet = 0
        self.in_game_players = [player for player in self.players if player.in_game]

    def blinds(self):
        self.players[1].balance -= self.big_blind
        self.players[0].balance -= self.small_blind
        self.players[1].bet += self.big_blind
        self.players[0].bet += self.small_blind
        self.current_bet = self.big_blind
        self.main_pot.total += (self.big_blind + self.small_blind)

    def special_round(self):
        """special round for pre-flop where the round start with uneven bets due to blinds bets"""
        while any(
                player.bet != self.current_bet for player in self.players if
                player.in_game and not player.is_all_in):  # as long as not all players have the same bet, the round will continue
            player_turn = self.players[2:] + self.players[:2]  # guarantee that the round will start with the player after the big blind
            for player in player_turn:
                if player.in_game and not player.is_all_in:
                    if sum_to_call(player, self) == 0 and self.current_bet > self.big_blind:
                        continue
                    elif player == player_turn[-1] and self.current_bet == self.big_blind:
                        player_action = checking_player_action_prompt(player)
                        if player_action == 'call':
                            call(player, self)
                        elif player_action == 'raise':
                            raise_amount = raise_amount_prompt(player, sum_to_call(player, self))
                            raising(raise_amount, player, self)
                        elif player_action == 'fold':
                            player.fold()
                        else:
                            pass

                    else:
                        player_action = calling_player_action_prompt(player, sum_to_call(player, self))
                        if player_action == 'call':
                            call(player, self)
                        elif player_action == 'raise':
                            raise_amount = raise_amount_prompt(player, sum_to_call(player, self))
                            raising(raise_amount, player, self)
                        elif player_action == 'fold':
                            player.fold()

                else:
                    continue

    def common_round(self):
        """common round for flop, turn and river where the round start with even bets"""
        for index, player in enumerate(self.players):
            if sum_to_call(player,self) == 0 and player.in_game and not player.is_all_in:
                player_action = checking_player_action_prompt(player)
                if player_action == 'raise':
                    raise_amount = raise_amount_prompt(player, sum_to_call(player, self))
                    raising(raise_amount, player, self)
                    while any(p.bet != self.current_bet for p in self.players if p.in_game and not p.is_all_in):  # as long as not all players have the same bet, the round will continue
                        player_turn = self.players[index + 1:] + self.players[:index + 1]
                        for p in player_turn:
                            if p.in_game and not p.is_all_in:
                                if p.bet != self.current_bet:
                                    player_action = calling_player_action_prompt(p, sum_to_call(p, self))
                                    if player_action == 'call':
                                        call(p, self)
                                    elif player_action == 'raise':
                                        raise_amount = raise_amount_prompt(p, sum_to_call(p, self))
                                        raising(raise_amount, p, self)
                                    elif player_action == 'fold':
                                        p.fold()
                                    else:
                                        pass
                    break
                elif player_action == 'fold':
                    player.fold()
            else:
                continue

    def handle_side_pot(self):
        """ creates side pots in case of all in players with different bet amounts """
        all_in_players = [player for player in self.players if player.is_all_in and player.bet < self.current_bet]
        if all_in_players:
            all_in_bets = sorted([player.bet for player in all_in_players])
            for bet in all_in_bets:
                for player in self.players:
                    if player.bet == bet and player.in_game:
                        side_pot = Pot()
                        side_pot.pot_members = [player for player in self.players if player.bet >= bet]
                        side_pot.total = self.main_pot.total - sum([player.bet - bet for player in self.main_pot.pot_members if player.in_game])
                        self.main_pot.total -= side_pot.total
                        self.main_pot.pot_members = [player for player in self.players if player.bet > bet]
                        self.main_pot.bet = self.current_bet
                        self.side_pot.append(side_pot)
                    else:
                        continue

    def pre_flop(self):
        deal_pre_flop(self.deck, self.players)
        set_hand_value(self.players)
        set_hand_name(self.players)
        self.special_round()

    def flop(self):
        deal_flop(self.deck, self.players)
        set_hand_value(self.players)
        set_hand_name(self.players)
        self.common_round()

    def turn(self):
        deal_turn(self.deck, self.players)
        set_hand_value(self.players)
        set_hand_name(self.players)
        self.common_round()

    def river(self):
        deal_river(self.deck, self.players)
        set_hand_value(self.players)
        set_hand_name(self.players)

        self.common_round()

    def table_status(self):
        """print table status"""
        print(f' current bet is: {self.current_bet}')
        print(f' current pot is: {self.main_pot.total}')
        print(f' current players in pot: {self.main_pot.pot_members}')
        if self.side_pot:
            for pot in self.side_pot:
                print(f' side pot is {pot.total}')
                print(f' side pot members are {pot.pot_members}')

    def reset_table(self):
        """reset table after each round to the initial state and rotate players list"""
        self.players = [player for player in self.players if player.balance > 0]
        self.players = self.players[1:] + self.players[0:1]
        self.deck = []
        self.main_pot.total = 0
        self.main_pot.pot_members = self.players
        self.main_pot.bet = 0
        self.side_pot = []
        self.current_bet = 0
        for player in self.players:
            player.bet = 0
            player.is_all_in = False
            player.in_game = True
            player.hand = []
            player.hand_name = ''
            player.hand_rank = 0
            player.best_sequence = []
            player.kickers = []
