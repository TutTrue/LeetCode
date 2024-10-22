# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        sums = []
        q = deque([(root, 0)])
        while q:
            node, level = q.pop()
            if level == len(sums):
                sums.append(-node.val)
            else:
                sums[level] -= node.val
            
            if node.left:
                q.append((node.left, level+1))
            
            if node.right:
                q.append((node.right, level+1))
        if k > len(sums):
            return -1
        heapify(sums)
        for _ in range(k-1):
            heappop(sums)
        return -sums[0]
            