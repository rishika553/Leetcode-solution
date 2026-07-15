from math import factorial
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[]
        for row in range(numRows):
            current=[1]
            for col in range(1,row):
                current.append(ans[row-1][col-1] + ans[row-1][col]) 
                
            if row > 0:
                    current.append(1)
                    
            ans.append(current)


        return ans       
        