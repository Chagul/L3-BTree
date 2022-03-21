class Node:
    """
    Cette classe permet de modéliser les noeuds dans les arbres-B.
    Elle comporte 5 attributs :
    nbKeys : le nombre de clés présentes dans ce noeud.
    keys : la liste des clés du noeud.
    children : la liste des noeuds enfants du noeud courant.
    parent : une référence vers le noeud père du noeud courant
    isLeaf : booléen déterminant si le noeud est une feuille ou non.
    """

    def __init__(self, keys, children):
        """
        Cette méthode est le constructeur de la classe. Il permet d'instancier un noeud pour un arbre-B.
        Elle prend en paramètre la liste des clés que le noeud crée va comporter ainsi que la liste des noeuds fils de ce nouveau noeud.
        """

        self.nbKeys = len(keys)
        self.keys = keys
        self.children = children
        self.parent = None
        self.isLeaf = len(self.children) == 0
        for child in children :
            child.setParent(self)

    def setIsLeaf(self, isLeaf):
        """
        Setter permettant de modifier la valeur de l'attribut isLeaf.
        Cette méthode prend en paramètre un argument, un booléen déterminant si le noeud est maintenant une feuille ou non.
        """

        self.isLeaf = isLeaf
    
    def getChildrens(self):
        """
        Getter permettant d'obtenir la liste des noeuds fils du noeud courant.
        Ne prend pas de paramètre et retourne l'attribut children, une liste comportant les noeuds fils du noeud courant.
        """

        return self.children

    def setKey(self,key):
        """
        Setter permettant de modifier la valeur l'attribut keys.
        Cette méthode prend en paramètre une liste de clés.
        Elle ajoute en fin de la liste de clé du noeud courant les nouvelles clés passées en paramètres. Elle trie ensuite la liste complète pour que les clés
        soient triées de la plus petite à la plus grande.
        """

        self.keys.extend(key)
        self.keys.sort()

    def setChildren(self, newChildrens):
        """
        Setter permettant de modifier la valeur de l'attribut children.
        Cette méthode prend en paramètre une liste de noeuds enfants.
        Elle remplace l'attribut children du noeud courant par la liste d'enfants passée en paramètre.
        """

        self.children = newChildrens

    def setParent(self, parent) :
        """
        Setter permettant de modifier la valeur de l'attribut parent.
        Cette méthode prend en paramètre un noeud.
        Elle remplace l'attribut parent du noeud courant par le noeud père passé en paramètre.
        """

        self.parent = parent