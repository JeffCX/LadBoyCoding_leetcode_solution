# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        """
            Time: O(n^2)
            Space: O(n)
        """
        
        if not root:
            return 0
        
        max_diff = float("-inf")
        
        stack = []
        stack.append(([],root))
        
        while stack:
            
            ancestors, node = stack.pop()

            current_val = node.val
            for number in ancestors:
                max_diff = max(max_diff, abs(number - current_val))
        
            if node.left:
                stack.append((ancestors+[current_val], node.left))
            
            if node.right:
                stack.append((ancestors+[current_val], node.right))
                
        return max_diff
