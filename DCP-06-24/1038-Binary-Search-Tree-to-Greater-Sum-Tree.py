# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s=0
        def dfs(root=root):
            nonlocal s
            if not root:
                return 
            dfs(root.right)
            s+=root.val
            root.val = s
            dfs(root.left)

        dfs()
        return root