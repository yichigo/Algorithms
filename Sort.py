class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        preHead = ListNode(val =  float('-inf'), next = head)
        
        right = preHead
        while right.next: # the new incoming node
            value = right.next.val
            # find a location for the new node
            left = preHead
            while left.next.val <= value:
                if left == right:
                    break
                left = left.next
            
            if left != right: # insert right.next into left.next
                tmp = right.next
                right.next = right.next.next
                tmp.next = left.next
                left.next = tmp
            else:
                right = right.next
        
        return preHead.next


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        preHead = ListNode(val = -float('-inf')) # should be removed at last
        node = preHead
        while (l1 and l2):
            if l1.val <= l2.val:
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
            
            node = node.next
        
        node.next = l1 or l2
        return preHead.next


    # merge sort, nlog(n)
    def sortList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next):
            return head
        
        # find the mid node
        mid, right = head, head
        while (right.next) and (right.next.next):
            mid, right = mid.next, right.next.next
        
        # mid.next must exist, since len >= 2
        # split the list into [head ... mid], [mid.next ... end]
        mid.next, head2 = None, mid.next
        
        return self.mergeTwoLists(self.sortList(head), self.sortList(head2))
            
            