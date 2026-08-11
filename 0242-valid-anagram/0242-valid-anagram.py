class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        t_list=list(t)
        for char in s:
            if char not in t_list:
                return False
            index = t_list.index(char)
            t_list.pop(index)

        return True

        
        