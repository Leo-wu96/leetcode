'''
Author: zixian.wu@shopee.com
Date: 2025-03-26 17:53:09
LastEditTime: 2025-03-26 18:41:30
Description: file content
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        number_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in number_to_index:
                return [number_to_index[complement], i]
            number_to_index[num] = i
        return []
        
        
        
# @lc code=end

