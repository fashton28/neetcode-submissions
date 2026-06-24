# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        counter = 0
        current = head

        while current:
            counter += 1
            current = current.next

        if counter - n == 0:
            return head.next
        
        current = head
        removalPosition = 1

        while removalPosition != counter - n:
            current = current.next
            removalPosition += 1 
       
        current.next = current.next.next
        
        return head




            