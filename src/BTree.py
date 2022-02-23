from Node import Node

class BTree:
    
    def __init__(self, root, L, U):
        self.root = root
        minKey = L - 1 
        maxKey = U - 1
        if minKey <= 0 or maxKey <= 0 or maxKey < minKey :
            raise Exception("Invalid L or U value")
        self.nbKeysMin = minKey
        self.nbKeysMax = maxKey

    def isValid(self):
        return self.isLinear() and self.isBalanced() and self.rightNumberOfKeys(self.root)

    def search(self, node, valueSearched):
        
        # si dans noeud courant
        if valueSearched in node.keys :
            return True
        #si il n'y a plus d'enfant, la valeur n'est pas là
        if len(node.children) == 0 or len(node.keys) <= 0 :
            return False
        #partie gauche de la premiere cléf
        if(valueSearched < node.keys[0]):
            return self.search(node.children[0], valueSearched)
        #partie droite de la dernière clef
        if(valueSearched >  node.keys[len(node.keys) -1 ]):
            return self.search(node.children[len(node.children)- 1], valueSearched)

        #pour chaque enfant
        for i in range(len(node.keys) - 1):
            rangeMaxKey = node.keys[i+1]
            possibleValues = range(node.keys[i], rangeMaxKey)
            #si la clef est entre la premiere clef et la derniere clef de l'enfant i
            if valueSearched in list(possibleValues) :
                return self.search(node.children[i+1], valueSearched)

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
        max = 0
        tmp = 0
        if node.isLeaf:
            return 0
        for child in node.children:
            tmp = 1 + self.getHeight(child)
            if tmp > max:
                max = tmp
        return max

    def isBalanced(self) :
        if len(self.root.children) == 0 :
            return True
        if( len(self.root.children) != len(self.root.keys) + 1):
            return False
        firstHeight = self.getHeight(self.root.children[0])
        for child in self.root.children:
            if firstHeight != self.getHeight(child) :
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

    def insert(self, node, valueToInsert):
        #si la valeur est déjà dans l'arbre, ne pas insérer
        if self.search(self.root, valueToInsert) :
            return False
        
        if node.isLeaf :
            #si pas besoin d'éclatement
            if len(node.keys) < self.nbKeysMax :
                node.keys.append(valueToInsert)
                return True
            #si besoin d'éclatement
            self.split(node)
            return self.insert(node, valueToInsert)

        elif valueToInsert < node.keys[0]:
            return self.insert(node.children[0], valueToInsert)
        elif valueToInsert > node.keys[len(node.keys) -1 ]:
            return self.insert(node.children[len(node.children)- 1], valueToInsert)
        else:
            for i in range(1,len(node.keys)):
                if valueToInsert < node.keys[i]:
                    return self.insert(node.children[i], valueToInsert)


        return True

    def split(self, node) :
        middle = len(node.keys)//2
        keyInParent = node.keys[middle]
        keysNewChildLeft = []
        keysNewChildRight = []
        
        for i in range(middle) :
            if(i < middle):
                keysNewChildLeft.append(node.keys[i])
            else: 
                keysNewChildRight.append(node.keys[i])
        
        newChildLeft = Node(keysNewChildLeft, [])
        newChildRight = Node(keysNewChildRight, [])
        
        for i in range(len(node.children)) :
            if(i < middle) :
                newChildLeft.children.append(node.children[i])
                node.children[i].parent = newChildLeft
            else :
                newChildRight.children.append(node.children[i])
                node.children[i].parent = newChildRight
        if(node.parent is None):
            newRoot = Node([keyInParent], [newChildLeft, newChildRight])
            self.root = newRoot
        else :
            print(node.children[0])
            print(node.children[1])
            node.parent.keys.append(node.keys[middle])
            node.keys.remove(node.keys[middle])
            if len(node.parent.keys) >= self.nbKeysMax :
                self.split(node.parent)
