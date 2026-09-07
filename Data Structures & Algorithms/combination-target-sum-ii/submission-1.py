class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        def genAll(candidates, i, n, target, output):
            candidates.sort()
            if(target==0):
                return [output]
            if(i==n or target<0):
                return []

            
            pick_i = genAll(candidates, i+1, n, target-candidates[i], output+[candidates[i]])
            new_i = i+1
            while(new_i!=n and candidates[new_i]==candidates[i]):
                new_i += 1
            not_i = genAll(candidates, new_i, n, target, output)
            # not_i = [x for x in not_i if x not in pick_i]
            return pick_i + not_i
        return genAll(candidates, 0, len(candidates), target, [])
        