#!/usr/bin/python3
"""
This module contains my solution to prime_game problem
"""


def isWinner(x, nums):
    """
    returns the winner of the game played by maria and ben

    parameters:
       x - number of rounds of game
       nums - array of numbers n

    return:
      name of player that won the most rounds
    """
    if x < 1 or not nums:
        return None
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(1 for i in range(2, n + 1) if is_prime(i))
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def is_prime(num):
    """check if a given number is a prime number"""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
