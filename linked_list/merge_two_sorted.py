from pickle import NONE


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = ListNode(val=value)
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
            res += str(temp.val)
            if temp.next is not None:
                res += " -> "
            temp = temp.next
        return res


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = dummy = ListNode()

        while list1 and list2:
            print('temp-->')
            Solution.print(temp)
            print('dummy-->')
            Solution.print(dummy)
            if list1.val > list2.val:
                temp.next = list2
                list2 = list2.next
            else:
                temp.next = list1
                list1 = list1.next

            temp = temp.next

        if list1:
            temp.next = list1
        if list2:
            temp.next = list2

        return dummy.next

    @staticmethod
    def print(res):
        temp = res
        res = ""
        while temp is not None:
            res += str(temp.val)
            if temp.next is not None:
                res += " -> "
            temp = temp.next
        print(res)


list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(4)
# print(list1)


list2 = LinkedList()
list2.append(1)
list2.append(3)
list2.append(4)
# print(list2)


s = Solution()
res = s.mergeTwoLists(list1.head, list2.head)
s.print(res)
