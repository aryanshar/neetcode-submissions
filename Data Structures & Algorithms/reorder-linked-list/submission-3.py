# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        head_l = []
        while(temp!=None):
            head_l.append(temp)
            temp = temp.next

        
        n = len(head_l)
        i = 0
        while(i<n//2):
            h = head_l[i]
            t = head_l[n-1-i]
            h_next = h.next
            t_next = t.next
            # reorder
            h.next = t
            t.next = h_next
            i += 1
        
        head_l[i].next = None


        
        