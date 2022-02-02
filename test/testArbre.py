import unittest
import sys
sys.path.append("../src")
from BTree import BTree
from Node import Node

class Test(unittest.TestCase):

    def setUp(self):
        self.arrayValues = [2, 4, 5, 7, 8, 9, 11, 12, 13, 22, 26, 28, 30, 32, 34, 36]
        self.btreeValid = BTree(
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

    def test010_isLinearReturnTrue(self):
        self.assertTrue(self.btreeValid.isLinear())

    def test011_isNotLinearReturnFalse(self):
        bTreeNotLinear = BTree(Node(keys=[7,22],
                                        children=[
                                                Node(keys=[4],children=[]),
                                                Node(keys=[25],children=[]),
                                                Node(keys=[11],children=[]),
                                                ]

            ),2,3)
        self.assertFalse(bTreeNotLinear.isLinear())

    def test020_isBalancedReturnTrue(self):
        self.assertTrue(self.btreeValid.isBalanced())

    def test021_isNotBalancedReturnFalse(self):
        bTreeNotBalanced = BTree(Node(keys=[7,22],
                                        children=[
                Node(
                    keys=[4],
                    children=[]
            )]),2,3)
        self.assertFalse(bTreeNotBalanced.isBalanced())
        bTreeNotBalanced = BTree(
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
                            keys=[12,16],
                            children=[
                                Node(keys=[14],
                                    children=[]
                                )
                            ]
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
        self.assertFalse(bTreeNotBalanced.isBalanced())

    def test030_rightNumberOfKeysReturnTrue(self):
        self.assertTrue(self.btreeValid.rightNumberOfKeys(self.btreeValid.root))

    def test_031_wrongNumberOfKeysReturnFalse(self):
        None

    def test_040_isValidReturnTrue(self):
        None 

    def test50_applatiFunctionReturnTheSameList(self):
        list = []
        self.btreeValid.linearize(self.btreeValid.root, list)
        self.assertEqual(list, self.arrayValues)

if __name__ == "__main__":
    unittest.main()