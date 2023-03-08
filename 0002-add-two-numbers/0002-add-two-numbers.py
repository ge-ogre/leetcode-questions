# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x = y = 0
        acc = acc2 = 1
        cur, cur2 = l1, l2
        while cur:
            x += cur.val * acc
            acc *= 10
            cur = cur.next
        
        while cur2:
            y += cur2.val * acc2
            acc2 *=10
            cur2 = cur2.next
        
        ##new list
        acc3 = 1       
        root = cur3 = ListNode(0)
        for i in range(len(str(x+y))):
            cur3.next = ListNode((x+y) / acc3 % 10)
            cur3=cur3.next
            acc3*=10
        
        return root.next