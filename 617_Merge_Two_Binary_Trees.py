import queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        t1_q = queue.Queue()
        t2_q = queue.Queue()
        t1_q.put(t1)
        t2_q.put(t2)

        if t1 == None:
            return t2

        while not (t1_q.empty() and t2_q.empty()):
            t1_node = t1_q.get()
            t2_node = t2_q.get()

            if t1_node == None or t2_node == None:
                continue

            t1_node.val = t1_node.val + t2_node.val

            if t1_node.left is None:
                t1_node.left = t2_node.left
            else:
                t1_q.put(t1_node.left)
                t2_q.put(t2_node.left)

            if t1_node.right is None:
                t1_node.right = t2_node.right
            else:
                t1_q.put(t1_node.right)
                t2_q.put(t2_node.right)

        return t1