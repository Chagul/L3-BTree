from Node import Node

class BTree:
    """
    Cette classe permet de modéliser les arbres-B.
    Elle comporte 3 attributs :
    root : la racine de l'arbre-B
    nbKeysMin : le nombre minimum de clefs contenus dans chaque noeud de l'arbre
    nbKeysMax : le nombre maximum de clefs contenus dans chaque noeud de l'arbre
    """
    
    def __init__(self, root, L, U):
        """
        Cette méthode est le constructeur de la classe. Il permet d'instancier un arbre-B.
        Elle demande 3 paramètres :
        root : le noeud racine pour l'arbre que l'on souhaite créer
        L : le nombre de fils minimum pour chaque noeud de l'arbre
        U : le nombre de fils maximum pour chaque noeud de l'arbre
        Une exception est levée si les valeurs de L et U sont incohérentes entre elles.
        """

        self.root = root
        minKey = L - 1 
        maxKey = U - 1
        if minKey <= 0 or maxKey <= 0 or maxKey < minKey :
            raise Exception("Invalid L or U value")
        self.nbKeysMin = minKey
        self.nbKeysMax = maxKey

    def isValid(self):
        """
        Cette méthode permet de vérifier si un arbre est valide en vérifiant 3 points :
        Est-il linéaire ?
        Est-il équilibré ?
        Le nombre de clés dans ses noeuds respecte-il bien les contraintes imposées lors de l'instanciation de l'arbre ?
        Elle renvoie True si toutes les conditions sont vérifiées et que l'arbre et valide et False si au moins l'une de ces trois conditions n'est pas respectée.
        """
        return self.isLinear() and self.isBalanced() and self.rightNumberOfKeys(self.root)

    def search(self, node, valueSearched):
        """
        Cette méthode permet de rechercher une valeur dans l'arbre en le parcourant récursivement.
        Elle renvoie True si la valeur est trouvée dans l'arbre et False sinon.
        Elle prend en paramètre le noeud à partir duquel la recherche dans l'arbre commence ainsi que la valeur à trouver.
        """
        
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
        """
        Cette méthode permet de vérifier que l'arbre est linéaire. 
        C'est à dire que lorsque l'on transforme l'arbre en une liste, cette dernière doit être triée par ordre croissant.
        """

        list = []
        self.linearize(self.root,list)
        for i in range(len(list) - 1):
            firstKey = list[i]
            secondKey = list[i+1]
            if secondKey < firstKey:
                return False
        return True

    def getHeight(self, node) :
        """
        Cette méthode calcule et renvoie la hauteur de l'arbre récursivement.
        Elle prend en paramètre un noeud à partir duquel elle calcule la hauteur de l'arbre.
        """

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
        """
        Cette méthode permet de vérifier que l'arbre-B est équilibré en le parcourant et en vérifiant que toutes les branches font la même hauteur.
        """

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
        """
        Cette méthode vérifie que les contraintes minimum et maximum du nombre de clés dans chaque noeud sont vérifiées en parcourant l'arbre récursivement.
        Elle prend en paramètre un noeud de départ pour la vérification.
        """

        bool = len(node.keys) <= self.nbKeysMax and len(node.keys) >= self.nbKeysMin
        if not bool :
            return False
        if node.isLeaf:
            return bool
        for i in range(len(node.keys) + 1):
             bool = bool and self.rightNumberOfKeys(node.children[i])
        return bool

    def linearize(self,node,list):
        """
        Cette méthode permet de linéariser l'arbre-B en le parcourant de gauche à droite depuis la racine.
        Elle prend en paramètre un noeud de départ dans l'arbre et une liste que la fonction met à jour avec les valeurs des clés de l'arbre. Cette dernière doit être préalablement vide.
        """

        #Si c'est une feuille, on rajoute toute les clefs
        if node.isLeaf:
            return list.extend(node.keys) 
        #Pour chaque enfant, on rappelle la fonction
        for i in range(len(node.children)):
            self.linearize(node.children[i],list)
            if i != len(node.keys):
                list.append(node.keys[i])

    def insert(self, node, valueToInsert):
        """
        Cette méthode permet d'insérer une valeur dans l'arbre tout en gardant une structure d'arbre valide.
        Elle réalise un parcours d'arbre récursif.
        Plusieurs cas d'exécutions existent pour l'insertion et des commentaires permet d'identifier ces diférents cas dans la fonction.
        Elle prend en paramètre un noeud à partir duquel parcourir l'arbre pour l'insertion ainsi que la valeur que l'on souhaite insérer.
        Renvoie True si la valeur a été correctement insérée dans l'arbre, False sinon.
        """

        #si la valeur est déjà dans l'arbre, ne pas insérer
        if self.search(self.root, valueToInsert) :
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
            return True
        #Si la valeur à inserer est inférieur à la clef la plus à gauche du noeud en cours
        elif valueToInsert < node.keys[0]:
            return self.insert(node.children[0], valueToInsert)
        #Si la valeur à inserer est inférieur à la clef la plus à droite du noeud en cours
        elif valueToInsert > node.keys[len(node.keys) -1 ]:
            return self.insert(node.children[len(node.children)- 1], valueToInsert)
        #Sinon on parcours les clefs pour trouver dans quel enfant aller par rapport aux clefs du noeud en cours
        else:
            for i in range(1,len(node.keys)):
                if valueToInsert < node.keys[i]:
                    return self.insert(node.children[i], valueToInsert)
        return True

    def split(self, node) :
        """
        Méthode auxiliaire permettant d'éclater des noeuds, utile pour l'insertion.
        Elle crée deux nouveaux noeuds dans le cas d'un éclatement, place correctement les clés déjà présentes
        dans l'arbre dans ces noeuds et met à jour les références vers ce's nouveaux fils.
        Des commentaires dans la fonction sont présents pour montrer les différentes étapes d'exécution.
        Elle prend en paramètre le noeud à éclater.
        """

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
        
        #On crée les deux fils
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
        """
        Méthode permettant d'insérer une liste de valeurs.
        Elle prend en paramètre une liste de valeurs à insérer.
        Elle réalise l'insertion en itérant sur cete liste et en appelant la fonction insert sur chacun de ses éléments.
        Elle renvoie True si toutes les valeurs ont été insérées, False si au moins une n'a pas été insérée.
        """

        areInserted = True
        for val in values :
            inserted = self.insert(self.root, val)
            if not inserted :
                areInserted = False
        return areInserted

    #experimental
    def printArbre(self,node,depth):
        if node == self.root:
            print("\t",node.keys)
        for child in node.children:
            print('\t'* depth, child.keys, end ="\t")
        print()
        for child in node.children:
            self.printArbre(child,depth = depth + 1)

    def deleteKey(self,node,valueToDelete):
        """
        Méthode permettant la suppression d'une valeur dans l'arbre.
        Des commentaires sont présents dans le code de la fonction pour identifier les différents cas d'exécutions possibles.
        Elle prend en paramètre le noeud à partir duquel parcourir l'arbre récursivement ainsi que la valeur à supprimer dans l'arbre.
        Elle renvoie True si la valeur a bien été supprimée de l'arbre, False sinon.
        WORK IN PROGRESS
        """

        #recherche la valeur dans l'arbre, rien a faire si elle n'est pas dedans
        if not self.search(self.root, valueToDelete):
            return False
        lenAfterRemoval = len(node.keys) - 1
        #Si c'est une feuille et qu'on peut supprimer sans passer en dessous du minimum, on a juste à supprimer, pas d'autre update necessaire
        if node.isLeaf:
            node.keys.remove(valueToDelete)
            if lenAfterRemoval >= self.nbKeysMin :
                return
            else:
                self.leafUpdate(node.parent, node)
                return
        
        if valueToDelete in node.keys:
            print("not in leaf")
            return
        #Si la valeur à supprimer est inférieure à la clef la plus à gauche du noeud en cours
        elif valueToDelete < node.keys[0]:
            return self.deleteKey(node.children[0], valueToDelete)
        #Si la valeur à inserer est inférieure à la clef la plus à droite du noeud en cours
        elif valueToDelete > node.keys[len(node.keys) -1 ]:
            return self.deleteKey(node.children[len(node.children)- 1], valueToDelete)
        #Sinon on parcourt les clefs pour trouver dans quel enfant aller par rapport aux clefs du noeud en cours
        else:
            for i in range(1,len(node.keys)):
                if valueToDelete < node.keys[i]:
                    return self.deleteKey(node.children[i], valueToDelete)

        #if lenAfterRemoval == 0:
        #    node.parent.children.remove(node)
        #else:
        #    None
        return True

    def leafUpdate(self, parent, leafUpdated):
        """
        Méthode auxiliaire permettant l'éclatement du noeud dans le cas de la suppression. L'arbre perdra alors un niveau de hauteur.
        Les différents cas possibles d'exécutions sont identifiés par des commentaires dans le code.
        Elle prend en paramètre le noeud père du noeud que l'on souhaite éclater ainsi que le noeud que l'on souhaite éclater.
        WORK IN PROGRESS
        """

        print("looking at ", parent.keys)
        indexNodeUpdatedInParent = 0
        while indexNodeUpdatedInParent < len(parent.children) and parent.children[indexNodeUpdatedInParent] != leafUpdated:
            indexNodeUpdatedInParent = indexNodeUpdatedInParent + 1
        
        leftNeighbour = parent.children[indexNodeUpdatedInParent - 1]
        rightNeigbour = parent.children[indexNodeUpdatedInParent + 1]
        print("index : ", indexNodeUpdatedInParent)
        ##Si on  peut prendre à gauche
        if indexNodeUpdatedInParent == 0:
            if len(rightNeigbour) > self.nbKeysMin:       
                tmpKeyFromParent = parent.keys[indexNodeUpdatedInParent]
                keyFromLeftNeighbour = takeLastKeyOfAndRemoveIt(leftNeighbour)
                parent.keys.insert(indexNodeUpdatedInParent, keyFromLeftNeighbour)
                leafUpdated.insert(tmpKeyFromParent)
                leafUpdated.keys.sort()
            else:
                tmpListOfKeys = leafUpdated.keys
                parent.children.pop(0)
                
        elif indexNodeUpdatedInParent == len(parent.keys):
            None

        # if indexNodeUpdatedInParent != 0 and len(leftNeighbour.keys) > self.nbKeysMin:
        #     tmpKeyFromParent = parent.keys[indexNodeUpdatedInParent - 1]
        #     keyFromLeftNeighbour = takeLastKeyOfAndRemoveIt(leftNeighbour)
        #     parent.keys.insert(indexNodeUpdatedInParent - 1, keyFromLeftNeighbour)
        #     leafUpdated.insert(tmpKeyFromParent)
        #     leafUpdated.keys.sort()
        
        # ##Si on peut prendre à droite
        # elif indexNodeUpdatedInParent != len(parent.keys) and len(rightNeigbour.keys) > self.nbKeysMin:
        #     tmpKeyFromParent = parent.keys[indexNodeUpdatedInParent + 1]
        #     keyFromRightNeigbour = self.takeFirstKeyOfAndRemoveIt(rightNeigbour)
        #     parent.keys.insert(indexNodeUpdatedInParent + 1, keyFromRightNeigbour)
        #     leafUpdated.keys.append(tmpKeyFromParent)
        #     leafUpdated.keys.sort()
        #     print(leafUpdated.keys)
        #     ##Sinon
        # else:
        #     if indexNodeUpdatedInParent != 0:
        #         child = parent.children[indexNodeUpdatedInParent - 1]
        #         child.keys.append(parent.keys[indexNodeUpdatedInParent - 1])
        #         parent.keys.pop(indexNodeUpdatedInParent - 1)
        #     else:
        #         child = parent.children[indexNodeUpdatedInParent + 1]
        #         child.keys.append(parent.keys[indexNodeUpdatedInParent])
        #         parent.keys.pop(indexNodeUpdatedInParent)
        #     print(child.keys)
        #     child.keys.extend(leafUpdated.keys)
        #     child.keys.sort()
        #     print(child.keys)

        #     parent.children.remove(leafUpdated)


    def takeLastKeyOfAndRemoveIt(self, node):
        """
        Méthode auxiliaire à la méthode d'éclatement de noeud pour la suppression.
        Permet d'obtenir la plus grande clé présente dans un noeud tout en la retirant de la liste des clés du noeud.
        Elle prend en paramètre le noeud duquel on souhaite extraire la plus grande valeur.
        Retourne la dernière clé contenue dans le noeud passé en paramère.
        """

        tmpKey = node.keys[len(node.keys) - 1]
        node.keys.pop(len(node.keys) - 1) 
        return tmpKey

    def takeFirstKeyOfAndRemoveIt(self, node):
        """
        Méthode auxiliaire à la méthode d'éclatement de noeud pour la suppression.
        Permet d'obtenir la plus petite clé présente dans un noeud tout en la retirant de la liste des clés du noeud.
        Elle prend en paramètre le noeud duquel on souhaite extraire la plus petite valeur.
        Retourne la première clé contenue dans le noeud passé en paramère.
        """

        tmpKey = node.keys[0]
        node.keys.remove(tmpKey)
        return tmpKey