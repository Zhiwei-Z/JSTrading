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
    trades = []
    fast = 'VALBZ'
    slow = 'VALE'
    fast_book = books_dict[fast][0]
    slow_book = books_dict[slow][0]
    if fast_book and slow_book:
        # fpf = fair_price(fast_book)
        # fps = fair_price(slow_book)
        hb1, buy_size1 = highest_buy(slow_book)
        ls1, sell_size1 = lowest_sell(slow_book)
        fpf = (hb1 + ls1) / 2

        hb2, buy_size2 = highest_buy(fast_book)
        ls2, sell_size2 = lowest_sell(fast_book)
        fps = (hb2 + ls2) / 2
        if fpf > fps + 10:
            trades.append(('BUY', slow, hb2 + 1, buy_size2))
            trades.append(('CONVERT', 'SELL', slow, buy_size2))
            trades.append(('SELL', fast, ls1 - 1, buy_size2))
        if fpf + 10 < fps:
            trades.append(('BUY', fast, hb1 + 1, buy_size1))
            trades.append(('CONVERT', 'SELL', fast, buy_size1))
            trades.append(('SELL', slow, ls2 - 1, buy_size1))

        return trades
    