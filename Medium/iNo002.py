# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t = 0
        l = ListNode(-1)
        il = l
        while l1 and l2:
            if l1.val + l2.val + t >= 10:
                il.next = ListNode(l1.val + l2.val + t - 10)
                t = 1
            else:
                il.next = ListNode(l1.val + l2.val + t)
                t = 0
            il = il.next
            l1 = l1.next
            l2 = l2.next
        while l1 and l2==None:
            if t == 1 and l1.val==9:
                il.next = ListNode(0)
                t = 1
            elif t == 1 and l1.val<9:
                il.next = ListNode(l1.val + 1)
                t = 0
            elif t == 0:
                il.next = l1
                break
            il = il.next
            l1 = l1.next
        while l2 and l1==None:
            if t == 1 and l2.val==9:
                il.next = ListNode(0)
                t = 1
            elif t == 1 and l2.val<9:
                il.next = ListNode(l2.val + 1)
                t = 0
            elif t == 0:
                il.next = l2
                break
            il = il.next
            l2 = l2.next
        if t == 1:
            il.next = ListNode(1)
        return l.next
