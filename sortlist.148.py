# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        last, mid = self.traverse(head)
        headnode = head
        while mid.next != None:
            self.sort(headnode, mid)
            self.traverse(head)
            headnode, mid = head.next, mid.next
        # self.traverse(head)
        return head

    def traverse(self, head):
        tempNode, midNode = head, head
        flag = False
        while tempNode.next != None:
            print(tempNode.val)
            tempNode = tempNode.next
            if flag:
                flag = False
                midNode = midNode.next
            else:
                flag = True
        print(tempNode.val)  
        return tempNode, midNode
    
    def sort(self, head, mid):
        print('Sorting: mid is ', mid.val)
        node = head.next 
        
        while node != mid:
            if head.val > node.val:
                temp  = head.val
                head.val = node.val
                node.val = temp
            if node.val > mid.val:
                temp  = mid.val
                mid.val = node.val
                node.val = temp
            node = node.next
        print('mid is ', mid.val)
        
        while node.next != None:
            if node.val < mid.val:
                temp  = mid.val
                mid.val = node.val
                node.val = temp
            node = node.next
        print('exiting')