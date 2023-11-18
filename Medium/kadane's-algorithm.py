# Question Link - https://www.algoexpert.io/questions/kadane's-algorithm

# O(n) Time | O(1) Space
def kadanesAlgorithm(array):
    maxTillHere = array[0]
    maxTillNow = array[0]

    for idx in range(1,len(array)):
        num = array[idx]
        maxTillHere = max(num,maxTillHere + num)
        maxTillNow = max(maxTillNow,maxTillHere)

    return maxTillNow
        
