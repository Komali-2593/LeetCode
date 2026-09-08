# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None or left == right:
                return head
    # Dummy node
        dummy = ListNode(0)
        dummy.next =head

    # before = reversal start ki mundu unna node
        before = dummy

        for _ in range(left-1):
            before = before.next

    # current = reversal start node
        current = before.next

    # Reverse
        for _ in range(right-left):

        # after = current tarvata unna node
            after = current.next

        # current ni after tarvata ki connect cheyyadam
            current.next = after.next

        # after ni before tarvata ki move cheyyadam
            after.next = before.next

        # before -> after
            before.next = after

    # Head update
        head = dummy.next

        return head