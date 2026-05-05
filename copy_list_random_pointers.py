"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        res={}
        curr = head
        while curr:
            res[curr]=Node(curr.val)
            curr=curr.next
        curr =head
        while curr:
            copy = res[curr]
            copy.next=res.get(curr.next)
            copy.random=res.get(curr.random)
            curr=curr.next
        return res[head]
