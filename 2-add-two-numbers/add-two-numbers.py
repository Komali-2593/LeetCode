# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1=[]
        arr2=[]
        head=None
        current=None
        while l1:
            arr1.append(l1.val)
            l1=l1.next
        while l2:
            arr2.append(l2.val)
            l2=l2.next
        arr1[::]=arr1[::-1]
        arr2[::]=arr2[::-1]
        num1 = int("".join(map(str, arr1)))
        num2 = int("".join(map(str, arr2)))
        sum=num1+num2
        sum=str(sum)[::-1]
        for digit in str(sum):
            new_node = ListNode(int(digit))

            if head is None:
                head = new_node
                current = new_node
            else:
                current.next = new_node
                current = new_node
        return head
        


        