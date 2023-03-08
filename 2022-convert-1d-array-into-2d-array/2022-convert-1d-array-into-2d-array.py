class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if not (len(original) == m*n): return []
        output = []
        ogi = 0
        for row in range(m):
            col = []
            for i in range(n):
                col.append(original[ogi])
                ogi+=1
            output.append(col)
        return output
            