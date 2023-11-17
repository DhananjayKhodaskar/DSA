# Question Link - https://www.algoexpert.io/questions/number-of-ways-to-traverse-graph

# O(n * m) time | O(n * m) space
def numberOfWaysToTraverseGraph(width, height):
    numberOfWays = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

    for widthIdx in range(1,width + 1):
        for heightIdx in range(1,height + 1):
            if widthIdx == 1 or heightIdx == 1:
                numberOfWays[heightIdx][widthIdx] = 1
            else:
                numberOfWays[heightIdx][widthIdx] = numberOfWays[heightIdx - 1][widthIdx] + numberOfWays[heightIdx][widthIdx - 1]
    return numberOfWays[height][width]
