# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    pre_val = None

    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        self.convertBST(root.right)
        self.visit_val(root)
        self.convertBST(root.left)

        return root

    def visit_val(self, node):
        if self.pre_val is None:
            self.pre_val = node.val
        else:
            node.val += self.pre_val
            self.pre_val = node.val