class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        output = []
        curr_sum = 0
        while(i<j):
            curr_sum = numbers[i]+numbers[j]
            if(curr_sum==target):
                output.append(i+1)
                output.append(j+1)
                break
            elif(curr_sum<target):
                i += 1
            else:
                j -= 1
        
        return output