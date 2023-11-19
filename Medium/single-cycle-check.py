# Question Link -  https://www.algoexpert.io/questions/single-cycle-check

# O(n) Time | O(1) Space
def hasSingleCycle(array):
    currentIndex = 0
    elementVisitedTillNow = 0

    while elementVisitedTillNow < len(array):
        if elementVisitedTillNow > 0 and currentIndex == 0:
            return False
        elementVisitedTillNow +=1
        currentIndex = getNextIndex(currentIndex,array)
    return currentIndex ==  0

def getNextIndex(currentIndex,array):
    jump = array[currentIndex]

    nextIndex = (currentIndex + jump) % len(array)

    return nextIndex     
        
        
