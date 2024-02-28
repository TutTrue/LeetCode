# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        left_most = None
        q = deque([root])
        while q:
            left_most = q.popleft()
            if left_most.right:
                q.append(left_most.right)
            if left_most.left:
                q.append(left_most.left)
        return left_most.val
            