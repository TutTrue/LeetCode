# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        def dfs(root=root, index=(0, 0)):
            if not root:
                return 
            dic[index[1]].append((index[0], root.val))
            dfs(root.left, (index[0] + 1, index[1] - 1))
            dfs(root.right, (index[0] + 1, index[1] + 1))
        dfs()
        res=[]
        for k, v in sorted(dic.items()):
            v.sort()
            res.append([x[1] for x in v])

        return res
