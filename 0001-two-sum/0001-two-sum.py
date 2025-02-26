class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            else:
                if right >= len(nums) - 1:
                    left += 1
                    right = left + 1
                else:
                    right += 1