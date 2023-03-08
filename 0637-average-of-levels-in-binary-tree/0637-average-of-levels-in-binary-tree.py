# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q, info = [root], []
        while len(q):
            qlen, row = len(q), 0
            for i in range(qlen):
                cur = q.pop(0)
                row += cur.val
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            info.append(row/qlen)
        return info