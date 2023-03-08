class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l, r = 0, len(arr)-1
        while (l < r):
            mid = l + (r - l) / 2
            if arr[mid] < arr[mid+1] : 
                l = mid + 1 
            else: 
                r = mid 
        return l