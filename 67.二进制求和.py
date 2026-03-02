'''
Author: zixian.wu@shopee.com
Date: 2025-03-28 17:10:36
LastEditTime: 2025-04-10 10:47:49
Description: file content
'''
#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, temp = len(a)-1, len(b)-1, 0
        result = []
        while i>=0 or j>=0 or temp:
            sum_value = temp
            if i >= 0:
                sum_value += int(a[i])
                i -= 1
            if j >= 0:
                sum_value += int(b[j])
                j -= 1
                
            temp = sum_value // 2
            result.append(str(sum_value%2))
        
        return "".join(reversed(result))
            
            
        
        
        
        
# @lc code=end

