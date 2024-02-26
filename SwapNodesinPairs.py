class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        while pre.next and pre.next.next:
            first = pre.next
            second = pre.next.next
            
            # Swapping
            first.next = second.next
            second.next = first
            pre.next = second
            
            # Move pre to the next pair
            pre = first
        
        return dummy.next
