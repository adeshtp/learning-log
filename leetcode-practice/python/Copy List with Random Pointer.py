# Problem: Copy List with Random Pointer
# Approach: use a dictionary to store copies of nodes
# Logic: 
  # Create copies in first pass
  # Connect next and random in second pass
  # Return the copied head

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        mapping = {}
        current = head

        while current:
            mapping[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            mapping[current].next = mapping.get(current.next)
            mapping[current].random = mapping.get(current.random)
            current = current.next

        return mapping[head]
