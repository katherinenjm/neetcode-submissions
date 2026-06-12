# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bigList = []
        sublist = []
        queue = deque()
        level = 0
        if root:
            queue.append(root)
        

        while queue:
            sublist = []
            for i in range(len(queue)):
                curr = queue.popleft()
                print(f"level = {level}")
                # print(f"level = {level}, curr = {curr.val},sublist being reset")
                sublist.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            print(f"sublist = {sublist}, level = {level}")
            level += 1
        # print(f"level = {level}, curr = {curr.val},sublist being reset")
        
            bigList.append(sublist)
            print(f"sublist apopended to bigList")
            print(f"bigList = {bigList}")
        
            # print(f"queue = {queue}, len(queue) = {len(queue)}")
            
        return bigList
            
        
        