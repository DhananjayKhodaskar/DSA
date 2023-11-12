# Question Link - https://www.algoexpert.io/questions/find-kth-largest-value-in-bst
# O(h + k) time | 0(h) space - where h is the height of the tree and k is the input

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0,0)
    reverseInorderTraversal(tree,k,treeInfo)
    return treeInfo.lastVisitedNode

def reverseInorderTraversal(tree,k,treeInfo):
    if tree is None or  treeInfo.nodeVisitedTillNow == k:
        return

    reverseInorderTraversal(tree.right,k,treeInfo)
    if treeInfo.nodeVisitedTillNow < k:
        treeInfo.nodeVisitedTillNow +=1
        treeInfo.lastVisitedNode = tree.value
        reverseInorderTraversal(tree.left,k,treeInfo)
    
    

class TreeInfo:
    def __init__(self,nodeVisitedTillNow,lastVisitedNode):
        self.nodeVisitedTillNow = nodeVisitedTillNow
        self.lastVisitedNode = lastVisitedNode
