class Bot:
    def __init__(self, exchange, strategies):
        self.exchange = exchange
        self.strategies = [eval("import strategies." + strategy) for strategy in strategies]

    def run(self):
        """
        infinite loop while connected
        :return:
        """
        data = self.exchange.read()
        while data:
            trades = []
            for strategy in self.strategies:
                trades.extend(eval(strategy).trade(self.exchange))
            self.exchange.trade_batch(trades)
            data = self.exchange.read()
