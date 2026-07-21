class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
       
        for i in xrange(1,x+1):
            
            sqr=i*i
            if sqr==x:
                return i
            if sqr > x:
                return   i-1  
           



        