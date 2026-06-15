class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
    
class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        dummyNode = TreeNode(key,val)
        if not self.root:
            self.root = dummyNode
            return

        curr = self.root
        while curr:
            if key > curr.key:
                if not curr.right:
                    curr.right = dummyNode
                    return
                curr = curr.right
            elif key < curr.key:
                if not curr.left:
                    curr.left = dummyNode
                    return
                curr = curr.left
            else:
                curr.val = val
                return

    


    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            elif key == curr.key:
                return curr.val

        return -1
            




    def getMin(self) -> int:
        curr = self.root
        if not curr:
            return -1
        while curr.left:
            curr = curr.left
        return curr.val



    def getMax(self) -> int:
        curr = self.root
        if not curr:
            return -1
        while curr.right:
            curr = curr.right
        return curr.val


    def remove(self, key: int) -> None:
        curr = self.root
        if not curr:
            return 
        def delete(node,key):
            if not node:
                return node
            
            if key > node.key:
                node.right = delete(node.right,key)
            elif key < node.key:
                node.left = delete(node.left, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    minNode = node.right
                    while minNode and minNode.left:
                        minNode = minNode.left
                    node.key = minNode.key
                    node.val = minNode.val
                    node.right = delete(node.right,minNode.key)

            return node
        self.root = delete(curr,key)
        




    def getInorderKeys(self) -> List[int]:
        curr = self.root
        inorderlist = []
        if not curr:
            return []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inorderlist.append(root.key)
            inorder(root.right)
            return inorderlist
            print(inorder(curr))
        return inorder(curr)


