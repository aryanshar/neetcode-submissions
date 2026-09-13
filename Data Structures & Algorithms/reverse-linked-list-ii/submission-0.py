# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if(head==None):
            return None
        dummy = ListNode(-1)
        dummy.next = head
        prev = None
        idx = 1
        begin = dummy
        tail = None
        while(head):
            if(idx>right):
                break
            tmp = head.next
            if(idx<left):
                begin = head
            if(idx==left):
                tail = head
            if(idx>=left and idx<=right):
                # reverse the list
                head.next = prev

            prev = head
            head = tmp
            idx += 1
        begin.next = prev
        tail.next = head

        return dummy.next
