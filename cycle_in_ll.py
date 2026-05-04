# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        r=t=head
        while r and r.next:
            t=t.next
            r=r.next.next
            if r==t:
                return True
        return False