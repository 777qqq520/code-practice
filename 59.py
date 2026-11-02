#边界收缩法（四层循环）
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0]*n for _ in range(n)]
        top,bottom = 0,n-1
        left,right = 0,n-1
        num = 1
        target = n * n
        while num <= target:
            for i in range(left,right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            for i in range(top,bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            if num <= target:                    #考虑边界条件，结束条件（防止重复填充）
                for i in range(right,left - 1,-1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1
            if num <= target:
                for i in range(bottom,top-1,-1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        return matrix 