class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        stoneJewels = 0
        for stone in S:
            for jewel in J:
                if stone == jewel:
                    stoneJewels += 1
                    break
        return stoneJewels
        