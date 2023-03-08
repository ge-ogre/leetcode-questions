class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        store={}
        for i in nums:
            if i not in store:
                store[i]=1
            else:
                return True
        return False