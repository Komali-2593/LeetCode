# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current=head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while current:
            
            if current.val==val:
                
                prev.next=current.next
                current=current.next
            else:
                prev=current
                current=current.next
        return dummy.next

        