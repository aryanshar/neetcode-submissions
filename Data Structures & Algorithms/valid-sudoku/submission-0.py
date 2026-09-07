import numpy as np
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = {k:[] for k in range(9)}
        cols = {k:[] for k in range(9)}
        box = defaultdict(list)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                
                # index for 3x3 bbox
                idx_box = (i//3,j//3)
                if num in rows[i] or num in cols[j] or num in box[idx_box]:
                    return False
                
                rows[i].append(num)
                cols[j].append(num)
                box[idx_box].append(num)
            
        return True