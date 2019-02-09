def trade(exchange):
    data = exchange.last_data
    # format of data, {type, symbol, buy: [[prize, size],...], sell[[prize, size],...]}
    '''pennnying strategy is to always buy at best_bid + 1, sell at best_offer - 1.'''
    trades = []
    if data['type'] == 'book' and data['symbol'] == "GS":
        bids = data['buy']
        best_bid = bids[0]
        trades.append(('SELL', data['symbol'], best_bid[0] + 1, 10))

        offers = data['sell']
        best_offer = offers[0]
        trades.append(('SELL', data['symbol'], best_offer[0] - 1, 10))
    return trades