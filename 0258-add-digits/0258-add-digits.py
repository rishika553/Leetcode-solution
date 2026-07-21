class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >=10:
            sums=0
            while num >0:
                last_digit=num%10
                sums+=last_digit
                num=num//10
            num=sums
        return num    
     



            
