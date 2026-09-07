class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
        # stringA = {}
        # for letter in s:
        #     if letter in stringA.keys():
        #         stringA[letter] += 1
        #     else:
        #         stringA[letter] = 1
        # for letter in t:
        #     if letter not in stringA.keys():
        #         return False
        #     else:
        #         stringA[letter] -= 1
        
        # for v in stringA.values():
        #     if v!= 0:
        #         return False
        # return True
        