'''
Author: zixian.wu@shopee.com
Date: 2026-03-05 18:45:52
LastEditTime: 2026-03-06 10:53:06
Description: file content
'''
#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry != 0:
            temp = 0
            if l1:
                temp += l1.val
            if l2: 
                temp += l2.val
            temp += carry
            carry = temp // 10
            current.next.val = temp % 10
            l1 = l1.next
            l2 = l2.next
            current = current.next
        return dummy.next
            
            
# @lc code=end

