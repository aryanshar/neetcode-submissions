# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = None
        if list1!=None and list2!=None:
            if list1.val <= list2.val:
                head = list1
                curr = list1
                list1 = list1.next
            else:
                head = list2
                curr = list2
                list2 = list2.next
        elif list1!=None:
                head = list1 if head is None else head
                curr = list1
                list1 = list1.next
        elif list2!=None: 
                head = list2 if head is None else head
                head = list2
                curr = list2
                list2 = list2.next
        print(head)
        while(list1!=None and list2!=None and list1.val is not None and list2.val is not None):
            if list1.val<=list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        while(list2 is not None):
            curr.next = list2
            curr = curr.next
            list2 = list2.next
        while(list1 is not None):
            curr.next = list1
            curr = curr.next
            list1 = list1.next
        
        if head is None:
            head = list1 if list1 is not None else list2
        return head

        