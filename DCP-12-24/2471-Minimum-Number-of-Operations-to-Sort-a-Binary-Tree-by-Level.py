# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([(root, 0)])
        arr = []
        while q:
            node, level = q.pop()
            if len(arr) == level:
                arr.append([node.val])
            else:
                arr[level].append(node.val)
            if node.right:
                q.append((node.right, level+1))
            if node.left:
                q.append((node.left, level+1))

        for a in arr:
            sorted_lvl = sorted(a)
            ops = 0
            
            index_map = {v: i for i, v in enumerate(sorted_lvl)}
            visited = [False] * len(a)
            
            for i in range(len(a)):
                if visited[i] or a[i] == sorted_lvl[i]:
                    continue
                cycle_size = 0
                x = i
                while not visited[x]:
                    visited[x] = True
                    x = index_map[a[x]]
                    cycle_size += 1
                if cycle_size > 0:
                    ops += (cycle_size - 1)
            
            res += ops
        return res