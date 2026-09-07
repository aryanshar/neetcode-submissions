class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        target = 0
        nums = sorted(nums)
        i = 0
        k  = len(nums) -1
        while(i < len(nums)-2):
            j = i + 1
            k = len(nums)- 1
            while(j<k):
                first_num = nums[i]
                second_num = nums[j]
                third_num = nums[k]
                curr_sum = first_num + second_num + third_num
                if (curr_sum == target):
                    res_list = [first_num, second_num, third_num]
                    if len(res):
                        if res_list not in res:
                            res.append(res_list)
                    if len(res) == 0:
                        res.append(res_list)
                    j +=1
                    k -=1
                elif (curr_sum > target):
                    k -= 1
                else:
                    j +=1
            i+=1
            j+=1
            
        return res
            
            
        