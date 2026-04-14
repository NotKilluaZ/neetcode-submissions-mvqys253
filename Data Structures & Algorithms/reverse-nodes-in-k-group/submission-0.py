# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        end = head
        prev = None
        new_head = None
        while end:
            for i in range(k - 1):
                if not end.next:
                    return new_head if new_head else head
                end = end.next
            next_start = end.next
            end.next = None
            
            reverse_head = self.reverse(start)

            if not new_head:
                new_head = reverse_head

            if prev:
                prev.next = reverse_head

            start.next = next_start
            prev = start
            start = next_start
            end = start

        return new_head if new_head else head

    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev