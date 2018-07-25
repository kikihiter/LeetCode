class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        posNum = True
        if str == "":
            return 0
        if str[0]=='-':
            posNum = False
            str = str[1:]
        elif str[0]=='+':
            str = str[1:]
        try:
            int(str[0])
        except:
            return 0
        rStr = ""
        for i in str:
            try:
                int(i)
            except:
                break
            rStr = rStr + i
        rStr = rStr.lstrip('0')
        if rStr == "":
            return 0
        if posNum == False:
            return max(-int(rStr),-2147483648)
        print rStr
        return min(int(rStr),2147483647)
