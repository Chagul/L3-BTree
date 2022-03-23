import sys
sys.path.append("../src")
from BTree import BTree
from Node import Node

def batterie1() :
    btree = BTree(Node([], []), 2, 3)
    valuesToInsert = [2, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 7, 9, 11, 13]
    valuesToDelete = [14, 10, 20, 18, 16, 24, 6]
    print("Valeurs à insérer :", valuesToInsert)
    print("Insertion des valeurs :", btree.insertList(valuesToInsert), "\n")
    print("Vérification de l'insertion : ")
    print("Recherche de la valeur 42 :", btree.search(btree.root, 42))
    print("L'arbre est-il un arbre-B ? :", btree.isValid())
    print("Insertion de la valeur 42 :", btree.insert(btree.root, 42))
    print("Recherche de la valeur 42 :", btree.search(btree.root, 42))
    print("L'arbre est-il toujours un arbre-B ? :", btree.isValid(), "\n")
    print("Suppression des valeus : Algorithme de suppression non terminé.")
    list = []
    btree.linearize(btree.root, list)
    print(list)

def batterie2() :
    values = [2,10,100,1000,5000,10000]
    btree = BTree(Node([], []), 6, 11)
    valuesToInsert = []
    for value in values:
        print("=========\nTest avec ", value, "\n")
        for i in range(10, value+1, 10) :
            valuesToInsert.append(i)
        for i in range(5, value, 10) :
            valuesToInsert.append(i)
        valuesToDelete = valuesToInsert.copy()
        print("Insertion des valeurs :", btree.insertList(valuesToInsert))
        print("Recherche de la valeur 4995 :", btree.search(btree.root, 4995))
        print("L'arbre est-il un arbre-B ? :", btree.isValid())
        print("L'arbre est-il un lineaire ? :", btree.isLinear())
        print("L'arbre a t'il un bon nombre de clefs ? :", btree.rightNumberOfKeys(btree.root))
        print("L'arbre est-il équilibré ? :", btree.isBalanced())
        print("L'arbre à une hauteur de  :", btree.getHeight(btree.root))
        print("Suppression des valeus : Algorithme de suppression non terminé.")        
        print()



if __name__ == "__main__":
    if(sys.argv[1] == "1") :
        batterie1()

    elif(sys.argv[1] == "2") :
        batterie2()