'''
Author: zixian.wu@shopee.com
Date: 2025-03-28 11:19:22
LastEditTime: 2025-03-28 11:32:22
Description: file content
'''
#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        temp = []
        i = 0
        while i < len(nums):
            if nums[i] in temp:
                nums.pop(i)
                i-=1
            else: 
                temp.append(nums[i])
            i += 1
        
        return len(nums)
# @lc code=end

