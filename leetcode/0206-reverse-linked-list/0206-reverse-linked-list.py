# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer=head
        arr=[]
        while pointer and pointer.next:
            arr.append(pointer.val)
            pointer=pointer.next
        if pointer:
            arr.append(pointer.val)

        arr=arr[::-1]
        dummy=ListNode()
        curr=dummy

        for num in arr:
            curr.next=ListNode(num)
            curr=curr.next
        return dummy.next
        
        