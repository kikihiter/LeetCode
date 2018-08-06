class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xy,yz,zx = 0,0,0
        zxList = [0 for i in range(len(grid))]
        for i in range(len(grid)):
            syz = 0
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    xy += 1
                    syz = max(syz,grid[i][j])
                zxList[j] = max(zxList[j],grid[i][j])
            yz += syz
        for szx in zxList:
            zx += szx
        return xy+yz+zx
