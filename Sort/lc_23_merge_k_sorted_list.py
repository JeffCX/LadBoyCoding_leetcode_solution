# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        head = point = ListNode(0)
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
                
        while not q.empty():
            
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            if node.next:
                q.put((node.next.val, node.next))
        
        return head.next
        
        
            
           
            
            
        
                
            
            
        