# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node_stack = []
        node = head
        while node:
            node_stack.append(node.val)
            node = node.next

        node = head

        while node_stack:
            val = node_stack.pop()
            node.val = val
            node = node.next

        return head