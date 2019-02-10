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
    return (lowest_sell(book)[0] + highest_buy(book)[0]) // 2


def trade(exchange):
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
        xfp = fair_price(XLFb)

        prediced_fair = (3 * bfp + 2 * gfp + 3 * mfp + 2 * wfp)
        # if prediced_fair > xfp + 100:
        #     trades.append(('BUY', 'XLF', xfp, 10))
        #     trades.append(('CONVERT', 'SELL', 'XLF', 10))
        #     trades.append(('SELL', 'BOND', bfp, 3))
        #     trades.append(('SELL', 'GS', gfp, 2))
        #     trades.append(('SELL', 'MS',mfp, 3))
        #     trades.append(('SELL', 'WFC', wfp, 2))
        #
        # elif prediced_fair + 100 < xfp:
        #     trades.append(('BUY', 'BOND', bfp, 3))
        #     trades.append(('BUY', 'GS', gfp, 2))
        #     trades.append(('BUY', 'MS', mfp, 3))
        #     trades.append(('BUY', 'WFC', wfp, 2))
        #     trades.append(('CONVERT', 'BUY', 'XLF', 10))
        #     trades.append(('SELL', 'XLF', xfp, 10))

        if prediced_fair > xfp + 100:
            trades.append(('BUY', 'BOND', bfp, 3))
            trades.append(('BUY', 'GS', gfp, 2))
            trades.append(('BUY', 'MS', mfp, 3))
            trades.append(('BUY', 'WFC', wfp, 2))
            trades.append(('CONVERT', 'BUY', 'XLF', 10))
            trades.append(('SELL', 'XLF', xfp, 10))

        elif prediced_fair + 100 < xfp:
            trades.append(('BUY', 'XLF', xfp, 10))
            trades.append(('CONVERT', 'SELL', 'XLF', 10))
            trades.append(('SELL', 'BOND', bfp, 3))
            trades.append(('SELL', 'GS', gfp, 2))
            trades.append(('SELL', 'MS', mfp, 3))
            trades.append(('SELL', 'WFC', wfp, 2))
    return trades
