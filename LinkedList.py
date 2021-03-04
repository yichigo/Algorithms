from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node


    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        node = head
        while node != None:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
        
        return False


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


    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = PriorityQueue()
        i = 0
        for i in range(len(lists)):
            node = lists[i]
            if node:
                q.put((node.val, i, node)) # use i to avoid tie
        
        preHead = ListNode(0) # should be removed at last
        node = preHead 
        # merge
        while q.qsize():
            _, i, node.next = q.get() # here get() is like list.pop()
            node = node.next
            if node.next:
                q.put((node.next.val, i, node.next))
        
        return preHead.next


    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        preHead = ListNode(val = 0, next = head) # preHead should be removed at last
        
        left = preHead
        right = left
        # make right n steps after left
        for i in range(n):
            right = right.next
            if right == None:
                return head
        
        # move right to the end, and left follows
        while right.next:
            left = left.next
            right = right.next
        
        # delete left.next, which is the nth from the end
        left.next = left.next.next
        
        return preHead.next


    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        left, right = head, head
        while right.next and right.next.next:
            left, right = left.next, right.next.next
        
        if right.next: # return the second middle node
            return left.next
        else: # return the middle node
            return left


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
    