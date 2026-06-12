# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        def inorderTraverse(root):
            
            inorderlist = []
            def inorder(root):
                nonlocal k
                if not root or len(inorderlist)==k:
                    return 
                
                inorder(root.left)
                if len(inorderlist) <= k-1:
                    inorderlist.append(root.val)
                inorder(root.right)

            inorder(root)
            return inorderlist
        
        print(inorderTraverse(root))
        
        return inorderTraverse(root)[-1]
        