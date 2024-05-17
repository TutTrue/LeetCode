# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node=root, path=0):
            if not node:
                return False
            path+=node.val
            if not node.left and not node.right:
                return targetSum == path
            return dfs(node.left, path) or dfs(node.right, path)
        return dfs()