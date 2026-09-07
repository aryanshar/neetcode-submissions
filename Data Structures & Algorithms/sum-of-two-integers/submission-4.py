class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        partial_sum = a^b
        carry = (a&b)<<1
        mask = 0xFFFFFFFF
        while(carry):
            new_partial_sum = (partial_sum^carry)&mask
            new_carry = ((partial_sum&carry)<<1)&mask
            partial_sum = new_partial_sum
            carry = new_carry
            if(partial_sum>0x7FFFFFFF):
                partial_sum=~(partial_sum^mask)
        
        return partial_sum