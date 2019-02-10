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
    # holdings = exchange.holdings
    # holds = holdings['XLF']
    trades = list()
    trades += trade_one(books_dict, 'GS')
    trades += trade_one(books_dict, 'MS')
    trades += trade_one(books_dict, 'WFC')
    return trades


def trade_one(books_dict, stock):
    trades = list()
    new_book = books_dict[stock][0]
    old_book = books_dict[stock][1]
    if new_book and old_book:
        new_low_sell = lowest_sell(new_book)
        new_high_buy = highest_buy(new_book)
        new_fair = (new_high_buy[0] + new_low_sell[0]) / 2

        old_low_sell = lowest_sell(old_book)
        old_high_buy = highest_buy(old_book)
        old_fair = (old_high_buy[0] + old_low_sell[0]) / 2

        if new_fair > old_fair and new_high_buy[0] + 1 < new_low_sell[0] - 1: # it's increasing
            trades.append(('BUY', stock, new_high_buy[0] + 1, 5))
            trades.append(('SELL', stock, new_low_sell[0] - 1, 5))

        # if new_fair < old_fair and new_high_buy[0] + 1 < new_low_sell[0] - 1: # it's increasing
        #     trades.append(('BUY', stock, 5, new_high_buy[0] + 1))
        #     trades.append(('SELL', stock, 5, new_low_sell[0] - 1))

    return trades



