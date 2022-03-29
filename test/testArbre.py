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

    def test_010_isLinearReturnTrue(self):
        self.assertTrue(self.btreeValid.isLinear())

    def test_011_isNotLinearReturnFalse(self):
        bTreeNotLinear = BTree(Node(keys=[7,22],
                                        children=[
                                                Node(keys=[4],children=[]),
                                                Node(keys=[25],children=[]),
                                                Node(keys=[11],children=[]),
                                                ]

            ),2,3)
        self.assertFalse(bTreeNotLinear.isLinear())

    def test_020_isBalancedReturnTrue(self):
        self.assertTrue(self.btreeValid.isBalanced())

    #       7,22
    #      /
    #     4
    #
    #            |7,                 22|
    #          /       |               \  
    #        |4|     |11|            |30,  34| 
    #       /  \      /  \           /   |   \
    #      |2| |5| |8,9|  |12,16||26,28||32|  |36|
    #                    /  
    #                  14
    def test_021_isNotBalancedReturnFalse(self):
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

    def test_030_rightNumberOfKeysReturnTrue(self):
        self.assertTrue(self.btreeValid.rightNumberOfKeys(self.btreeValid.root))

    def test_031_wrongNumberOfKeysRaiseException(self):
        #If L value is too small
        self.assertRaises(Exception,BTree,Node(keys=[1,2], children=[]),0,2)
        #If L value is inferior in comparaison of U value 
        self.assertRaises(Exception,BTree,Node(keys=[1,2], children=[]),3,2)
        #If U value is too small
        self.assertRaises(Exception,BTree,Node(keys=[1,2], children=[]),1,2)
    
    def test_040_getHeightJustRoot(self):
        btreeRoot = BTree(Node(keys=[1],children=[]),2,3)
        self.assertEqual(0,btreeRoot.getHeight(btreeRoot.root))
    
    def test_041_getHeight(self):
        self.assertEqual(2,self.btreeValid.getHeight(self.btreeValid.root))

    def test_050_isValidReturnTrue(self):
        self.assertTrue(self.btreeValid.isValid())

    def test_60_applatiFunctionReturnTheSameList(self):
        list = []
        self.btreeValid.linearize(self.btreeValid.root, list)
        self.assertEqual(list, self.arrayValues)

    def test_070_searchReturnTrue(self):
        self.assertTrue(self.btreeValid.search(self.btreeValid.root,4))
        self.assertTrue(self.btreeValid.search(self.btreeValid.root,7))
        self.assertTrue(self.btreeValid.search(self.btreeValid.root,12))
        self.assertTrue(self.btreeValid.search(self.btreeValid.root,30))
        self.assertTrue(self.btreeValid.search(self.btreeValid.root,36))

    def test_071_searchReturnFalseWhenTheValueIsNotInTheTree(self):
        self.assertFalse(self.btreeValid.search(self.btreeValid.root, -1))
        self.assertFalse(self.btreeValid.search(self.btreeValid.root, 40))

    def test_080_insertionWithoutSplitIsCorrect(self):
        listBefore = []
        valueToInsert = 3
        self.btreeValid.linearize(self.btreeValid.root, listBefore)
        listBefore.append(valueToInsert)
        listBefore.sort()
        self.assertTrue(self.btreeValid.insert(self.btreeValid.root, valueToInsert))
        listAfter = []
        self.btreeValid.linearize(self.btreeValid.root, listAfter)
        self.assertEqual(listBefore, listAfter )
        self.assertTrue(self.btreeValid.isValid())
    
    def test_0810_insertValueAlreadyInTreeReturnFalse(self):
        valueToInsert = 2
        self.assertFalse(self.btreeValid.insert(self.btreeValid.root, valueToInsert))

    def test_0811_insertValueAlreadyInTreeDoesntAppendToList(self):
        valueToInsert = 2
        self.btreeValid.insert(self.btreeValid.root, valueToInsert)
        listAfterInsertion = []
        self.btreeValid.linearize(self.btreeValid.root, listAfterInsertion)
        cptValueToInsert = 0
        for value in listAfterInsertion:
            if value == valueToInsert:
                cptValueToInsert = cptValueToInsert + 1
        self.assertEqual(1,cptValueToInsert)
        
    def test_0812_insertValueAlreadyInTreeDoesntChangeTree(self):
        listAfterInsertion = []
        valueToInsert = 2
        self.btreeValid.insert(self.btreeValid.root, valueToInsert)
        self.btreeValid.linearize(self.btreeValid.root, listAfterInsertion)
        self.assertTrue(self.btreeValid.isValid())
    
    def test_0820_insertListOfValuesThatAreNotInTheTree(self):
        listOfValuesToInsert = [1,3,6,14]
        listBeforeInsertion = []
        self.btreeValid.linearize(self.btreeValid.root, listBeforeInsertion)
        listBeforeInsertion.extend(listOfValuesToInsert)
        listBeforeInsertion.sort()
        listAfterInsertion = []
        self.btreeValid.insertList(listOfValuesToInsert)
        self.btreeValid.linearize(self.btreeValid.root, listAfterInsertion)
        self.assertEqual(listBeforeInsertion, listAfterInsertion)

    def test_0821_insertListOfValuesThatAreNotInTheTreeReturnTrue(self):
        listOfValuesToInsert = [1,3,6,14]
        listBeforeInsertion = []
        self.btreeValid.linearize(self.btreeValid.root, listBeforeInsertion)
        listBeforeInsertion.extend(listOfValuesToInsert)
        listBeforeInsertion.sort()
        self.assertTrue(self.btreeValid.insertList(listOfValuesToInsert))

    def test_0822_insertListOfValueContainingValuesThatAreAlreadyInTreeRetunFalseButStillInsertValue(self):
        valueAlreadyInTree =  4
        listOfValuesToInsert = [1,3,valueAlreadyInTree,14]
        listBeforeInsertion = []
        self.btreeValid.linearize(self.btreeValid.root, listBeforeInsertion)
        listBeforeInsertion.extend(listOfValuesToInsert)
        listBeforeInsertion.sort()
        listBeforeInsertion.remove(valueAlreadyInTree)
        listAfterInsertion = []
        self.assertFalse(self.btreeValid.insertList(listOfValuesToInsert))
        self.btreeValid.linearize(self.btreeValid.root,listAfterInsertion)
        self.assertEqual(listBeforeInsertion,listAfterInsertion)

    def test_0823_insertListOfValuesThatAreAllAlreadyInTreeReturnFalseAndDoesntChangeTheTree(self):
        listOfValuesToInsert = [2,4,7,22]
        listBeforeInsertion = []
        self.btreeValid.linearize(self.btreeValid.root, listBeforeInsertion)
        listAfterInsertion = []
        self.assertFalse(self.btreeValid.insertList(listOfValuesToInsert))
        self.btreeValid.linearize(self.btreeValid.root,listAfterInsertion)
        self.assertEqual(listBeforeInsertion,listAfterInsertion)



        


if __name__ == "__main__":
    unittest.main()