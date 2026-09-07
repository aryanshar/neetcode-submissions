from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    def isinAnagramList(self, s: str, strs: List[str]) -> str | None:
        for word in strs:
            if self.isAnagram(s, word):
                return word
        return None
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check_anagram  = {}
        for word in strs:
            toast = self.isinAnagramList(word, check_anagram.keys())
            if word in check_anagram.keys() or toast is not None:
                check_anagram[toast].append(word)
            else:
                check_anagram[word] = [word]
        return list(check_anagram.values())
         
        # for i in range(len(strs)):
        #     ana = [strs[i]]
        #     for m in range(i+1, len(strs)):
        #         if self.isAnagram(strs[i], strs[m]):
        #           ana.append(strs[m])
        #     ans.append(ana)
        # return ans