class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        anchor = 0
        for explorer in range(len(nums)):
            if nums[anchor] != nums[explorer]:
                anchor += 1
                nums[anchor] = nums[explorer]

        return anchor+1