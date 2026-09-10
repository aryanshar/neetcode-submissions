class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        store = {}
        i = 0
        j = 0
        max_len = 0
        while(j<len(s)):
            if(s[j] in store and (store[s[j]]>=i)):
                i = store[s[j]] + 1
            store[s[j]] = j
            max_len = max(max_len, j-i+1)
            j += 1
        return max_len