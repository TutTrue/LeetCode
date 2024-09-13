# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        q = [root1, root2]
        res = []
        while q:
            cur = q.pop()
            if not cur:
                continue
            res.append(cur.val)
            q.append(cur.left)
            q.append(cur.right)

        res.sort()
        return res
