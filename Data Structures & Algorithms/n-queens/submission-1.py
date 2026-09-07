class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []
        def canPlace(board, i, j, n):
            # check along column
            check1, check2, check3 = True, True, True
            for k in range(i):
                if(board[k][j]=="Q"):
                    check1 = False

            # check left diagonal
            row = i-1
            col = j-1
            while(row>=0 and col>=0):
                if(board[row][col]=="Q"):
                    check2 = False
                row -= 1
                col -= 1
                

            # check right diagonal
            row = i-1
            col = j+1
            while(row>=0 and col<n):
                if(board[row][col]=="Q"):
                    check3 = False
                row -= 1
                col += 1
                
            return check1 and check2 and check3
        
        def NQueen(board, i, j, n):

            # base case
            if(i==n):
                res.append(["".join(row) for row in board])
                return

            if(j==n):
                # move to next row
                return

            # recursive case
            # place the queen at i, j if canplace
            if(canPlace(board, i, j, n)):
                board[i][j] = "Q"
                check = NQueen(board, i+1, 0, n)
                board[i][j] = "."
                # if(check):
                #     board[i][j] = "."
                #     return True
            NQueen(board, i, j+1, n)
        
        NQueen(board, 0, 0, n)
        return res
            