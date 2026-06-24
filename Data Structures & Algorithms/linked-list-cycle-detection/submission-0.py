# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() #using an array makes it a way slower solution
        current = head
        while current and current.next != None:
            if current in seen:
                return True
            else:
                seen.add(current)
                current = current.next
        return False  