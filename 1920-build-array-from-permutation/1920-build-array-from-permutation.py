class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums)):
            temp=nums[nums[i]]
            ans.append(temp)

        return ans    