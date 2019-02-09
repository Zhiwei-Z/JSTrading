import time
import argparse

import errno
from socket import error as socket_error

from Connection import ExchangeConnection
from Bot import Bot


def main(strategies, test=True):
    """
    Run bot with strategies as input
    :param strategies:
    :param test:
    :return:
    """
    exchange_connection = ExchangeConnection(test)  # flag for testing
    print("Successfully Connected")
    bot = Bot(exchange_connection, strategies)
    print("Bot Initialized")
    bot.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('strategies')
    parser.add_argument('--test', action='store_true', default=False)
    args = parser.parse_args()

    strategies = args.strategies.split(',')

    while True:
        try:
            main(strategies, args.test)
        except socket_error as serr:
            if serr.errno != errno.ECONNREFUSED:
                raise serr
            print("Connection Failed, Sleeping...")
            time.sleep(1)
