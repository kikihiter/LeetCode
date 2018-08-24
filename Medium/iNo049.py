class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        这题主要是用的排序的一个想法，把元素都切分成一个个字母，先对这些字母排序，然后将有着相同字母序列的元素组合在一起
        看了一个答案，用的是字典，想法其实差不多，但是代码量和运行效率差了很多
        用字典好一些
        """
        if strs == []:
            return []
        strList = []
        
        #建立一个新列表，用于同时存储字符串和字符串拆分的字母
        for i in range(len(strs)):
            letterList = []
            for j in range(len(strs[i])):
                letterList.append(strs[i][j])
                letterList[:] = sorted(letterList[:])
            strList.append([strs[i],i,letterList])
        
        #声明一个函数，用于控制排序
        def takeThrid(ilist):
            return ilist[2]
        #对列表第三项进行升序排序
        strList.sort(key=takeThrid)
        
        #找到相同字母序列的字符串
        ansList = []
        tempAns = []
        elem = strList[0][2]
        for i in range(len(strList)):
            if i != len(strList)-1 and strList[i][2] == elem:
                tempAns.append(strList[i][0])
            elif i != len(strList)-1 and strList[i][2] != elem:
                elem = strList[i][2]
                ansList.append(tempAns)
                tempAns = [strList[i][0]]
            
            elif i == len(strList)-1 and strList[i][2] != elem:
                ansList.append(tempAns)
                ansList.append([strList[i][0]])
            elif i == len(strList)-1 and strList[i][2] == elem:
                tempAns.append(strList[i][0])
                ansList.append(tempAns)
                #ansList.append(strList[i][0])
        
        return ansList
