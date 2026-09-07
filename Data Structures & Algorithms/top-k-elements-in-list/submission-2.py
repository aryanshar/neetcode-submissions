class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ans = {}

        for num in nums:
            
            if num in ans:
                ans[num] += 1
            else:
                ans[num] = 1

        
        ans = dict(sorted(ans.items(), key=lambda item: item[1], reverse=True))

        new_ans = []
        idx = 0
        for ke,val in ans.items():
            if(k<=0):
                break
            new_ans.append(ke)
            k -= 1
        
        return new_ans