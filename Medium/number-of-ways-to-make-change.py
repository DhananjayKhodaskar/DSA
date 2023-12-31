# Question Link - https://www.algoexpert.io/questions/number-of-ways-to-make-change
# O(nd) time | O(n) space where d is the number of denom where n is the target amount money.

def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n+1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(1,n+1):
            if denom <= amount:
                ways[amount] = ways[amount] + ways[amount - denom]
    return ways[n]
