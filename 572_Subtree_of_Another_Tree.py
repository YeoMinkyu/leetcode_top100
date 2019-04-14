# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        self.result = 0
        if not s and not t:
            return True
        elif not s or not t:
            return False

        if self.check_node(s, t):
            return True
        else:
            if self.isSubtree(s.left, t):
                return True
            else:
                if self.isSubtree(s.right, t):
                    return True
                else:
                    return False
        return False

    def check_node(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False

        if s.val == t.val:
            if self.check_node(s.left, t.left):
                if self.check_node(s.right, t.right):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
