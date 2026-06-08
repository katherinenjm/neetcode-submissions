class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        homepage = ListNode(homepage)
        self.curr = homepage
        

    def visit(self, url: str) -> None:
        newSite = ListNode(url)              #assign site as ListNode
        
        self.curr.next = newSite            #assign forward pointer of tail = newSite
        newSite.prev = self.curr            #assign backward pointer of new value to be the curr(previous tail)
        self.curr = newSite                 #update curr


    def back(self, steps: int) -> str:
        while self.curr.prev and steps>0:
            self.curr = self.curr.prev
            steps -=1
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        while self.curr.next and steps >0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val
        

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)