class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        store = {}
        i = 0
        j = 0
        n = len(s)
        max_len = 0
        while(j<len(s)):
            if (s[j] not in store):
                curr_len = j - i + 1
            elif(s[j] in store and (store[s[j]]<i)):
                curr_len = j - i + 1
            else:
                i = store[s[j]] + 1
            store[s[j]] = j
            j += 1
            max_len = max(max_len, curr_len)
        
        return max_len