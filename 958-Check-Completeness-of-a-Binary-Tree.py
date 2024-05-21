# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        bfs = deque([root])
        while bfs[0]:
            tmp = bfs.popleft()
            bfs.append(tmp.left)
            bfs.append(tmp.right)
        while bfs and not bfs[0]:
            bfs.popleft()
        return not bfs # return True if len(bfs) == 0 else False