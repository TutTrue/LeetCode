# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s = 0
        def traverse(root):
            nonlocal s
            if not root:
                return 0
            s += root.left.val if root.left and not root.left.left and not root.left.right else 0
            traverse(root.right)
            traverse(root.left)
            return s
        return traverse(root)
        