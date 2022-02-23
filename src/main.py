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
    # btree.linearize(btree.root, list)
    # print(list)
    btree.insert(btree.root,10)
    print(btree.search(btree.root,10))
    btree.linearize(btree.root, list)
    print(list)
    #print("Balanced ", btree.isBalanced())
    #print("RightNumberOfKeys", btree.rightNumberOfKeys(btree.root))
    #print("Linear ", btree.isLinear())


if __name__ == "__main__":
    main()