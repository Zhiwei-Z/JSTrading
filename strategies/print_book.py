import numpy as np
def trade(exchange):
    data = exchange.last_data
    trades = []
    if np.random.random_sample() < 0.02:
        print(data)
    return []