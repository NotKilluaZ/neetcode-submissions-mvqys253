# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            q_len = len(q)
            r = None
            for x in range(q_len):
                node = q.popleft()
                if node:
                    r = node
                    q.append(node.left)
                    q.append(node.right)
            if r:
                res.append(r.val)

        return res