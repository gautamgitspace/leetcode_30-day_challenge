class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        prev = head
        
        while prev:
            if prev.next and prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return head
