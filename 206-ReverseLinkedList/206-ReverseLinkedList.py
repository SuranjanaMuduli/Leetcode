# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # def reverseList(self, head):
    #     """
    #     :type head: Optional[ListNode]
    #     :rtype: Optional[ListNode]
    #     """
    #     prev, cur = None, head
    #     while cur:
    #         temp = cur.next
    #         cur.next = prev
    #         prev = cur
    #         cur = temp
    #     return prev
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        
        # Recurse to the end of the list
        reversed_head = self.reverseList(head.next)
        
        # Reverse the current node's pointer
        head.next.next = head
        head.next = None
        
        return reversed_head 

