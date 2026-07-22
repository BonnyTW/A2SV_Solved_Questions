# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        i = 0
        j = 1

        gcd_val = []

        while j < len(arr):
            gcd_val.append(gcd(arr[i],arr[j]))
            i += 1
            j += 1
        
        x = 0
        y = 0

        
        ans = []
        for i in range(len(arr)):
            ans.append(arr[i])
            if i < len(gcd_val):
                ans.append(gcd_val[i])
        
        temp = head

        for num in ans:
            temp.next = ListNode(num)
            temp = temp.next
        
        return head.next

        


        
