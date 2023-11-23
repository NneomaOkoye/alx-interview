#!/usr/bin/python3
'''
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given total total.
'''


def makeChange(coins, total):
    """
    For a given few coins

    Args:
        coins: List of coin denominations available.
        total: Integer value for the target total.

    Returns:
        Integer: The fewest number of coins needed to meet the total.
        If the total is 0 or less, return 0.
        If the total cannot be met by any number of coins available, return -1.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort the coin denominations in descending order
    num_coins = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1

    return num_coins if total == 0 else -1
