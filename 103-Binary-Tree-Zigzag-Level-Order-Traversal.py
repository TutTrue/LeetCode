# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        def dfs(node=root, level=0):
            if not node:
                return
            if len(res) <= level:
                res.append([node.val])
            else:
                res[level].insert(0, node.val)

            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs()
        for i in range(0, len(res), 2):
            res[i].reverse()
        return res