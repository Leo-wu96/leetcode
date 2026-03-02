'''
Author: zixian.wu@shopee.com
Date: 2025-03-27 11:55:48
LastEditTime: 2025-03-27 17:37:24
Description: file content
'''
#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = []
        first = strs[0]
        if len(strs) == 1:
            return strs[0]
        if len(first) > 0:
            j = 0
            while True:
                for i in strs[1:]:
                    if j >= len(i) or j >= len(first):
                        return "".join(result)
                    if first[j] != i[j]:
                        return "".join(result)
                
                result.append(first[j])
                j += 1
                    
        
        return "".join(result)
    
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs[0]) == 1: return strs[0]
        prefix = strs[0]
        for i in strs:
            while strs[i][:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
        
        return prefix
            
        
        
# @lc code=end


