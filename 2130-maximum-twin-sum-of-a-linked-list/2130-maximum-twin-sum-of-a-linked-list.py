class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # 3. Calculate the maximum twin sum
        max_sum = 0
        first_half = head
        second_half = prev  # 'prev' is the new head of the reversed second half
        
        while second_half:
            max_sum = max(max_sum, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next
            
        return max_sum
