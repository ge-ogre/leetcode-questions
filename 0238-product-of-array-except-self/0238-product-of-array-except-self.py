class Solution(object):
    def productExceptSelf(self, A):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        p = 1
        for i in range(len(A)):
            answer.append(p)
            p *= A[i]
        p = 1
        for i in range(len(A)-1, -1, -1):
            answer[i] = answer[i] * p
            p *= A[i]
        return answer