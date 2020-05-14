# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        """
            Space: O(1)
            Time: O(n)
        """
        
        # detect cycle
        def detect_cycle(node):
            
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            
            return None
       
        # find cycle
        intersection = detect_cycle(head)
        if intersection is None:
            return None
        
        start = head
        while start != intersection:
            start = start.next
            intersection = intersection.next
        return intersection
        
