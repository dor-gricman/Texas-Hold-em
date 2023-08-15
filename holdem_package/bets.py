def raising(raise_value, pl, table):
    call(pl, table)
    call_value = sum_to_call(pl, table)
    pl.bet += raise_value
    table.current_bet = pl.bet - call_value
    pl.balance -= raise_value - call_value
    table.main_pot.total += raise_value
    if pl.balance == 0:
        pl.all_in()


def call(pl, table):
    call_value = sum_to_call(pl, table)
    if call_value >= pl.balance:
        table.main_pot.total += pl.balance
        pl.bet += pl.balance
        pl.balance = 0
        pl.all_in()
    else:
        table.main_pot.total += call_value
        pl.balance -= call_value
        pl.bet += call_value


def sum_to_call(pl, table):
    return table.current_bet - pl.bet
