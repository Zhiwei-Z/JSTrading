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
    XLFb = books_dict['XLF'][0]
    trades = list()
    if XLFb:
        trades.append(('BUY', 'XLF', lowest_sell(XLFb)[0] + 1, 1))
    return trades
