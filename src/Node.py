class Node():

    def __init__(self, keys, children, parent):
        self.nbKeys = len(keys)
        self.keys = keys
        self.children = children
        self.parent = parent