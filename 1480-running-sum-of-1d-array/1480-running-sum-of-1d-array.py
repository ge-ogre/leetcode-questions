class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        otpt = [None] * len(nums)
        acc = 0
        for i in range(len(nums)):
            otpt[i] = nums[i] + acc
            acc += nums[i]
            
        return otpt