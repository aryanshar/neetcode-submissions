class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pLeft = [1]*n
        pRight = [1]*n


        i = 1
        while(i<n):
            j = n - 1 -i
            pLeft[i] = pLeft[i-1]*nums[i-1]
            pRight[j] = pRight[j+1]*nums[j+1]
            i +=1
        output = [1]*n

        for i, out in enumerate(output):
            output[i] = pLeft[i]*pRight[i]
        return output