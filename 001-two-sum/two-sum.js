// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
//
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
//
//
// Example:
//
// Given nums = [2, 7, 11, 15], target = 9,
//
// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].
//
//


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    if (nums.length < 2) {
        return false;
    }
    
    let candiMap = new Map();
    for(let count in nums) {
        if (candiMap.has(nums[count])) {
            return [Number(candiMap.get(nums[count])), Number(count)];
        } else {
            candiMap.set(target-nums[count], count);
        }
    }
};
