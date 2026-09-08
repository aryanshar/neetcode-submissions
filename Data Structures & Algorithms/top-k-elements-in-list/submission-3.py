from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        
        ans = [x for x in mp.keys()]
        ans.sort(key=lambda x: mp[x], reverse=True)
        ans = ans[:k]
        return ans
