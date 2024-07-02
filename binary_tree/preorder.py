
class binaryTree:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


bt = binaryTree(1)

bt_left = binaryTree(2)
bt_left.leftChild = binaryTree(3)
bt_left.rightChild = binaryTree(4)

bt_right = binaryTree(5)
bt_right.leftChild = binaryTree(6)
bt_right.rightChild = binaryTree(7)

bt.leftChild = bt_left
bt.rightChild = bt_right


def preOrderTraversal(rootNode):
    if not rootNode:
        return

    print(rootNode.value)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return

    inOrderTraversal(rootNode.leftChild)
    print(rootNode.value)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return

    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.value)


postOrderTraversal(bt)
