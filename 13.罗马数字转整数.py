'''
Author: zixian.wu@shopee.com
Date: 2025-03-27 11:08:18
LastEditTime: 2025-03-27 11:55:06
Description: file content
'''
#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result, i = 0, 0
        a = list(s)
        while i < len(a):
            if i+1 == len(a):
                result += map[a[i]]
            elif a[i] == "I":
                if a[i+1] in ["V", "X"]:
                    result += map[a[i+1]]-map[a[i]]
                    i += 1
                else:
                    result += map[a[i]]
            elif a[i] == "X":
                if a[i+1] in ["L", "C"]:
                    result += map[a[i+1]]-map[a[i]]
                    i += 1
                else:
                    result += map[a[i]]
            elif a[i] == "C":
                if a[i+1] in ["D", "M"]:
                    result += map[a[i+1]]-map[a[i]]
                    i += 1
                else:
                    result += map[a[i]]
            else:
                result += map[a[i]]
            i += 1
        
        return result
                    
        
# @lc code=end

