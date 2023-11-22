# Question Link - https://www.algoexpert.io/questions/union-find

class UnionFind:
    def __init__(self):
        self.parents = {}

    # O(1) time | O(1) space
    def createSet(self, value):
        self.parents[value] = value

    # O(1) time(aprox) | O(1) space
    def find(self, value):
        if value not in self.parents:
            return None
            
        if value != self.parents[value]:
            self.parents[value] = self.find(self.parents[value])
        
            
        return self.parents[value]

    # O(1) time(aprox) | O(1) space
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return 
            
        valueOneRoot = self.find(valueOne)
        valueTwoRoot = self.find(valueTwo)
        self.parents[valueOneRoot] = valueTwoRoot
        
