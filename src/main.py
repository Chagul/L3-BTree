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
    ),3,2)
    list = []
    btree.linearize(btree.root, list)
    print(list)
if __name__ == "__main__":
    main()