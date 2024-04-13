# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return head

        pointer = head
        head = head.next
        pointer.next = None
        while head.next:
            new_head = head.next

            head.next = pointer
            pointer = head
            head = new_head
        head.next = pointer
        return head