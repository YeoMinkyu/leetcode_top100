# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        depth = 0
        current_level = [root]

        while current_level:
            next_level = []
            while current_level:
                node = current_level.pop()
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            depth += 1
            current_level = next_level

        return depth