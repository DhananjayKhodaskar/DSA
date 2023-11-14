# Question Link - https://www.algoexpert.io/questions/split-binary-tree

# Time Complexity - O(n) where n is the number of nodes in the tree.
# Space Complexity - O(h) where h is the height of the binary tree.

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def splitBinaryTree(tree):
    desiredSubtreeSum = getTreeSum(tree) / 2
    _,canBeSplit = trySubtree(tree,desiredSubtreeSum)
    return desiredSubtreeSum if canBeSplit else 0

def trySubtree(tree,desiredSubtreeSum):
    if tree is None:
        return (0,False)
        
    leftSum,leftCanBeSplit = trySubtree(tree.left,desiredSubtreeSum)
    rightSum,rightCanBeSplit = trySubtree(tree.right,desiredSubtreeSum)

    currSum = leftSum + rightSum + tree.value
    canBeSplit =  leftCanBeSplit or rightCanBeSplit or currSum == desiredSubtreeSum
    return (currSum,canBeSplit)
    
    

def getTreeSum(tree):
    if tree is None:
        return 0

    return tree.value + getTreeSum(tree.left) + getTreeSum(tree.right)

