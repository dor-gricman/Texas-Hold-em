class Pot:
    def __init__(self):
        self.total = 0
        self.pot_members = []
        self.pot_bet = 0

    def __repr__(self):
        return f'side pot: {self.pot_members}, total: {self.total}'
