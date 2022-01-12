class BTree():
    
    def __init__(self, root, L, U):
        self.root = root
        self.nbKeysMin = L-1
        self.nbKeysMax = U-1