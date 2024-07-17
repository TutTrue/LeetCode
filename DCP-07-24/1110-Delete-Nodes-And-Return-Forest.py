# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        s = set(to_delete)

        def dfs(root, is_root):
            if not root:
                return None
            in_deleted = root.val in s
            if is_root and not in_deleted:
                res.append(root)
            root.left = dfs(root.left, in_deleted)
            root.right = dfs(root.right, in_deleted)
            return None if in_deleted else root
        dfs(root, True)
        return res