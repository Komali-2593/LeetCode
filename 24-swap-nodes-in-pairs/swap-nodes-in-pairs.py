# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d1=ListNode(0)
        prev=d1
        d1.next=head
        
        
        current=head
        while prev.next and prev.next.next:
            first=prev.next
            second=first.next
            first.next=second.next
            prev.next=second
            second.next=first
            prev=first
        
        return d1.next


        