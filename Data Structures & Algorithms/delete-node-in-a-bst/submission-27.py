# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        def findMinNode(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        
        minInsertionNode = None
        print(f"root = {root.val}")
        
        if key < root.val:
            print(f"val = {key}, root = {root.val}, val<root => move down LHS of BST")
            root.left = self.deleteNode(root.left,key)

        elif key > root.val:
            print(f"val = {key}, root = {root.val}, val>root => move down RHS of BST")
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                print(f"root.right = {root.right.val}")
                minInsertionNode = findMinNode(root.right)
                print(f"minInsertionMode = {minInsertionNode.val}")
                minInsertionNode.left = root.left
                root = root.right
 
            # print(f" root.right = {root.right.val}")

        return root
        