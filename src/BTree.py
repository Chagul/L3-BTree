class BTree:
    
    def __init__(self, root, L, U):
        self.root = root
        self.nbKeysMin = L-1
        self.nbKeysMax = U-1

    def isValid(self):
        if not self.isLinear():
            return False
        for Node in root.childrens:
            None
        return True

    def recherche(self, valueSearched):
        None

    def isLinear(self):
        list = []
        self.linearize(self.root,list)
        for i in range(len(list) - 1):
            firstKey = list[i]
            secondKey = list[i+1]
            if secondKey > firstKey:
                return False
        return True

    def linearize(self,node,list):
        if node.isLeaf:
            return list.extend(node.keys) 
        for i in range(len(node.keys) + 1):
            self.linearize(node.children[i],list)
            if i != len(node.keys):
                list.append(node.keys[i])
