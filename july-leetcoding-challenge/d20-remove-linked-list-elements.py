"""
Remove all elements from a linked list of integers that have value val.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        curr = head
        prev = head
        while curr and curr.next:
            if curr.next.val == val:
                it = curr.next
                while it and it.val == val:
                    it = it.next
                curr.next = it
            curr = curr.next
        return head