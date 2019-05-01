# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        pList = [root]
        cList = []
        ansList = []
        tempList = []
        while len(pList) != 0 or len(cList) != 0:
            while len(pList) != 0:
                if pList[-1].right != None:
                    cList.insert(0,pList[-1].right)           
                if pList[-1].left != None:
                    cList.insert(0,pList[-1].left)
                tempList.append(pList[-1].val)
                del pList[-1]
            ansList.append(tempList[::-1])
            tempList = []
            pList = cList
            #pList[:] = cList[:]
            cList = []
        return ansList[::-1]
