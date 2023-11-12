# Question Link - https://www.algoexpert.io/questions/height-balanced-binary-tree
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    return getTreeInfo(tree).isBalanced

def getTreeInfo(tree):
    if tree is None:
        return TreeNode(True,0)

    left = getTreeInfo(tree.left)
    right = getTreeInfo(tree.right)

    isBalanced = left.isBalanced and right.isBalanced and abs(
    right.height -  left.height) <= 1
    currHeight  = max(left.height , right.height) + 1
    return TreeNode(isBalanced,currHeight)

class TreeNode:
    def __init__(self,isBalanced,height):
        self.isBalanced = isBalanced
        self.height = height


    
