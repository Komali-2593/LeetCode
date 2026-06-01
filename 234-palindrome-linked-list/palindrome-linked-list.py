class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []

        current = head
        while current:
            arr.append(current.val)
            current = current.next

        return arr == arr[::-1]