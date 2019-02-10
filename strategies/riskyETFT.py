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
    '''
    3 BOND
    2 GS
    3 MS
    2 WFC
    '''
    books_dict = exchange.latest_books
    holdings = exchange.holdings
    holds = holdings['XLF']
    trades = []
    # Bondb = books_dict['BOND'][0]
    GSb = books_dict['GS'][0]
    MSb = books_dict['MS'][0]
    WFCb = books_dict['WFC'][0]
    XLFb = books_dict['XLF'][0]
    if GSb and MSb and WFCb and XLFb:
        bfp = 1000
        gfp = fair_price(GSb)
        mfp = fair_price(MSb)
        wfp = fair_price(WFCb)

        # fp = fair_price(fast_book)
        # hb, buy_size = highest_buy(slow_book)
        # ls, sell_size = lowest_sell(slow_book)
        # if hb > fp:
        #     trades.append(('SELL', slow, hb, buy_size))
        # if ls < fp:
        #     trades.append(('BUY', slow, ls, sell_size))

        lowest_sell_xlf, sell_size = lowest_sell(XLFb)
        highest_buy_xlf, buy_size = highest_buy(XLFb)
        # xfp = (lowest_sell_xlf[0] + highest_buy_xlf[0]) / 2

        predicted_fp = (3 * bfp + 2 * gfp + 3 * mfp + 2 * wfp) / 10

        if highest_buy_xlf > predicted_fp and holds > -50:
            trades.append(('SELL', 'XLF', highest_buy_xlf - 1, buy_size))
        if lowest_sell_xlf < predicted_fp and holds < 50:
            trades.append(('BUY', 'XLF', lowest_sell_xlf + 1, sell_size))
    return trades

