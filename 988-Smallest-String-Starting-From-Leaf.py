# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = []
        m = None
        def dfs(root=root, s=''):
            nonlocal m
            if not root:
                return
            if not root.left and not root.right:
                st = s+chr(root.val + 97)
                if not m:
                    m = st[::-1]
                else:
                    m = min(m, st[::-1])
                return
            dfs(root.left, s+chr(root.val + 97))
            dfs(root.right, s+chr(root.val + 97))
        dfs()
        return m