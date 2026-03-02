'''
Author: zixian.wu@shopee.com
Date: 2025-03-28 11:57:35
LastEditTime: 2025-03-28 15:47:10
Description: file content
'''
#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# 二分法: 双指针，有序数组，使得复杂度为O(logn),所以不能遍历整个数组，这会使得O(n)
# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            temp = (left+right)//2
            if nums[temp] < target:
                left = temp + 1
            else:
                right = temp
        return left
        
        
            

# @lc code=end

