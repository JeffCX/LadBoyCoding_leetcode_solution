"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        # [1,2,3,4,5,6, 7,8,9,10,11,12]
        
        if not head:
            return head

        stack = []
        dummyNode = result = Node(0)
        
        stack.append(head)
        
        while stack:
            
            cur = stack.pop()
            if cur:
                newNode = Node(cur.val)
                dummyNode.next = newNode
                newNode.prev = dummyNode
                dummyNode = dummyNode.next

                if cur.child:
                    stack.append(cur.next)
                    stack.append(cur.child)
                else:
                    stack.append(cur.next)
                    
        result.next.prev = None
        return result.next
            
