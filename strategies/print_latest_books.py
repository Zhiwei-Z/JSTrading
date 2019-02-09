import numpy as np
def trade(exchange):
    books = exchange.latest_books
    if np.random.randint(1,100)==1:
        print(books)
    return []