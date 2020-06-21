class Solution(object):
    def deleteNode(self, node):
        """
        Q : delete a node in the LL given access to that node only
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
