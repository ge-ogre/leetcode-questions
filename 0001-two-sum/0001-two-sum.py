class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, n in enumerate(nums):
            store[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in store and store[diff] != i:
                return [i, store[diff]]