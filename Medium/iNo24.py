# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        leftHead = []
        rightHead = []
        
        #节点数小于2的时候
        if head == None:
            return head
        elif head.next == None:
            return head
        
        newHead = ListNode(head.next.val)
        tempHead = newHead
        ifLeft = True
        #将原head的各个节点分别存放到left和right的Head列表中
        while head != None:
            if ifLeft == True:
                leftHead.append(head.val)
                ifLeft = False
            elif ifLeft == False:
                rightHead.append(head.val)
                ifLeft = True
            head = head.next
        
        #分别从leftHead和rightHead中提取数值作为节点的值
        i=0
        while i != len(leftHead)-1:
            newHead.next = ListNode(leftHead[i]) 
            try:
                newHead.next.next = ListNode(rightHead[i+1])
            except:
                newHead.next.next = ListNode(leftHead[i+1])
                break
            newHead = newHead.next.next
            i += 1
        else:
            newHead.next = ListNode(leftHead[-1])
        
        return tempHead
