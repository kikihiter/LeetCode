#建立一个函数，实现两个列表之间的全组合
def zuhe(list1,list2):
    """
    :type list1[str]
          list2[str]
    :rtype: List[str]
    """
    returnList = []
    for i in list1:
        for j in list2:
            returnList.append(i+j)
    return returnList

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        
        phoneButton = [["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
        buttonList = []
        #strList =[]
        for num in digits:
            num = int(num)-2
            buttonList.append(phoneButton[num])
        
        strList = buttonList[0]
        if len(buttonList) == 1:
            return strList
        #print buttonList
        for i in range(1,len(buttonList)):
            strList = zuhe(strList,buttonList[i])
            #for i in range(len(button)):
        
        return strList
