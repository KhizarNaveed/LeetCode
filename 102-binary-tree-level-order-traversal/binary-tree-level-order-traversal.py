from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1. Edge Case: If the tree is empty, return an empty list
        if root is None:
            return []
        
        # 2. Initialize the Queue and the Result list
        queue = deque([root])
        result = []
        
        # 3. Loop while there are nodes in the queue
        while queue:
            # The magic trick: freeze the current size of the queue
            level_size = len(queue)
            current_level = []
            
            # 4. Process exactly 'level_size' nodes
            for _ in range(level_size):
                node = queue.popleft()          # Pop from the front
                current_level.append(node.val)  # Add to current level
                
                # Add children to the BACK of the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 5. Add the completed level to the result
            result.append(current_level)
            
        return result