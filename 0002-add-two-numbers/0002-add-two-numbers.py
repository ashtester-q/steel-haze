# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        '''
        sum1 = 0
        x10 = 0
        current_node = l1
        while current_node != None:
            sum1 += current_node.val*(10**x10)
            x10 += 1
            current_node = current_node.next
        sum2 = 0
        x10 = 0
        current_node = l2
        while current_node != None:
            sum2 += current_node.val*(10**x10)
            x10 += 1
            current_node = current_node.next            
        '''
        def sum(ls):
            sum = 0
            x10 = 0
            current_node = ls
            while current_node != None:
                sum += current_node.val*(10**x10)
                x10 += 1
                current_node = current_node.next 

            return sum
        num1 = sum(l1)
        num2 = sum(l2)
        total = num1 + num2
        if total == 0:
            return ListNode(0)
        else:
            total_str_re = str(total)[::-1]
            head = ListNode(int(total_str_re[0]))
            current_node = head
            for i in range(1,len(total_str_re)):
                new_node = ListNode(int(total_str_re[i]))
                current_node.next = new_node
                current_node = new_node
            return head
                

