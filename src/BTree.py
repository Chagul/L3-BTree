class BTree:
    
    def __init__(self, root, L, U):
        self.root = root
        minKey = L - 1 
        maxKey = L - 1
        if minKey <= 0 or maxKey <= 0 or maxKey < minKey :
            raise Exception("Invalid L or U value")
        self.nbKeysMin = L-1
        self.nbKeysMax = U-1

    def isValid(self):
        return self.isLinear() and self.isBalanced() and self.rightNumberOfKeys(self.root)

    def recherche(self, valueSearched):
        None

    def isLinear(self):
        list = []
        self.linearize(self.root,list)
        for i in range(len(list) - 1):
            firstKey = list[i]
            secondKey = list[i+1]
            if secondKey < firstKey:
                return False
        return True

    def getHeight(self, node) :
        if not node.isLeaf :
            return 1 + self.getHeight(node.children[0])
        else :
            return 0

    def isBalanced(self) :
        if len(self.root.children) == 0 :
            return True
        firstHeight = self.getHeight(self.root.children[0])
        for i in (1, len(self.root.children)-1):
            if firstHeight != self.getHeight(self.root.children[i]) :
                return False
        return True

    def rightNumberOfKeys(self, node) : 
        bool = len(node.keys) <= self.nbKeysMax and len(node.keys) >= self.nbKeysMin
        if not bool :
            return False
        if node.isLeaf:
            return bool
        for i in range(len(node.keys) + 1):
             bool = bool and self.rightNumberOfKeys(node.children[i])
        return bool

    def linearize(self,node,list):
        if node.isLeaf:
            return list.extend(node.keys) 
        for i in range(len(node.keys) + 1):
            self.linearize(node.children[i],list)
            if i != len(node.keys):
                list.append(node.keys[i])
