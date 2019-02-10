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


def trade(exchange):
    books_dict = exchange.latest_books
    # data = exchange1.last_data
    # trades = []
    # if data['type'] == 'book' and data['symbol'] == 'VALBZ':
    #     bids = data['buy']
    #     for price, size in bids:
    #         if price > 1000:
    #             trades.append(('SELL', 'BOND', price, size))
    #
    #     asks = data['sell']
    #     for price, size in asks:
    #         if price < 1000:
    #             trades.append(('BUY', 'BOND', price, size))
    # return trades
    trades = []
    fast = 'VALBZ'
    slow = 'VALE'
    fast_book = books_dict[fast][0]
    slow_book = books_dict[slow][0]
    if fast_book and slow_book:
        fp = fair_price(fast_book)
        hb, buy_size = highest_buy(slow_book)
        ls, sell_size = lowest_sell(slow_book)
        if hb > fp:
            trades.append(('SELL', slow, hb+1, buy_size))
            trades.append(('BUY', fast, ls-1, buy_size/2))
        if ls < fp:
            trades.append(('BUY', slow, ls-1, sell_size))
            trades.append(('SELL', fast, hb+1, sell_size/2))

    return trades
