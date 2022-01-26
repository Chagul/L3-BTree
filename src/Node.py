class Node:

    def __init__(self, keys, children):
        self.nbKeys = len(keys)
        self.keys = keys
        self.children = children
        self.parent = None
        self.isLeaf = len(self.children) == 0

    def setIsLeaf(self, isLeaf):
        self.isLeaf = isLeaf
    
    def getChildrens(self):
        return self.children

    def setKey(self,key):
        self.keys.extend(key)
        self.keys.sort()

    def setChildren(self, newChildrens):
        self.children = newChildrens