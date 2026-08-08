# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Thought:
            The hint states sth like "Divide and Conquer"
            Not exactly same cuz this is not like recursion

        """
         # 1. Find the middle of the linked list
        slow = head
        fast = head.next

        # * Nice method for divide linked list into 2 parts
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split into two halves
        second = slow.next
        slow.next = None

        # 2. Reverse the second half
        prev = None
        curr = second

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        second = prev

        # 3. Merge the two halves alternately
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2