from collections import defaultdict, Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def isSubstring(s1,s2):
            if(len(s1)>len(s2)):
                return False
            store = Counter(s1)
            window = Counter(s2[:len(s1)])
            if store==window:
                return True
        
            for i in range(len(s1), len(s2)):
                ch = s2[i]
                if ch not in window:
                    window[ch] = 1
                else:
                    window[ch] += 1
                
                old_ch = s2[i-len(s1)]
                window[old_ch] -= 1

                if window[old_ch] == 0:
                    del window[old_ch]
                
                if window==store:
                    return True
            
            return False

        return isSubstring(s1,s2)
        