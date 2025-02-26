class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = {}
        for i in s:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1

        for i in t:
            if i in store:
                store[i] -= 1
            else:
                return False
        
        for k in store:
            if store[k] != 0:
                return False

        return True