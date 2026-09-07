class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        key_store = {}

        n = len(s)
        i,j=0,0

        max_len = 0
        curr_len = 0
        while(j<n):
            if s[j] not in key_store.keys():
                key_store[s[j]] = j
                curr_len = j - i + 1
                max_len = max(max_len, curr_len)
            elif key_store[s[j]] >= i:
                i = key_store[s[j]] + 1
                key_store[s[j]] = j
                curr_len = j - i +1
            else:
                curr_len = j - i + 1
                key_store[s[j]] = j
                max_len = max(max_len, curr_len)
            j += 1
            

        return max_len


        
        