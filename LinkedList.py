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
        preHead = ListNode(val = -999) # should be removed at last
        node = preHead
        while (l1 and l2):
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            
            node = node.next
        
        if l1:
            node.next = l1
        elif l2:
            node.next = l2
        
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
        
        left = head
        right = head
        rightNext = right.next
        while rightNext and rightNext.next:
            left = left.next
            right = rightNext.next
            rightNext = right.next
        
        if rightNext: # return the second middle node
            return left.next
        else: # return the middle node
            return left

    