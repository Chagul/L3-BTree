from BTree import BTree
from Node import Node

def main():
    btree = BTree(
    Node(
        keys=[7,22],
        children=[
            Node(
                keys=[4],
                children=[
                    Node(
                        keys=[2],
                        children=[]
                    ),
                    Node(
                        keys=[5],
                        children=[]
                    )
                ]
            ),
            Node(
                keys=[11],
                children=[
                    Node(
                        keys=[8,9],
                        children=[]
                    ),
                    Node(
                        keys=[12,13],
                        children=[]
                    )
                ]
            ),
            Node(
                keys=[30,34],
                children=[
                    Node(
                        keys=[26,28],
                        children=[]
                    ),
                    Node(
                        keys=[32],
                        children=[]
                    ),
                    Node(
                        keys=[36],
                        children=[]
                    )
                ]
            )
        ]
    ),2,3)
    # btree.linearize(btree.root, list)
    # print(list)
    # print("Valid  ", btree.isValid())
    #for i in range(51) :
    #    print(i, ", ", btree.search(btree.root, i))
    list = []
    btree.linearize(btree.root, list)
    print("search avant insert:",btree.search(btree.root,14))
    print(list)
    btree.insert(btree.root,14)
    print("search apres insert:" ,btree.search(btree.root,14))

    print("------")
    btree.insert(btree.root,1)
    print("------")
    # print("------")
    # btree.printArbre(btree.root,0)
    # btree.deleteKey(btree.root, 26)
    list = []
    btree.linearize(btree.root, list)
    btree.insert(btree.root,14)
    print(list)
    print("------")
    list = []
    btree.linearize(btree.root, list)



    # for i in range(50):
        # print(i , " " , btree.search(btree.root,i))
    # btree.insert(btree.root,22)
    # btree.linearize(btree.root, list)
    # print(list)
    #print("Balanced ", btree.isBalanced())
    #print("RightNumberOfKeys", btree.rightNumberOfKeys(btree.root))
    #print("Linear ", btree.isLinear())


if __name__ == "__main__":
    main()