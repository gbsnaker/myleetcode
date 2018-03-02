# -*- coding:utf-8 -*-


# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsSorted = sorted(nums)
        import bisect
        pos = bisect.bisect(numsSorted, target/2)
        smallVec = numsSorted[0:pos]
        small = 0
        large = 0
        if smallVec[len(smallVec)-1]+smallVec[len(smallVec)-2] == target:
            large = smallVec[len(smallVec)-1]
            small = smallVec[len(smallVec)-2]
        if len(smallVec) < len(numsSorted):
            largeVec = numsSorted[pos:len(numsSorted)]
            if  len(largeVec)>1 and largeVec[0]+largeVec[1] == target:
                large = largeVec[1]
                small = largeVec[0]
            else:
                for smallItem in smallVec:
                    foundFlag = False
                    for largeItem in reversed(largeVec):
                        sumValue = smallItem+largeItem
                        if sumValue == target:
                            foundFlag = True
                            small = smallItem
                            large = largeItem
                            break
                        elif sumValue < target:
                            break
                    if foundFlag == True:
                        break
        if small == large:
            smallPos = nums.index(small)
            largePosVec = nums[smallPos+1:len(nums)]
            largePos = smallPos+1+largePosVec.index(large)
        else:
            smallPos = nums.index(small)
            largePos = nums.index(large)
        return [smallPos, largePos]
            
