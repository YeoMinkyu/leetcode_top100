# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list = None

        if not l1 and not l2:
            return new_list
        elif not l2:
            return l1
        elif not l1:
            return l2

        while l1 and l2:
            if l1.val <= l2.val:
                if new_list is None:
                    new_list = l1
                    l1 = l1.next
                    current_node = new_list
                else:
                    current_node.next = l1
                    l1 = l1.next
                    current_node = current_node.next
            else:
                if new_list is None:
                    new_list = l2
                    l2 = l2.next
                    current_node = new_list
                else:
                    current_node.next = l2
                    l2 = l2.next
                    current_node = current_node.next

        if l1 is None:
            current_node.next = l2
        elif l2 is None:
            current_node.next = l1

        return new_list
