# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        bfs = deque([root])
        res = [root.val]
        while bfs:
            tmp = bfs.popleft()
            if tmp.left:
                bfs.append(tmp.left)
            if tmp.right:
                bfs.append(tmp.right)
            res.append(tmp.left.val if tmp.left else None)
            res.append(tmp.right.val if tmp.right else None)
        j = len(res) - 1
        while not res[j]:
            j-=1
        for i in range(j):
            if not res[i]:
                return False
        print(res)
        return True
        