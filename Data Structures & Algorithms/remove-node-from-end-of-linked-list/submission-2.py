# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head

        for _ in range(n):
            r = r.next

        while r:
            r = r.next
            l = l.next

        remove = l.next
        after = remove.next
        l.next = after

        return dummy.next