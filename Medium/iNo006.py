class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zig = ""
        l=len(s)
        if l<=numRows or numRows==1:
            return s
        for i in range(numRows):
            k=0
            while i==0 and (2*numRows-2)*k<l:
                zig = zig + s[(2*numRows-2)*k]
                k+=1
            if i!=0 and i!=numRows-1:
                while (2*numRows-2)*k+i<l:
                    zig = zig + s[(2*numRows-2)*k+i]
                    if (2*numRows-2)*k+2*numRows-i-2<l:
                        zig = zig + s[(2*numRows-2)*k+2*numRows-i-2]
                    k+=1
            while i==numRows-1 and (numRows-1)*(2*k+1)<l:
                zig = zig + s[(numRows-1)*(2*k+1)]
                k+=1
        return zig
