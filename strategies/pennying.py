def trade(exchange):
    data = exchange.last_data
    # format of data, {type, symbol, buy: [[prize, size],...], sell[[prize, size],...]}
    '''pennnying strategy is to always buy at best_bid + 1, sell at best_offer - 1.'''
    trades = []
    if data['type'] == 'book' and data['symbol'] in ("GS", "MS", "WFC"):
        best_bid = highest_buy(data)
        best_offer = lowest_sell(data)
        if best_bid > best_offer:
            trades.append(('SELL', data['symbol'], best_bid[0] + 1, 10))
            trades.append(('SELL', data['symbol'], best_offer[0] - 1, 10))
    return trades


def lowest_sell(book):
    asks = book['sell']
    low = 100000000
    s = 0
    for price, size in asks:
        low = min(low, price)
        s = size
    return low, s


def highest_buy(book):
    bids = book['buy']
    h = 0
    s = 0
    for price, size in bids:
        h = max(h, price)
        s = size
    return h, s


def fair_price(book):
    return (lowest_sell(book)[0] + highest_buy(book)[0]) / 2