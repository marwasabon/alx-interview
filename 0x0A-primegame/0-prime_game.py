#!/usr/bin/python3
"""
Module: Prime Number Selection Game
"""


def find_primes(limit):
    """Generate a list of prime numbersi
    from 1 to the specified limit (inclusive).
    """
    primes = []
    is_prime = [True] * (limit + 1)

    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num, limit + 1, num):
                is_prime[multiple] = False

    return primes


def isWinner(rounds, upper_limits):
    """
    Identify the winner of the Prime Game.
    """
    if (rounds is None or
            upper_limits is None or
            rounds == 0 or
            not upper_limits):
        return None
    score_maria, score_ben = 0, 0

    for i in range(rounds):
        prime_list = find_primes(upper_limits[i])
        if len(prime_list) % 2 == 0:
            score_ben += 1
        else:
            score_maria += 1

    if score_maria > score_ben:
        return 'Maria'
    elif score_ben > score_maria:
        return 'Ben'

    return None
