'''
Author: zixian.wu@shopee.com
Date: 2025-04-10 15:06:09
LastEditTime: 2025-04-11 17:28:00
Description: file content
'''
#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 0, x
        while left < right:
            temp = (left + right) // 2
            if temp ** 2 == x: return temp
            elif temp ** 2 > x:
                right = temp
            else: left = temp + 1

        return left - 1
        
# @lc code=end

