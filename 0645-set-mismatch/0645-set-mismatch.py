class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
                
            else:
                freq[num]=1
        duplicate = 0
        missing = 0

                
        for i in range(1,len(nums)+1):
            
            if i not in freq:
                missing=i
                
            elif freq[i]==2:
                duplicate=i
        return [duplicate, missing]