# Question Link - https://www.algoexpert.io/questions/breadth-first-search

# O(e + v) Time | O(v) Space
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            currNode = queue.pop(0)
            for children in currNode.children:
                queue.append(children)
            array.append(currNode.name)
        return array
