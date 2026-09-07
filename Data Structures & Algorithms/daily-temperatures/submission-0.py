class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rev_temp = temperatures
        stack = []
        output = [0]*len(rev_temp)
        max_temp = 0
        max_temp_index = -1

        for i in range(len(rev_temp)):
            if len(stack)==0:
                stack.append(i)
                max_temp = max(max_temp, rev_temp[i])
            elif rev_temp[stack[-1]] >= rev_temp[i]:
                stack.append(i)
            else:
                # compute output
                max_temp = max(max_temp, rev_temp[i])
                while(len(stack) and rev_temp[stack[-1]]<rev_temp[i]):
                    top = stack.pop()
                    output[top] = i - top
                stack.append(i)
        while(len(stack)):
            top = stack.pop()
            output[top] = 0
        return output

