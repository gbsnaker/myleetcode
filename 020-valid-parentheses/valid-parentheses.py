# -*- coding:utf-8 -*-


# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
#


parentheses = {'{': -3, '[': -2, '(': -1, ')': 1, ']': 2, '}': 3}
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2 or len(s)%2 != 0:
            return False
        else:
            def findStart(partS):
                for i in range(len(partS)-1):
                    if parentheses[partS[i]]<0 and parentheses[partS[i+1]]>0 and parentheses[partS[i]]+parentheses[partS[i+1]] == 0:
                        return i
                return -1
            def checkValidStr(candStr, startPos):
                for j in range(startPos+1):
                    if parentheses[candStr[startPos-j]]>0 or parentheses[candStr[startPos+1+j]]<0 or parentheses[candStr[startPos-j]]+parentheses[candStr[startPos+1+j]] != 0:
                        return candStr[0:startPos-j+1]+candStr[startPos+1+j:]
                return candStr[2*(startPos+1):]
            while len(s) > 1:
                pos = findStart(s)
                if pos == -1 or len(s)<pos*2:
                    return False
                s = checkValidStr(s, pos)
            if len(s) == 0:
                return True
            else:
                return False
        
