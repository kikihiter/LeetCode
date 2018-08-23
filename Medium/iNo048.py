class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n/2):
            for j in range(n/2):
                matrix[i][j],matrix[j][n-i-1],matrix[n-i-1][n-j-1],matrix[n-j-1][i] = matrix[n-j-1][i],matrix[i][j],matrix[j][n-i-1],matrix[n-i-1][n-j-1]
                
        if n%2 != 0:
            for i in range(n/2):
                matrix[n/2][i],matrix[i][n/2],matrix[n/2][n-i-1],matrix[n-i-1][n/2] = matrix[n-i-1][n/2],matrix[n/2][i],matrix[i][n/2],matrix[n/2][n-i-1]
