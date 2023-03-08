# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root, root2):
            if root == None:
                if root2 == None: return True
                else: return False
            if root2 == None:
                if root == None: return True
                else: return False
            
            return (root.val == root2.val) and (dfs(root.left, root2.left)) and (dfs(root.right, root2.right))
        
        return dfs(p, q)