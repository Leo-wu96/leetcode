'''
Author: zixian.wu@shopee.com
Date: 2025-03-28 16:59:33
LastEditTime: 2025-03-28 17:09:46
Description: file content
'''
#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        
        while i >= 0:
            if digits[i] + 1 == 10:
                digits[i] = 0
            else:
                break
            i -= 1
                
        if i<0: digits.insert(0,1)
        else: 
            if digits[i] + 1 < 10:
                digits[i] += 1
                
        return digits
            
        
# @lc code=end

