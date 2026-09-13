# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        idx = 0
        while(head and idx<1000):
            if(head in visited):
                return True
            visited.add(head)
            head = head.next
            idx += 1
        return False