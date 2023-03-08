class Solution(object):
    def twoSum(self, A, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, 1
        while l<r:
            if A[r] == target - A[l]:
                return [l,r]
            if r == len(A)-1:
                l+=1
                r = l+1
            else:
                r+=1