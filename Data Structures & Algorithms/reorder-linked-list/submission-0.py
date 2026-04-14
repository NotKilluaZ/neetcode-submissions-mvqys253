# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            mid = mid.next

        second = mid.next
        prev = None
        mid.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            second = temp2
            first = temp1