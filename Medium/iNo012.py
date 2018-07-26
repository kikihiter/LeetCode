class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #返回罗马数字符串
        sRoman = ""
        #千位数
        k = num//1000
        num %= 1000
        sRoman += "M"*k
        
        #百位数
        h = num//100
        num %= 100
        if h == 9:
            sRoman += "CM"
        elif 5<=h<9:
            sRoman += "D"+"C"*(h-5)
        elif h == 4:
            sRoman += "CD"
        else:
            sRoman += "C"*h
        
        #十位数
        D = num//10
        P = num%10
        if D == 9:
            sRoman += "XC"
        elif 5<=D<9:
            sRoman += "L"+"X"*(D-5)
        elif D == 4:
            sRoman += "XL"
        else:
            sRoman += "X"*D
        
        #个位数
        if P == 9:
            sRoman += "IX"
        elif 5<=P<9:
            sRoman += "V"+"I"*(P-5)
        elif P == 4:
            sRoman += "IV"
        else:
            sRoman += "I"*P
            
        return sRoman
