class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rsum=[]
        cursum=0
        for i in range(len(nums)):
            cursum+=nums[i]
            rsum.append(cursum)
        return rsum  
