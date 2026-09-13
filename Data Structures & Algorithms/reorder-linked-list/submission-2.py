# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        store = {}
        n = 0
        while(temp):
            store[n] = temp
            n += 1
            temp = temp.next
        left = 0
        right = n-1
        while(left<right):
            third = store[left].next
            new_second = store[right]
            store[left].next = new_second
            new_second.next = third
            left += 1
            right -= 1
        store[left].next = None

            