# -*- coding:utf-8 -*-


# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxStrLen = len(s)
        maxLen = len(set(s))
        subStr = ''
        found = False
        if maxLen == maxStrLen:
            return maxLen
        for curLen in range(maxLen, 0, -1):
            beginPos = 0
            if found == True:
                break
            while beginPos+curLen <= maxStrLen:
                subStr = s[beginPos: beginPos+curLen]
                beginPos += 1
                if len(subStr) == len(set(subStr)):
                    found = True
                    break
        return len(subStr)
                    
        
