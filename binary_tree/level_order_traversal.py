import collections
import queue


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


# def levelOrderTraversal(rootNode: binaryTree):
#     if not rootNode:
#         return

#     res = []
#     queue = collections.deque()
#     queue.append(rootNode)

#     while queue:

#         queue_length = len(queue)
#         level = []
#         for i in range(queue_length):
#             root = queue.popleft()
#             level.append(root.value)

#             if root.leftChild is not None:
#                 queue.append(root.leftChild)

#             if root.rightChild is not None:
#                 queue.append(root.rightChild)

#         res.append(level)

#     print(res)


def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    res = []
    queue = collections.deque()
    queue.append(rootNode)
    while queue:
        level = []
        for _ in range(len(queue)):
            curr = queue.popleft()
            level.append(curr.value)
            if curr.leftChild is not None:
                queue.append(curr.leftChild)
            if curr.rightChild is not None:
                queue.append(curr.rightChild)
        res.append(level)
    print(res)


levelOrderTraversal(bt)
