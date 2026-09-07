class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        def check(board, i, j, index, word):
            if(index==len(word)):
                return True

            if(i<0 or i>=ROWS or j<0 or j>=COLS or word[index]!=board[i][j]):
                return False
            
            temp = board[i][j]
            board[i][j] = "#"
            east = check(board, i+1, j, index+1, word)
            south = check(board, i, j+1, index+1, word)
            west = check(board, i-1, j, index+1, word)
            north = check(board, i, j-1, index+1, word)
            choice = east or north or south or west
            board[i][j] = temp
            return choice

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if(check(board, row, col, 0, word)):
                        return True
        return False