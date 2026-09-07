class Solution:
    def searchBin(self, matrix, start, end, target):
        mid = (start+end)//2
        if (start>end):
            return False
        elif (matrix[mid]==target):
            return True
        elif (matrix[mid]<target):
            return self.searchBin(matrix, mid+1, end, target)
        else:
            return self.searchBin(matrix, start, mid-1, target)
        
    def checkmatrix(self, matrix, start, end, target):
        mid_row = (start+end)//2
        if(start>end):
            return False
        elif (self.searchBin(matrix[mid_row], 0, len(matrix[-1])-1, target)):
            return True
        elif (matrix[mid_row][-1]<target):
            new_mid = (mid_row+1+end)//2
            return self.checkmatrix(matrix, mid_row+1, end, target)
        elif (matrix[mid_row][0]>target):
            new_mid = (start+mid_row-1)//2
            return self.checkmatrix(matrix, start, mid_row-1, target)
        else:
            return False    

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[-1])

        s_row = 0
        e_row = rows-1

        s_cols = 0
        e_cols = cols-1

        out = self.checkmatrix(matrix, s_row, e_row,target)
        return out

