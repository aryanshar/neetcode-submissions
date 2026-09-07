class Solution:
    def isAllowed(self, c: str) -> bool:
        if c >= "A" and c <= "Z":
            return True
        elif c <="z" and c>= "a":
            return True
        elif c <= "9" and c>= "0":
            return True
        else:
            return False
    def isPalindrome(self, s: str) -> bool:
        inp = ''
        for cha in s:
            if self.isAllowed(cha):
                inp += cha.lower()
        i = 0
        j = len(inp)- 1
        print(inp)
        while(i<len(inp) and i<=j):
            if (inp[i] == inp[j]):
                i +=1
                j -=1
            else:
                return False
        return True
            
        