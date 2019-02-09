from strategies import pennying

class Test:
    def __init__(self, b):
        self.latest_books = b

book_dict = {'BOND': [{'buy': [[998, 6]],
           'sell': [[1001, 11], [1002, 13]],
           'symbol': 'BOND',
           'type': 'book'}],
 'GS': [{'buy': [[8384, 1], [8383, 1], [8382, 3], [8381, 4], [8380, 1]],
         'sell': [[8387, 2], [8389, 4], [8390, 3], [8391, 1]],
         'symbol': 'GS',
         'type': 'book'}],
 'MS': [{'buy': [[3926, 2], [3925, 1]],
         'sell': [[3929, 9], [3930, 12], [3931, 11]],
         'symbol': 'MS',
         'type': 'book'}],
 'VALBZ': [{'buy': [[4215, 15], [4212, 10]],
            'sell': [[4216, 5], [4217, 19]],
            'symbol': 'VALBZ',
            'type': 'book'}],
 'VALE': [{'buy': [[4208, 1], [4196, 1], [4194, 7], [4191, 1]],
           'sell': [[4212, 2], [4221, 1], [4232, 6]],
           'symbol': 'VALE',
           'type': 'book'}],
 'WFC': [{'buy': [[5545, 2], [5544, 8]],
          'sell': [[5547, 11], [5548, 8], [5549, 5]],
          'symbol': 'WFC',
          'type': 'book'}],
 'XLF': [{'buy': [[4264, 2],
                  [4260, 1],
                  [4258, 2],
                  [4253, 2],
                  [4252, 1],
                  [4248, 2],
                  [4244, 1],
                  [4243, 3],
                  [4242, 1]],
          'sell': [[4301, 2], [4305, 1], [4320, 1]],
          'symbol': 'XLF',
          'type': 'book'}]}

t = Test(book_dict)
print(pennying.trade(t))