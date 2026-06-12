# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorderlist = []
        if not root:
            return []
        print(f"inorderlist = {inorderlist} at root = {root.val}")
        inorderlist.extend(self.inorderTraversal(root.left))
        inorderlist.append(root.val)
        inorderlist.extend(self.inorderTraversal(root.right))
       
        return inorderlist

        