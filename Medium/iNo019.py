# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return head
        if head.next == None and n == 1:
            return None
        i=0
        newHead = head
        headList = []
        while newHead != None:
            i += 1
            headList.append(newHead.val)
            newHead = newHead.next
        print headList
        del headList[i-n]
        #print headList
        
        newHead = ListNode(headList[0])
        tepHead = newHead
        for j in range(1,len(headList)):
            tepHead.next = ListNode(headList[j])
            tepHead = tepHead.next
        return newHead
    
    
    """
    #从答案里选了一个最快的，这个算法相当于只遍历了一遍就完成了，所以比其他人快
        def removeNthFromEnd(self, head, n):
        k = n
        node = head
        nthNode = head
        
        #这一步，实际上，只是个计数器，可以把nthNode的相关操作都看作是计数
        while n:
            nthNode = nthNode.next
            n -= 1
        
        #这里考虑的是n超过node节点数的情况，实际上不需要考虑，因为问题说n是有意义的
        if nthNode == None:
            return head.next if k > 1 else None
        
        #运用nthNode计数，Node计的数实际上是len-n,运用node将操作移动到len-n的位置，实际上就是删除指定节点的位置
        while nthNode.next != None:
            nthNode = nthNode.next
            node = node.next
        
        #找到目标节点进行跳过，连接到下个节点
        node.next = node.next.next
        return head
    
    """
    """
    另一个几乎是最慢的算法67ms，但是思想和最快的其实是一样的，所以说leetcode很神奇
      fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
            print(fast.val,slow.val)
        slow.next = slow.next.next
        return head
    """
