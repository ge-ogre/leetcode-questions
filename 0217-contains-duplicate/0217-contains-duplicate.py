class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for i in nums:
            if i in store:
                return True
            else:
                store[i] = 1
        return False