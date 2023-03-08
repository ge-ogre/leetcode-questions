class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        store={}
        if n<0:
            return False
        
        while n!=1:
            acc=0
            for i in str(n):
                acc+=pow(int(i),2)
            n=acc
            if n in store:
                return False
            else:
                store[n]=1
            print(n)
            
        return True