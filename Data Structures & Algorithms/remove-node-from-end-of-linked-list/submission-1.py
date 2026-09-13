# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        first = second = dummy


        # take second_pointer so that first and second have
        # n distance between them
        for _ in range(n):
            second = second.next
        
        # then take both till last one reaches the end
        while(second.next):
            first = first.next
            second = second.next

        # now start.next needs to be deleted
        first.next = first.next.next

        return dummy.next