# TODO : 속도 개선 및 한번에 못 푼 문제라 복습 필요!


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.result = 0

        if not root:
            return self.result

        self.pre_travel(root, target)

        return self.result

    def pre_travel(self, node, target):
        if not node:
            return

        self.visit(node, target)
        self.pre_travel(node.left, target)
        self.pre_travel(node.right, target)

    def visit(self, node, target):
        if not node:
            return

        if node.val == target:
            self.result += 1

        self.visit(node.left, target - node.val)
        self.visit(node.right, target - node.val)

