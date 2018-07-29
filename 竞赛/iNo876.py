# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        elif head.next == None:
            return head
        elif head.next.next == None:
            return head.next
        
        headList = []
        while head != None:
            headList.append(head.val)
            head = head.next
        
        newHead = ListNode(headList[len(headList)/2])
        tempHead = newHead
        for i in range(len(headList)/2,len(headList)-1):
            tempHead.next = ListNode(headList[i+1])
            tempHead = tempHead.next
        
        return newHead
