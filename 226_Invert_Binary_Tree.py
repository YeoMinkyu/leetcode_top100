# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        current_node = [root]

        while current_node:
            next_node = []
            while current_node:
                node = current_node.pop(0)

                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)

                temp_node = node.left
                node.left = node.right
                node.right = temp_node

            current_node = next_node

        return root