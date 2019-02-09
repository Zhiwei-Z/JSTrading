import numpy as np


def trade(exchange):
    data = exchange.last_data
    trades = []
    if data['type'] == 'book' and data['symbol'] == 'BOND':
        print(data)
    return []
