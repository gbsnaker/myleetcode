# -*- coding:utf-8 -*-


# Write a function to find the longest common prefix string amongst an array of strings.
#


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def longestPrefix(str1, str2):
            lastStr = ''
            length = min(len(str1), (str2))
            if length > 0:
                for j in range(length):
                    if str1[:j+1] != str2[:j+1]:
                        return lastStr
                    else:
                        lastStr = str1[:j+1]
                return lastStr
            else:
                return lastStr
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            stra = strs[0]
            for i in range(len(strs)-1):
                strb = strs[i+1]
                stra = longestPrefix(stra, strb)
            return stra
        
