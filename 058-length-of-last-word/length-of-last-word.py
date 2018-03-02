# -*- coding:utf-8 -*-


# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5
#
#


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if len(s) == 0:
            return 0;
        else:
            while s.rfind(' ', 0, len(s)) == (len(s) - 1):
                s = s[0:len(s)-1]
                if len(s) == 0:
                    return 0
            return len(s)-s.rfind(' ', 0, len(s))-1
