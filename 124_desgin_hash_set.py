"""
basic hash set implmentations based on buckets
operations based on key - add, delete and fetch 
"""

class ListNode(object):
    def __init__(self, key, next):
            self.key = key
            self.next = next

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        bucket implementation(array of linkedlists)
        """
        self.size = 10000
        self.buckets = [None]*self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket_idx = key % self.size
        curr = self.buckets[bucket_idx]
        if not curr:
            # first time insert, create a list node
            self.buckets[bucket_idx] = ListNode(key, None)
            return
        if curr.key == key:
            return
        while curr:
            if curr.key == key:
                # return if curr in next iteration is matches key
                return
            if not curr.next:
                # link this new node to the existing
                curr.next = ListNode(key, None)
            if curr.next:
                # move to the next node and check again
                curr = curr.next
        return


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket_idx = key % self.size
        curr = self.buckets[bucket_idx]
        if not curr:
            # no such element to remove, do nothing
            return
        if curr.key == key:
            # very first element, adjust next
            curr = curr.next
            return
        # element lies deep in the list
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        return

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucket_idx = key % self.size
        curr = self.buckets[bucket_idx]
        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False
