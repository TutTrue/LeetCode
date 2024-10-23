# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sums = defaultdict(int)
        siblings = {}
        def dfs_getsum(node=root, level=0):
            if not node:
                return
            sums[level] += node.val
            if node.left:
                siblings[node.left] = node.right.val if node.right else 0
            if node.right:
                siblings[node.right] = node.left.val if node.left else 0
            dfs_getsum(node.right, level+1)
            dfs_getsum(node.left, level+1)
        def dfs_modifytree(node=root, level=0):
            if not node:
                return
            node.val = sums[level] - node.val - siblings.get(node, 0)
            dfs_modifytree(node.left, level+1)
            dfs_modifytree(node.right, level+1)
            
        dfs_getsum()
        dfs_modifytree()
        
        return root