# Contains helper functions for your apps!
import os
from os import listdir, remove


# If the io following files are in the current directory, remove them!
# 1. 'currency_pair.txt'
# 2. 'currency_pair_history.csv'
# 3. 'trade_order.p'
def check_for_and_del_io_files():
    try:
        os.remove('currency_pair.txt')
    except IOError:
        print('no txt detected!')
    try:
        os.remove('currency_pair_history.csv')
    except IOError:
        print('no csv detected!')
    try:
        os.remove('trade_order.p')
    except IOError:
        print('no p detected!')

    pass  # nothing gets returned by this function, so end it with 'pass'.
