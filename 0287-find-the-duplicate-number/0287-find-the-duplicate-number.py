class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        store = {}
        for i in nums:
            if i not in store:
                store[i]=1
            else:
                return i