class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def genAll(i, n, left, right, output):
            if(i==2*n):
                res.append(output)
                return
            
            if(left<n):
                genAll(i+1, n, left+1, right, output+"(")
            if(right<left):
                genAll(i+1, n, left, right+1, output+")")
        genAll(0, n, 0, 0, "")
        return res
        