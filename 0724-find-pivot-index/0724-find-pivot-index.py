class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in nums:
            total += i
        leftsum = 0
        for i in range(len(nums)):
            rightsum = total - (nums[i] + leftsum)
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        
        return -1
            