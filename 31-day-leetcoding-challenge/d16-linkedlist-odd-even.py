"""
Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        odd = head
        even = head.next
        even_head = head.next
        while odd and odd.next and odd.next.next:
            odd.next = odd.next.next
            if odd.next:
                even.next = odd.next.next
            else:
                even.next = None
            odd = odd.next
            even = even.next
        odd.next = even_head
        return head