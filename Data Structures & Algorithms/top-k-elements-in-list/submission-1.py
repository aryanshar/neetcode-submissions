class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            if num in num_freq.keys():
                num_freq[num] += 1
            else:
                num_freq[num] = 1
        
        num_freq = sorted(num_freq.items(), key = lambda x:x[1], reverse = True)
        ans = []
        for i, ke in enumerate(num_freq):
            if i==k:
                return ans
            ans.append(ke[0])
        return ans
        