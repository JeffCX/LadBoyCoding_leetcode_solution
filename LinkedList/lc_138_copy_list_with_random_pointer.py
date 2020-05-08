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
        
        """
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        
        hashmap = {}
        
        dummyHead = result = Node(0)
        
        current = head
        
        while current:
            
            NewNode = Node(current.val)
            hashmap[current] = NewNode
            dummyHead.next = NewNode
            dummyHead = dummyHead.next
            current = current.next
            
        current = head
        while current:
            
            copiedNode = hashmap[current]
            random = current.random
            if random is not None:
                copiedRandom = hashmap[random]
                copiedNode.random = copiedRandom
            else:
                copiedNode.random = None
            current = current.next
                
        return result.next
        
        