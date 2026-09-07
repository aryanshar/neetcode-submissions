class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            freq_map = {}
            start = 0
            max_len = 0
            win_len = 0
            max_freq = 0
            for j in range(len(s)):
                # add curr elem to window
                curr_elem = s[j]
                if curr_elem in freq_map:
                    freq_map[curr_elem] += 1
                else:
                    freq_map[curr_elem] = 1
                win_len = j - start + 1
                max_freq = max([v for v in freq_map.values()])
                # check if valid
                if (win_len - max_freq > k):
                    freq_map[s[start]] -= 1
                    win_len -= 1
                    start += 1
                max_len = max(max_len, win_len)
            return max_len
            # if ch not in win and updated_start==start:
            #     win[ch] = j
                
            # else:
            #     # this is a continuation string where k is getting reduced
            #     if(k>0):
            #         # do sonmething
            #     else:
            #         # do something
        