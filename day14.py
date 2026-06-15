# 2465. Number of Distinct Averages
"""In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1. For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin. Given the head of a linked list with even length, return the maximum twin sum of the linked list.
Difficulty: Medium
Approach: Brute Force and 2 pointer"""

#Brute Force
def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None

        def lenOfLinkedList(node):
            if node is None:
                return 0
            return 1 + lenOfLinkedList(node.next)

        n = lenOfLinkedList(head)

        def traverseLL(node):
            curr = node
            count = 0

            while curr:
                count += 1
                if count == n//2:
                    curr.next = curr.next.next
                curr = curr.next
        
        traverseLL(head)
        return head

# Optimized - 2 pointer method(Slow-Fast)
def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None

    slow = head
    fast = head.next.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    slow.next = slow.next.next
    return head