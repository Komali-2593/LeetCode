# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        fast=head
        slow=head

        while fast and fast.next:
            prev=slow
            fast=fast.next.next
            slow=slow.next
        prev.next=slow.next
        return dummy.next

        