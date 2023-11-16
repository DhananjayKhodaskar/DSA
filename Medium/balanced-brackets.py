#Question Link - https://www.algoexpert.io/questions/balanced-brackets

# O(n) Time | O(n) Space
def balancedBrackets(string):
    openingBrackets = "([{"
    stack = []
    closingBrackets = ")}]"
    matchingBrackets = {")":"(","]":"[","}":"{"}
    
    for bracket in string:
        if bracket in openingBrackets:
            stack.append(bracket)
            
        elif bracket in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBrackets[bracket]:
                stack.pop()
            else:
                return False
           
       
            
    return len(stack) == 0
