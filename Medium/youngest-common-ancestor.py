# Question Link - https://www.algoexpert.io/questions/youngest-common-ancestor
# O(d) where d is the depth of the deepest node | O(1) space 

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne,topAncestor)
    depthTwo = getDescendantDepth(descendantTwo,topAncestor)

    if depthOne > depthTwo:
        return backtrackAncestorTree(descendantOne,descendantTwo,depthOne- depthTwo)
    else:
        return backtrackAncestorTree(descendantTwo,descendantOne,depthTwo - depthOne)

def getDescendantDepth(descendant,topAncestor):
    depth = 0

    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor

    return depth

def backtrackAncestorTree(lowerDescendant,higherDescendant,diff):

    while diff > 0:
        diff -= 1
        lowerDescendant = lowerDescendant.ancestor
        
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
        
    return lowerDescendant

