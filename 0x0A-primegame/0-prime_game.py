#!/usr/bin/python3
'''
Game of primes: Determine the winner for each round
'''


def isWinner(x, nums):
    '''
    Determine the winner of each round

    Args:
        x (int): Number of rounds to play
        nums (list): List of integers representing the range of numbers for each rnd

    Returns:
        str or None: The name of the player with the most wins or None
    '''


    def rec(n):
        '''
        Play a single round of the game

        Args:
            n (int): The range of numbers for this round

        Returns:
            int: 1 if Maria wins, 2 if Ben wins
        '''
        if n == 1:
            return 2
        if n == 2:
            return 1

        count = 0
        for num in range(3, n + 1):
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                count += 1

        if count % 2:
            return 2
        return 1

    if x == 0 or len(nums) != x:
        return None

    maria = 0
    ben = 0

    for rnd in nums:
        result = rec(rnd)
        if result == 1:
            maria += 1
        else:
            ben += 1

    if maria == ben:
        return None
    elif maria > ben:
        return "Maria"
    else:
        return "Ben"
