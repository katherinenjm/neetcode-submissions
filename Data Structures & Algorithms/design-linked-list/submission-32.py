class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class MyLinkedList:

    

    def __init__(self):
        self.dummyleft  = ListNode(0)
        self.dummyright = ListNode(0)
        self.dummyleft.next = self.dummyright
        self.dummyright.prev = self.dummyleft

    def get(self, index: int) -> int:
        curr = self.dummyleft.next
        while curr and index >0:
            curr = curr.next
            index -= 1
        if curr and curr != self.dummyright and index == 0:
            return curr.val
        return -1
                
            

    def addAtHead(self, val: int) -> None:
        print(f"val added at head is {val}")
        newNode = ListNode(val)   #create new node with value

        newNode.prev = self.dummyleft # assign values to prev and next for newNode
        newNode.next = self.dummyleft.next

        newNode.next.prev = newNode # update  next pointer for dummy head node
        newNode.prev.next = newNode #update prev pointer for node adjacent to dummy head
        





            

    def addAtTail(self, val: int) -> None:
        print(f"val added at tail is {val}")
        #create new node with appropriate value
        newNode = ListNode(val)

        #assign values to newNode prev + next pointers
        newNode.next = self.dummyright
        newNode.prev = self.dummyright.prev

        #reassign pointers for nodes adj to newNode
        newNode.next.prev = newNode
        newNode.prev.next = newNode
            

    def addAtIndex(self, index: int, val: int) -> None:
        print(f"val = {val} added at index = {index}")
        #iterate through doublelinkedlist to reach index i
        curr = self.dummyleft.next
        while curr and index>0:
            curr = curr.next
            index -= 1
  
        if curr and curr != self.dummyright and index==0:
            newNode = ListNode(val)
            #assign newnode pointers
            newNode.next = curr
            newNode.prev = curr.prev

            #reassign pointers of nodes adkjacent to newNode
            newNode.next.prev = newNode
            newNode.prev.next= newNode
        
        if curr and curr == self.dummyright and index == 0:
            newNode = ListNode(val)

            #assign newnode pointers
            newNode.next = curr
            newNode.prev = curr.prev

            #reassign pointers of nodes adkjacent to newNode
            newNode.next.prev = newNode
            newNode.prev.next= newNode
        

      


            

    def deleteAtIndex(self, index: int) -> None:
        #iterate to find ith index
        curr = self.dummyleft.next
        while curr and index>0:
            curr = curr.next
            index -=1
        if curr and curr != self.dummyright and index == 0:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev



            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)