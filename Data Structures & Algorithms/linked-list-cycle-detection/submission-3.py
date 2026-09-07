# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while(fast):
            if fast.next==slow and fast.next is not None:
                return True
            elif fast.next is not None:
                fast = fast.next
                fast = fast.next
                slow = slow.next
            else: return False
        return False

        