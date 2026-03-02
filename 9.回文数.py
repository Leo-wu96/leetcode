'''
Author: zixian.wu@shopee.com
Date: 2025-03-26 18:50:02
LastEditTime: 2025-03-26 18:54:06
Description: file content
'''
#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        numbers = list(str(x))
        a, b = 0, len(numbers)-1
        while a < b or a+1<b:
            if numbers[a] != numbers[b]:
                return False
            a+=1
            b-=1
        return True
        
# @lc code=end

