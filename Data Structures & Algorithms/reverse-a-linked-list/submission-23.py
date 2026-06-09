# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # #need curr, curr.next, and prev
        # curr = head
        # prev = None
        # while curr:
        #     temp = curr.next # saving the next value for current value
        #     curr.next = prev #reversign the pointer for next it instead of l-> r we fo r->l
        #     prev = curr      #increment prev
        #     curr = temp      # increment c
        
        
        # return prev

        #base case
        if not head or not head.next:
            return head
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None


        return newHead
        