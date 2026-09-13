# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # two pointer approach
        # fast and slow pointer
        dummy = ListNode(0, head)
        slow = fast = dummy
        idx = 0
        while(fast.next and idx<1000):
            slow = slow.next
            fast = fast.next.next
            if(slow==fast):
                return True
            if(fast==None):
                return False
            idx += 1
        
        return False