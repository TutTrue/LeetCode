# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = 0
        def dfs(root, path=0):
            nonlocal s
            if not root:
                return 0
            if not root.left and not root.right:
                s += path * 10 + root.val
                return s
            dfs(root.left, (path * 10) + root.val)
            dfs(root.right, (path * 10) + root.val)
            return s
        return dfs(root)