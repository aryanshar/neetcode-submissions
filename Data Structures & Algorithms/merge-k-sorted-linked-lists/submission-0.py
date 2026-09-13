# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        R = len(lists)
        output = []
        heap = []
        dummy = ListNode(-1)
        for row, l in enumerate(lists):
            if(l==None):
                continue
            ele = l.val
            row_idx = row
            heapq.heappush(heap, (ele, row, l))
        heapq.heapify(heap)
        temp = dummy
        while(heap):
            ele, row, node = heapq.heappop(heap)
            temp.next = node
            temp = node
            if(node.next):
                # can push its next element in heap
                node = node.next
                heapq.heappush(heap, (node.val, row, node))
        
        return dummy.next
        