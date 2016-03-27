import pandas as pd
from primesieve.numpy import generate_n_primes_array

__author__ = 'rheineke'


def next_digit_after_digit_series(last_digit_srs, last_digit):
    # Count last digits of next prime after last_digit
    lst_digit_label = last_digit_srs == last_digit
    after_lst_digit_label = lst_digit_label.shift().fillna(False)
    return last_digit_srs.loc[after_lst_digit_label].value_counts()


if __name__ == '__main__':
    # n_primes = 100000000
    n_primes = 1000000000
    prime_srs = pd.Series(generate_n_primes_array(n_primes))
    lst_digit_srs = prime_srs % 10
    # Count number of each last digit
    cnt_lst_digit_srs = lst_digit_srs.value_counts()
    # Count last digits of next prime after 1
    next_after_one_srs = next_digit_after_digit_series(lst_digit_srs, 1)
    # Count last digits of next prime after 3
    next_after_three_srs = next_digit_after_digit_series(lst_digit_srs, 3)
