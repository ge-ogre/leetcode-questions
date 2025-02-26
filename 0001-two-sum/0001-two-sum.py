class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in store:
                return [i, store[diff]]
            store[n] = i