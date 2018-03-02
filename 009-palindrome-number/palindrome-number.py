# -*- coding:utf-8 -*-


# Determine whether an integer is a palindrome. Do this without extra space.
#
# click to show spoilers.
#
# Some hints:
#
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.
#
#


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        digit = 1
        while x/digit >= 10:
            digit *= 10

        while x:
            left = x/digit
            right = x%10
            print left, right
            if left != right:
                return False
            x = (x%digit)/10
            digit /= 100
        return True
