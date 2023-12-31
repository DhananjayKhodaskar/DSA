# Question Link - https://www.algoexpert.io/questions/min-number-of-coins-for-change

# O(nd) time | O(n) space
def minNumberOfCoinsForChange(n, denoms):
    numOfCoins = [float('inf') for amount in range(n + 1)]
    numOfCoins[0] = 0

    for denom in denoms:
        for amount in range(1,len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] =  min(numOfCoins[amount],1 + numOfCoins[amount - denom])
    return numOfCoins[n] if  numOfCoins[n] != float('inf') else -1
