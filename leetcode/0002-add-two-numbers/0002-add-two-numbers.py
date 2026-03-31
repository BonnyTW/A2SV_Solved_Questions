# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=[]
        num2=[]

        p1=l1
        while p1 and p1.next:
            num1.append(p1.val)
            p1=p1.next
        if p1:
            num1.append(p1.val)
        num1=int(''.join(str(num) for num in num1[::-1]))
        
        p2=l2
        while p2 and p2.next:
            num2.append(p2.val)
            p2=p2.next
        if p2:
            num2.append(p2.val)
        num2=int(''.join(str(num) for num in num2[::-1]))

        ans=str(num1+num2)
        
        dummy= ListNode()
        curr=dummy
        for num in ans[::-1]:
            curr.next=ListNode(int(num))
            curr=curr.next
        return dummy.next



        