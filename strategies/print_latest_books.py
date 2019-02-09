import numpy as np
import pprint as pp


def trade(exchange):
    books = exchange.latest_books
    if np.random.randint(1, 1000) == 1:
        pp.pprint(books)
    return []
