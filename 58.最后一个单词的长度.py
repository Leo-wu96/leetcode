'''
Author: zixian.wu@shopee.com
Date: 2025-03-28 15:50:10
LastEditTime: 2025-03-28 16:52:16
Description: file content
'''
#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        i = len(l)-1
        while l[i] == " ":
            i -= 1
        return len(l[i])
        
        
# @lc code=end

