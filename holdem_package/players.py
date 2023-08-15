
class Players:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = []
        self.bet = 0
        self.in_game = True
        self.is_all_in = False
        self.hand_rank = 0
        self.hand_name = ""
        self.best_sequence = []
        self.kickers = []

    def fold(self):
        self.in_game = False

    def all_in(self):
        self.is_all_in = True

    def __repr__(self):
        return self.name

    @staticmethod
    def generate_players(num):
        players_list = []
        for i in range(1, num + 1):
            player_name = f'player {i}'
            players_list.append(Players(player_name, 1000))
        return players_list
