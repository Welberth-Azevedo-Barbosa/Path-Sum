class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
         
        if root.left is None and root.right is None:
            return root.val == targetSum
        
        left_sum = targetSum - root.val
        has_left_path = self.hasPathSum(root.left, left_sum)
        has_right_path = self.hasPathSum(root.right, left_sum)
        
        return has_left_path or has_right_path