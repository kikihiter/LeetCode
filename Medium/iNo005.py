class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        本答案未考虑被抛弃字段的部分有效性
        if s==None:
            return
        k1=1
        maxNum1=0
        maxIndex1=0
        k2=1
        maxNum2=0
        maxIndex2=0
        for i in range(len(s)):
            if i-2*k1>=0 and s[i] == s[i-2*k1]:
                #k1+=1
                if maxNum1<k1:
                    maxNum1 = k1
                    maxIndex1 = i-2*k1
                k1+=1
            elif i-2*k1<0 or i-2*k1>=0 and s[i] != s[i-2*k1]:
                k1=1
                
            if i-2*k2+1>=0 and s[i] == s[i-2*k2+1]:
                #k2+=1
                print k2
                if maxNum2<k2:
                    maxNum2 = k2
                    maxIndex2 = i-2*k2+1
                k2+=1
            elif i-2*k2+1<0 or i-2*k2+1>=0 and s[i] != s[i-2*k2+1]:
                k2=1
        
        print maxNum1,maxIndex1,maxNum2,maxIndex2
        if 2*maxNum1+1 > 2*maxNum2:
            return s[maxIndex1:maxIndex1+maxNum1*2+1]
        elif 2*maxNum1+1 < 2*maxNum2:
            return s[maxIndex2:maxIndex2+maxNum2*2]
        """
        if s==None:
            return ""
        l1 = [1 for i in range(len(s))]
        l2 = [1 for i in range(len(s))]
        #print l1,l2
        #print s[l1[3]*2+1]
        #print 2-11[2]*2>=0
        
        for i in range(len(s)):
            #print i-11[i]*2>=0
            while i-l1[i]>=0 and i+l1[i]<len(s) and s[i-l1[i]] == s[i+l1[i]]:
                l1[i]+=1
            while i-l2[i]>=0 and i+l2[i]-1<len(s) and s[i-l2[i]] == s[i+l2[i]-1]:
                l2[i]+=1
        max1 = max(l1)
        max2 = max(l2)
        #print l1,l2,max1,max2,max1*2-1,max2*2-2,l2.index(max2)
        if max1 == max2 == 1:
            return s[0]
        elif max1*2-1 > max2*2-2:
            return s[l1.index(max1)-max1+1:l1.index(max1)+max1]
        elif max1*2-1 < max2*2-2:
            #print "Ture"
            return s[l2.index(max2)-max2+1:l2.index(max2)+max2-1]
        
