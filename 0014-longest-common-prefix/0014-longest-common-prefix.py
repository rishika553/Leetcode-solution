class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result=""
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if len(strs[j])<= i:
                    return result
                if strs[0][i]!=strs[j][i]:
                    return  result
                
            result +=strs[j][i]
        return result   