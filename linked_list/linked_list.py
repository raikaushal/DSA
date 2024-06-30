class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def __str__(self):
        temp = self.head
        res = ""
        while temp is not None:
            res += str(temp.value)
            if temp.next is not None:
                res += " -> "
            temp = temp.next
        return res


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print(llist)
