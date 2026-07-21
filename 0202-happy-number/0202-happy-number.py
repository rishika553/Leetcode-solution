class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=set()
        while n != 1:
            if n in seen:
                
                return False
            seen.add(n)
            sums = 0
            while n>0:
                last_digit=n%10
                sums+=last_digit**2
                n=n//10
            n=sums
        
        return True