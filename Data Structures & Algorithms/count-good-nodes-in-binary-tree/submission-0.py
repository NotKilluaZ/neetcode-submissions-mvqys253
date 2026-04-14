# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def dfs(node, largest):
            if not node:
                return 0
            
            if node.val >= largest:
                res = 1
            else:
                res = 0

            largest = max(largest, node.val)

            return res + dfs(node.left, largest) + dfs(node.right, largest)

        return dfs(root, root.val)
