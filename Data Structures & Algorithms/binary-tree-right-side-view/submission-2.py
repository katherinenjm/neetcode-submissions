# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        biglist = []
        level = 0

        if root:
            queue.append(root)

            while queue:
                sublist = []
                for i in range(len(queue)):
                    curr = queue.popleft()
                    sublist.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)   
                    if curr.right:
                        queue.append(curr.right)
                level += 1 
                biglist.append(sublist[-1]) 
        return biglist
