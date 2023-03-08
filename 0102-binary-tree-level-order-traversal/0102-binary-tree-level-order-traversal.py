# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q, ans = [root], []
        while len(q):
            qlen, curlvl = len(q), []
            for i in range(qlen):
                cur = q.pop(0)
                curlvl.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            ans.append(curlvl)
        return ans