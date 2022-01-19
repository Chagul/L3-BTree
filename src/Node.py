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

    def searchKey(self,key):
        if(key in self.keys):
            return True
        return False
