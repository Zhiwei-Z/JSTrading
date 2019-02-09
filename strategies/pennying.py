def trade(exchange):
    data = exchange.last_data
    # format of data, {type, symbol, buy: [[prize, size],...], sell[[prize, size],...]}
    '''pennnying strategy is to always buy at best_bid + 1, sell at best_offer - 1.'''
    trades = []
    if data['type'] == 'book' and data['symbol'] == "GS":
        bids = data['buy']
        if bids != []:
            best_bid = bids[0]
        offers = data['sell']
        if offers != []:
            best_offer = offers[0]
        if best_bid > best_offer:
            trades.append(('SELL', data['symbol'], best_bid[0] + 1, 10))
            trades.append(('SELL', data['symbol'], best_offer[0] - 1, 10))
    return trades
