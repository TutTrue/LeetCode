# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return
        if depth == 1:
            tmp = TreeNode(val)
            tmp.left = root
            root = tmp

        def dfs(root=root, d=1):
            if not root:
                return
            if d == depth - 1:
                ltmp = TreeNode(val)
                rtmp = TreeNode(val)

                ltmp.left = root.left
                root.left = ltmp
                
                rtmp.right = root.right
                root.right = rtmp

                return
            dfs(root.left, d+1)
            dfs(root.right, d+1)
        dfs()
        return root    