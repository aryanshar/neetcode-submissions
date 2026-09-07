# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        temp = head
        idx = 1
        if temp==None:
            return []
        count = 0
        temp2 = temp
        while(temp2):
            temp2 = temp2.next
            count += 1
        if(n>count):
            return head
        n = count - n + 1
        while(temp and idx<n):
            prev = temp
            temp = temp.next
            idx += 1
        if(n==1):
            # last element
            temp = head
            temp2 = head.next
            head = temp2
            del temp

        elif(idx==n):
            prev.next = temp.next
            del temp
            # some middle element

        return head