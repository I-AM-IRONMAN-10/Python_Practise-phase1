def ListNode(self,val=0,next=None):
    self.val=val
    self.next=next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        def get_val(node):
            res = ""
            while node:
                res += str(node.val)
                node = node.next
            return int(res[::-1]) 

  
        total = get_val(l1) + get_val(l2)
        
      
        digits = str(total)[::-1]
        
     
        dummy = ListNode(0)
        current = dummy
        for d in digits:
            current.next = ListNode(int(d))
            current = current.next
            
        return dummy.next
