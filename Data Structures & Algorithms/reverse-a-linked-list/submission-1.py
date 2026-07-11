# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        node1 = head
        node2= head.next
        temp =node2.next
        node1.next =None
        while node2:
            node2.next = node1
            node1 = node2
            if temp is None:
                return node2
            node2 = temp
            temp = temp.next




        