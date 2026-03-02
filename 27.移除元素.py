'''
Author: zixian.wu@shopee.com
Date: 2025-03-28 11:34:59
LastEditTime: 2025-03-28 11:35:08
Description: file content
'''
#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
        
# @lc code=end

