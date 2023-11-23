#!/usr/bin/python3
"""
This module contains the make change function
"""


def makeChange(coins, total):
    """returns fewest number of coins to meet total"""
    if total <= 0:
        return 0

    min_coins = [0] + [total + 1] * total

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[total] < total:
        return min_coins[total]

    return -1
