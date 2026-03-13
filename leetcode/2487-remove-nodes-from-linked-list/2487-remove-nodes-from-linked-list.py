# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        
        pointer=head

        while pointer and pointer.next:
            arr.append(pointer.val)
            pointer=pointer.next
        if pointer:
            arr.append(pointer.val)
        
        md_s=[]
        for num in arr:
            while md_s and md_s[-1]<num:
                md_s.pop()
            md_s.append(num)
        
        dummy=ListNode(md_s[0])
        head=dummy

        for i in range(1,len(md_s)):
            dummy.next=ListNode(md_s[i])
            dummy=dummy.next
        return head



            
        