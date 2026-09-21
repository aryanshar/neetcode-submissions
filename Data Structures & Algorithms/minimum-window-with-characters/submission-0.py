class Solution:
    def minWindow(self, s: str, t: str) -> str:

        freq_t = {}
        for ch in t:
            if ch not in freq_t:
                freq_t[ch] = 1
            else:
                freq_t[ch] += 1

            ## aliter
            # freq_t = Counter(t)
        freq_s = {}
        wind_size = 0
        min_size =float('inf')
        start_idx = -1
        start = 0
        count = 0
        for i, ch in enumerate(s):
            if(ch not in freq_s):
                freq_s[ch] = 1
            else:
                freq_s[ch] += 1

            if(ch in freq_t and freq_s[ch]<=freq_t[ch]):
                count += 1

            if(count==len(t)):
                # window is found
                while(s[start] not in freq_t or (freq_s[s[start]] > freq_t[s[start]])):
                    # remove the elements
                    freq_s[s[start]] -= 1
                    start += 1
                wind_size = i - start + 1
                if(wind_size<min_size):
                    min_size = wind_size
                    start_idx=start
                    
                    # remove elements from left

        if(start_idx==-1):
            return ""
        else:
            return s[start_idx:start_idx+min_size]
            


        