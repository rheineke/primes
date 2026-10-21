import numpy as np
import pandas as pd
import primesieve

from prime.final_digit import next_digit_after_digit_series, numpy_main

FIRST_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def last_digits(primes):
    return pd.Series(np.asarray(primes)) % 10


def test_next_digit_after_three():
    # 3->5, 13->7, 23->9
    counts = next_digit_after_digit_series(last_digits(FIRST_PRIMES), 3)
    assert counts.to_dict() == {5: 1, 7: 1, 9: 1}


def test_next_digit_after_one():
    # 11->3, 31->7
    counts = next_digit_after_digit_series(last_digits(FIRST_PRIMES), 1)
    assert counts.to_dict() == {3: 1, 7: 1}


def test_last_prime_has_no_successor():
    counts = next_digit_after_digit_series(last_digits([3, 5, 7]), 7)
    assert counts.empty


def test_consecutive_primes_avoid_repeating_last_digit():
    # Lemke Oliver and Soundararajan (2016): a prime ending in 1 is followed
    # by another ending in 1 less often than by one ending in 3, 7 or 9.
    digits = last_digits(primesieve.n_primes(100_000))
    counts = next_digit_after_digit_series(digits, 1)
    assert counts[1] < min(counts[3], counts[7], counts[9])
    assert counts.sum() == (digits == 1).sum()


def test_numpy_main_runs():
    numpy_main(1000)
