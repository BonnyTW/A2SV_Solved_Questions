# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arr=[]
        pointer=head

        while pointer and pointer.next:
            arr.append(pointer.val)
            pointer=pointer.next
        if pointer:
            arr.append(pointer.val)
        
        left=[]
        right=[]

        for num in arr:
            if num<x:
                left.append(num)
            elif num>=x:
                right.append(num)
        ans=left+right
        
        dummy=ListNode()
        curr=dummy

        for num in ans:
            curr.next=ListNode(num)
            curr=curr.next
        return dummy.next
        