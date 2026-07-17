class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        maxwealth=0
        for i in range(len(accounts)):
            currentwealth=0
            for j in range(len(accounts[i])):
                currentwealth+=accounts[i][j]
                if currentwealth > maxwealth:
                    maxwealth = currentwealth
        return maxwealth    

