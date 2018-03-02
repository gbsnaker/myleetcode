# -*- coding:utf-8 -*-


# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output:  321
#
#
#
# Example 2:
#
# Input: -123
# Output: -321
#
#
#
# Example 3:
#
# Input: 120
# Output: 21
#
#
#
# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        neg_flag = False
        if x_str[0] == '-':
            x_str = x_str[1:]
            neg_flag = True
        reversed_str = x_str[::-1]
        value = int(reversed_str)
        if value > (2**31):
            return 0
        elif value == (2**31) and not neg_flag:
            return 0
        else:
            if neg_flag:
                reversed_str = '-' + reversed_str
            return int(reversed_str)
