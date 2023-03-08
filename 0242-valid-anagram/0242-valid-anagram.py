class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        store={}
        for i in s:
            if i not in store:
                store[i]=1
            else:
                store[i]+=1
        
        for i in t:
            if i not in store:
                return False
            else:
                store[i]-=1
        
        for i in store:
            if store[i] > 0:
                return False
        
        return True