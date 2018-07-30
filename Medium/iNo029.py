#使被除数不断翻倍，加快运行速度
def processMi(dividend, divisor):
    mi = 0
    n = 0
    while divisor <= dividend:
            n = n + 2**mi
            mi += 1
            dividend -= divisor
            divisor += divisor
            #print n,"Ok"
    return dividend,n

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #符号处理
        pos = True
        if dividend < 0 and divisor > 0:
            pos = False
            dividend = -dividend
        elif dividend > 0 and divisor < 0:
            pos = False
            divisor = -divisor
        elif dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        
        mi = 0
        while divisor <= dividend:
            dividend,n = processMi(dividend, divisor)
            #mi += processMi(dividend, divisor)[1]
            #print dividend, mi
            mi += n
        """
        临界问题，这里我是搞不明白,感受一下这三个例子（是系统给出的两个答案，你们可以自己输入看看）
        Example1:
        input: -2147483648
               -1
        output:2147483647
        
        Example2:
        input: -214748364865
               -1
        output:214748364865
        
        Example3:
        input: -2147483648
               1
        output:-2147483648
        """    
        if pos == False:
            mi = -mi
        if mi > 2147483647:
            mi = 2147483647
        return mi
