'''
Author: zixian.wu@shopee.com
Date: 2025-03-27 17:38:25
LastEditTime: 2026-03-03 14:32:39
Description: file content
'''
#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        stack = []
        for i in s:
            if i in ["{", "(", "["]:
                stack.append(i)
            if i in ["}", ")", "]"]:
                if len(stack) == 0:
                    return False
                j = stack.pop()
                if i == "}" and j != "{":
                    return False
                elif i == ")" and j != "(":
                    return False
                elif i == ']' and j != "[":
                    return False
        
        return stack == []
    
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {"}":"{", ")": "(", "]":"["}
        for i in s:
            if i in bracket_map.values():
                stack.append(i)
            if i in bracket_map.keys():
                if stack == [] or stack.pop() != bracket_map[i]:
                    return False
        return stack == []
                
# @lc code=end
