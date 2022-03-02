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
        #Si c'est une feuille, on rajoute toute les clefs
        if node.isLeaf:
            return list.extend(node.keys) 
        #Pour chaque enfant, on rappelle la fonction
        for i in range(len(node.children)):
            self.linearize(node.children[i],list)
            if i != len(node.keys):
                list.append(node.keys[i])

    def insert(self, node, valueToInsert,searchDone):
        #si la valeur est déjà dans l'arbre, ne pas insérer
        if searchDone == False and self.search(self.root, valueToInsert) :
            searchDone = True
            return False
        if node.isLeaf :
            #si pas besoin d'éclatement
            indexToInsert = 0
            while indexToInsert < len(node.keys) and node.keys[indexToInsert] < valueToInsert:
                indexToInsert = indexToInsert + 1
            node.keys.insert(indexToInsert,valueToInsert)
            if len(node.keys) <= self.nbKeysMax :
                return True
            #si besoin d'éclatement
            self.split(node)
            return self.insert(node, valueToInsert,searchDone)
        #Si la valeur à inserer est inférieur à la clef la plus à gauche du noeud en cours
        elif valueToInsert < node.keys[0]:
            return self.insert(node.children[0], valueToInsert,searchDone)
        #Si la valeur à inserer est inférieur à la clef la plus à droite du noeud en cours
        elif valueToInsert > node.keys[len(node.keys) -1 ]:
            return self.insert(node.children[len(node.children)- 1], valueToInsert,searchDone)
        #Sinon on parcours les clefs pour trouver dans quel enfant aller par rapport aux clefs du noeud en cours
        else:
            for i in range(1,len(node.keys)):
                if valueToInsert < node.keys[i]:
                    return self.insert(node.children[i], valueToInsert,searchDone)
        return True

    def split(self, node) :
        print("SPLIT")
        middle = len(node.keys)//2
        keyInParent = node.keys[middle]
        keysNewChildLeft = []
        keysNewChildRight = []
        node.keys.remove(keyInParent)
        
        #On parcours le noeud pour répartir les clefs entre deux fils
        for i in range(len(node.keys)) :
            if(i < middle):
                keysNewChildLeft.append(node.keys[i])
            else: 
                keysNewChildRight.append(node.keys[i])
        
        #On créer les deux fils
        newChildLeft = Node(keysNewChildLeft, [])
        newChildRight = Node(keysNewChildRight, [])
        
        #Pour chaque enfant du noeud en cours, on attribue ses anciens enfants sous les nouveaux enfants
        for i in range(len(node.children)) :
            if(i < middle) :
                node.children[i].parent = newChildLeft
                newChildLeft.children.append(node.children[i])
            else :
                node.children[i].parent = newChildRight
                newChildRight.children.append(node.children[i])
        #Si le noeud en cours est la racine, on créer une nouvelle racine
        if(node.parent is None):
            newRoot = Node([keyInParent], [newChildLeft, newChildRight])
            self.root = newRoot
        #Sinon on ajoute la clef du milieu au parent du noeud en cours, on l'enleve du noeud en cours
        else :
            indexToInsert = 0
            while indexToInsert < len(node.parent.keys) and node.parent.keys[indexToInsert] < keyInParent:
                indexToInsert = indexToInsert + 1
            node.parent.keys.insert(indexToInsert,keyInParent)
            #Si l'ajout de notre clef depasse le nombre de clef max, on split le parent
            if len(node.parent.keys) > self.nbKeysMax :
                self.split(node.parent)
            node.parent.children.insert(indexToInsert,newChildLeft)
            node.parent.children[indexToInsert + 1] = newChildRight

        
    def insertList(self, values) :
        for val in values :
            if(self.insert(self.root, val)) :
                print("Value ", val, " inserted.")
            else :
                print("Value ", val, " already in the tree.")

    #experimental
    def printArbre(self,node,depth):
        if node == self.root:
            print("\t",node.keys)
        for child in node.children:
            print('\t'* depth, child.keys, end ="\t")
        print()
        for child in node.children:
            self.printArbre(child,depth = depth + 1)

    def deleteKey(self,node,valueToDelete,searchDone):
        if node.isLeaf:
            node.key.remove(valueToDelete)
            return 
        if searchDone == False and search(self.root, valueToDelete):
            searchDone = True
            return False