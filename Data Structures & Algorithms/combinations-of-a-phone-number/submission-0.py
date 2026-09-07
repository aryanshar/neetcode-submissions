class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = ["","", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        if not digits:
            return []
        def check(digits, i, n, output):
            if(i==n):
                # base case
                # print and return
                res.append(output)
                return

            digit = int(digits[i])
            for k in keypad[digit]:
                check(digits, i+1, n, output+k)
        check(digits, 0, len(digits), "")
        return res