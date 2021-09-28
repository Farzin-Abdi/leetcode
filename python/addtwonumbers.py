class Solution:
    
    def addTwoNumbers(self, l1, l2):
        def get_list(node):
            outlist = []
            while node != None:
                outlist.append(str(node.val))
                node = node.next
            return outlist
        
        def get_listnode(lists):
            head = ListNode(lists[0])
            tail = head
            e = 1
            while e < len(lists):
                  tail.next = ListNode(lists[e])
                  tail = tail.next
                  e+=1
            return head
        
        l1_s, l2_s = int(''.join(get_list(l1)[::-1])), int(''.join(get_list(l2)[::-1]))
        z= ([int(x) for x in str(l1_s + l2_s)])[::-1]
        h = get_listnode(z)
        return h