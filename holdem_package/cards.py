class Cards:
    def __init__(self, value, suite, color):
        self.value = value
        self.suit = suite
        self.color = color

    def __repr__(self):
        card_symbols = {
            "diamond": '\u2662',
            "heart": '\u2661',
            "spade": '\u2664',
            "club": '\u2667',
        }
        card_symbol = card_symbols.get(self.suit)
        return f"{self.value} {card_symbol}"

    @staticmethod
    def generate_deck():
        deck = []
        suits = ["diamond", "heart", "spade", "club"]
        for s in suits:
            for val in range(2, 15):
                clr = "red" if s in ["diamond", "heart"] else "black"
                deck.append(Cards(val, s, clr))
        return deck



