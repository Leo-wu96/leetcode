'''
Author: zixian.wu@shopee.com
Date: 2025-03-27 18:24:24
LastEditTime: 2025-03-28 11:06:50
Description: file content
'''
#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 递归深度可能会受到 Python 的递归限制，尤其在处理较长的链表时。如果链表非常长，可能会导致栈溢出。在这种情况下，可以考虑使用迭代的方法。

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
                
            current = current.next
        if list1:
            current.next = list1
        else:
            current.next = list2
            
        return dummy.next

# @lc code=end