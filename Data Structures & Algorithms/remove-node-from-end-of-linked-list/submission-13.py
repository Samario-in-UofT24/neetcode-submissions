# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Change in-place is more trivial

        - Iteration to get the length
        - Check (length-n) for the index of node for remove
            if 0, return head.next
            else, change the pointer to skip the removed node.
                to locate the node, use a for loop, then use break as work is done
        """

        l = 0
        curr = head

        while curr:
            l += 1
            curr = curr.next

        target = l - n

        if target == 0:
            return head.next

        curr = head
        for i in range(l - 1):
            if (i + 1) == target:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head

