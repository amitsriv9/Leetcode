# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        0 1 2 3 4 5 6 7 8
        0 8 1 7 2 6 3 5 4
        0 1 2 3 ... 7 8
        left = 0
        right = len-1
        find the middle  
        """
        middle = self.findMinddle(head)
        self.shuffle(head, middle)


    def findMinddle(self, head):
        temp, middle = head, head
        move = False
        while temp.next != None:
            temp = temp.next
            if not move:
                move = True
            else:
                middle = middle.next
                move = False
        return middle
    
    def findLast(self, middle):
        node, prev = middle, None
        while node.next != None:
            prev = node
            node = node.next
        prev.next = None
        return node

    def shuffle(self, head, middle):
        current  = head
        while current != middle:
            temp = current.next
            last = self.findLast(middle)
            current.next = last
            last.next = temp
            current = temp


'''
Solution works but can be optimized
'''