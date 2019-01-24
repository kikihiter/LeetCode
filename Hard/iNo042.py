class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j = 0,len(height)-1
        if j <= 1:
            return 0
        h = min(height[0],height[-1])
        content_all = h * (j+1)
        while i <= j:
            if height[i] <= h:
                i += 1
                continue
            if height[j] <= h:
                j -= 1
                continue
            h_new = min(height[i],height[j])
            content_all += (h_new-h)*(j-i+1)
            h = h_new
        content_pack = 0
        for num in height:
            content_pack += num
        return content_all - content_pack
