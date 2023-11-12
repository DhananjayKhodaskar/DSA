# Question Link - https://www.algoexpert.io/questions/two-number-sum
# Time Complexity - O(n)
# Space Complexity - O(n)

def twoNumberSum(array, targetSum):
    mySet = set()
    res = []
    
    for element in array:
        if targetSum - element in mySet:
            res.append(element)
            res.append(targetSum -  element)
            return res
        else:
            mySet.add(element)
            
    return res
            
        
        
        
    
