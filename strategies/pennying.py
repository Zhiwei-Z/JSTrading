def trade(exchange):
    books_dict = exchange.last_books
    # format of data, {type, symbol, buy: [[prize, size],...], sell[[prize, size],...]}
    '''pennnying strategy is to always buy at best_bid + 1, sell at best_offer - 1.'''
    trades = []
    GSb = books_dict['GS'][0]
    MSb = books_dict['MS'][0]
    WFCb = books_dict['WFC'][0]
    best_bid = highest_buy(GSb)
    best_offer = lowest_sell(GSb)
    if best_bid[0] - 1 > best_offer[0] + 1:
        trades.append(('BUY', 'GS', best_offer[0] + 1, best_offer[1]))
        trades.append(('SELL', 'GS', best_bid[0] - 1, best_bid[1]))

    best_bid = highest_buy(MSb)
    best_offer = lowest_sell(MSb)
    if best_bid[0] - 1 > best_offer[0] + 1:
        trades.append(('BUY', 'MS', best_offer[0] + 1, best_offer[1]))
        trades.append(('SELL', 'MS', best_bid[0] - 1, best_bid[1]))

    best_bid = highest_buy(WFCb)
    best_offer = lowest_sell(WFCb)
    if best_bid[0] - 1 > best_offer[0] + 1:
        trades.append(('BUY', 'WFC', best_offer[0] + 1, best_offer[1]))
        trades.append(('SELL', 'WFC', best_bid[0] - 1, best_bid[1]))


    # if books_dict['type'] == 'book' and books_dict['symbol'] in ("GS", "MS", "WFC"):
    #     best_bid = highest_buy(books_dict)
    #     best_offer = lowest_sell(books_dict)
    #     if best_bid > best_offer:
    #         trades.append(('SELL', books_dict['symbol'], best_bid[0] + 1, 10))
    #         trades.append(('SELL', books_dict['symbol'], best_offer[0] - 1, 10))
    # return trades


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