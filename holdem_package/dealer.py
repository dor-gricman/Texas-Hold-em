def deal_pre_flop(deck, players):
    """deal two private cards to each player and remove them from the deck"""
    for player in players:
        player.hand = deck[0:2]
        del deck[0:2]


def deal_flop(deck, players):
    """deal three common cards and add them to every player's hand, then remove them from the deck"""
    flop_cards = deck[0:3]
    for player in players:
        if player.in_game:
            player.hand.extend(flop_cards)
            del deck[0:3]


def deal_turn(deck, players):
    """deal one common cards and add him to every player's hand, then remove him from the deck"""
    turn_card = deck[0:1]
    for player in players:
        if player.in_game:
            player.hand.extend(turn_card)
            del deck[0:1]


def deal_river(deck, players):
    """deal one common cards and add him to every player's hand, then remove him from the deck"""
    river_card = deck[0:1]
    for player in players:
        if player.in_game:
            player.hand.extend(river_card)
            del deck[0:1]
