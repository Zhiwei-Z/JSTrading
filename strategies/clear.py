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
    holdings = exchange.holdings
    # holds = holdings['XLF']
    trades = list()
    trades += clear(books_dict, holdings, 'GS')
    trades += clear(books_dict, holdings, 'MS')
    trades += clear(books_dict, holdings, 'WFC')
    trades += clear(books_dict, holdings, 'XLF')
    trades += clear(books_dict, holdings, 'VALE')
    trades += clear(books_dict, holdings, 'VALBZ')

    return trades


def clear(books_dict, holdings, stock):
    trades = list()
    book = books_dict[stock][0]
    holdings = holdings[stock]
    if book and holdings:
        low_sell = lowest_sell(book)
        high_buy = highest_buy(book)
        if holdings > 0:
            trades.append(('SELL', stock, high_buy[0] - 1, holdings))

        if holdings < 0:
            trades.append(('BUY', stock, low_sell[0] + 1, -holdings))

    return trades



