class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # lets do O(n) space soln
        # rotation by 90 degrees clockwise
        # mat[0][0] = mat[0][-1]
        # mat[0][1] = mat[1][-1]
        # mat[i][j] = mat[j][n-1-i]
        # mat[i][j] = 
        # mat[i] = ith row will become n-1-jth column in the transformation


        # result = {}
        # top, bottom = 0, len(matrix) - 1
        # left, right = 0, len(matrix[0]) - 1
        # n = len(matrix)
        # while top <= bottom and left <= right:
        #     # 1. Traverse from Left to Right along the Top row
        #     for i in range(left, right + 1):
        #         if(top==0):
        #             result[(top,i)]=matrix[top][i]
        #         else:
        #             temp = matrix[top][i]
        #             matrix[top][i] = result[(i,n-1-top)]
        #             del result[(i,n-1-top)]
        #             result[(top,i)] = temp
        #     top += 1  # Move top boundary down
            
        #     # 2. Traverse from Top to Bottom along the Right column
        #     for i in range(top, bottom + 1):
        #         temp = matrix[i][right]
        #         matrix[i][right] = result[(right,n-1-i)]
        #         del result[(right,n-1-i)]
        #         result[(i, right)] = temp
        #     right -= 1  # Move right boundary left
            
        #     # Make sure we are on a different row than we started
        #     if top <= bottom:
        #         # 3. Traverse from Right to Left along the Bottom row
        #         for i in range(right, left - 1, -1):
        #             temp = matrix[bottom][i]
        #             matrix[bottom][i] = result[(i,n-1-bottom)]
        #             del result[(i,n-1-bottom)]
        #             result[(bottom, i)] = temp
        #         bottom -= 1  # Move bottom boundary up
                
        #     # Make sure we are on a different column than we started
        #     if left <= right:
        #         # 4. Traverse from Bottom to Top along the Left column
        #         for i in range(bottom, top - 1, -1):
        #             result.append(matrix[i][left])
        #             temp = matrix[i][left]
        #             matrix[i][left] = result[(left,n-1-i)]
        #             del result[(left,n-1-i)]
        #             result[(i, left)] = temp
        #         left += 1  # Move left boundary right
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        

                