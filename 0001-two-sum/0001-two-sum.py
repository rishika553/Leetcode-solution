class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        freq={}
        for i in range(len(nums)):
            a=target-nums[i]
            if a in freq:
                return [i,freq[a]]
            
            freq[nums[i]]=i