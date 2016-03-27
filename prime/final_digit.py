from collections import defaultdict

import numpy as np
import pandas as pd
from primesieve.numpy import generate_n_primes_array
import primesieve

__author__ = 'rheineke'


def next_digit_after_digit_series(last_digit_srs, last_digit):
    # Count last digits of next prime after last_digit
    lst_digit_label = last_digit_srs == last_digit
    after_lst_digit_label = lst_digit_label.shift().fillna(False)
    return last_digit_srs.loc[after_lst_digit_label].value_counts()


def numpy_main(n_primes):
    prime_srs = pd.Series(generate_n_primes_array(n_primes))
    lst_digit_srs = prime_srs % 10
    # Count number of each last digit
    cnt_lst_digit_srs = lst_digit_srs.value_counts()
    # Count last digits of next prime after 1
    next_after_one_srs = next_digit_after_digit_series(lst_digit_srs, 1)
    # Count last digits of next prime after 3
    next_after_three_srs = next_digit_after_digit_series(lst_digit_srs, 3)


if __name__ == '__main__':
    # n_primes = 100000000
    n_primes = 1000000000

    prime_lst_digits = [1, 3, 5, 7, 9]
    count_dict = dict((d, 0) for d in prime_lst_digits)
    next_last_digit = dict((p, count_dict.copy()) for p in prime_lst_digits)

    it = primesieve.Iterator()
    num_primes = 0
    prev_lst_digit = np.nan
    while num_primes < n_primes:
        prime = it.next_prime()
        lst_digit = prime % 10
        # Update counts
        if pd.notnull(prev_lst_digit):
            next_last_digit[prev_lst_digit][lst_digit] += 1
        # Update references
        num_primes += 1
        prev_lst_digit = lst_digit

    next_df = pd.DataFrame(next_last_digit)
