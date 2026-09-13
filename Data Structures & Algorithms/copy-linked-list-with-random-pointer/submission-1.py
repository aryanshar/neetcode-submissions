"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {}
        temp = head
        while(temp):
            mp[temp] = Node(temp.val)
            temp = temp.next
        new_head = mp[head] if head else None
        temp = head
        while(temp):
            x_random = temp.random
            x_next = temp.next
            mp[temp].random = mp[x_random] if x_random else None
            mp[temp].next = mp[x_next] if x_next else None
            temp = temp.next
        
        return new_head