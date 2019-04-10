# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        elif root.left == None and root.right == None:
            return True

        result = True

        current_node = [root]

        while current_node:
            next_node = []
            print(current_node)
            while current_node:
                node = current_node.pop(0)

                if node:
                    next_node.append(node.left)
                    next_node.append(node.right)

            current_node = next_node

            if not self._is_symmetric(next_node, result):
                return False

        return result

    def _is_symmetric(self, nodes, result):
        length = len(nodes)
        for i in range(0, int(length * 0.5)):
            if nodes[i] is None:
                if nodes[length - i - 1]:
                    result = False
            elif nodes[length - i - 1] is None:
                if nodes[i]:
                    result = False
            elif nodes[i].val != nodes[length - i - 1].val:
                result = False

        return result