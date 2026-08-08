# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Thought:
            In one operation cycle, store the curr and curr.next(temp). 
            Then check the last two elements a and b in the list.
            Connect b to curr, temp to b, NIL to a.

            The next cycle starts from temp.next
            **Correction**:
                Next cycle should start from temp

            but a may be the same as temp. Problems? - No

            Theta( n ^ 2 )

        Implementation:

        """
        curr = head

        # >= 2 terms
        while curr and curr.next:

            temp = curr.next
            a = temp

            # break if temp is the last node 
            if a.next is None:
                break

            while a.next.next is not None:

                a = a.next

            b = a.next

            curr.next = b
            b.next = temp
            a.next = None

            curr = temp
            



