class Node():

    def __init__(self, keys, children, parent, isLeaf):
        self.nbKeys = len(keys)
        self.keys = keys
        self.children = children
        self.parent = parent
        self.isLeaf = False

    def setIsLeaf(self, isLeaf):
        self.isLeaf = isLeaf
    
    def getChildrens(self):
        return self.children